from http import HTTPStatus

import pytest
from django.urls import reverse

from bag.models import Bag


@pytest.mark.parametrize(
    'name, method',
    (('api_v1:bag', 'get'),
     ('api_v1:random', 'get'),
     ('api_v1:add', 'post'),
     ('api_v1:delete', 'delete'))
)
def test_for_anonimous_api(client, name, method):
    """Отказ в доступе для неавторизованных пользователей."""
    url = reverse(name)
    response = getattr(client, method)(url)
    assert response.status_code == HTTPStatus.UNAUTHORIZED, (
        'Убедитесь, что неавторизованный пользователь не имеет доступ к '
        f'эндпоинту {url}.'
    )


def test_get_bag_api(owner_client_api, create_bag):
    """Эндпоинты доступны для авторизованных пользователей."""
    url = reverse('api_v1:bag')
    response = owner_client_api.get(url)
    assert response.status_code == HTTPStatus.OK, (
        'Убедитесь, что авторизованный пользователь имеет доступ к '
        f'эндпоинту {url}.')
    assert len(response.data) == 10


def test_get_random_api(owner_client_api, owner, create_bag):
    """Эндпоинты доступны для авторизованных пользователей."""
    bag = Bag.objects.filter(owner=owner)
    url = reverse('api_v1:random')
    response = owner_client_api.get(url)
    assert response.status_code == HTTPStatus.OK, (
        'Убедитесь, что авторизованный пользователь имеет доступ к '
        f'эндпоинту {url}.')
    assert bag.filter(token__char=response.data.get('token')) is not None


@pytest.mark.parametrize(
    'url, excpected_status',
    (('api_v1:bag', HTTPStatus.OK),
     ('api_v1:random', HTTPStatus.OK))
)
def test_empty_bag_api(owner_client_api, url, excpected_status):
    """Эндпоинты доступны для авторизованных пользователей."""
    url = reverse(url)
    response = owner_client_api.get(url)
    assert response.status_code == excpected_status, (
        'Убедитесь, что авторизованный пользователь имеет доступ к '
        f'эндпоинту {url}.')


@pytest.mark.parametrize(
    'char, excpected_status, expected_number',
    ((pytest.lazy_fixture('random_token_char'), HTTPStatus.CREATED, 1),
     ('17', HTTPStatus.BAD_REQUEST, 0))
)
def test_get_add_api(
    owner_client_api,
    char,
    excpected_status,
    expected_number
):
    """Эндпоинты доступны для авторизованных пользователей."""
    url = reverse('api_v1:add')
    response = owner_client_api.post(url, data={'token': char})
    assert response.status_code == excpected_status, (
        'Убедитесь, что авторизованный пользователь имеет доступ к '
        f'эндпоинту {url}.')
    assert Bag.objects.count() == expected_number


@pytest.mark.parametrize(
    'char, excpected_status, expected_number',
    ((pytest.lazy_fixture('token_in_bag_char'), HTTPStatus.NO_CONTENT, 0),
     ('17', HTTPStatus.NOT_FOUND, 0))
)
def test_get_delete_api(
    owner_client_api,
    char,
    excpected_status,
    expected_number,
):
    """Эндпоинты доступны для авторизованных пользователей."""
    url = reverse('api_v1:delete')
    response = owner_client_api.delete(url, data={'token': char})
    assert response.status_code == excpected_status, (
        'Убедитесь, что авторизованный пользователь имеет доступ к '
        f'эндпоинту {url}.')
    assert Bag.objects.count() == expected_number
