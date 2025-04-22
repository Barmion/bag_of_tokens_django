from http import HTTPStatus

import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects


@pytest.mark.parametrize(
    'name',
    ('about', 'login', 'registration')
)
def test_pages_availability_for_anonymous_user(client, name):
    """Страница доступна для неавторизованного пользователя."""
    url = reverse(name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK, (
        f'Убедитесь, что страница {url} доступна '
        'для неавторизованного пользователя.'
    )


def test_logout_availability_for_anonymous_user(client):
    """Страница доступна для неавторизованного пользователя."""
    url = reverse('logout')
    response = client.post(url)
    assert response.status_code == HTTPStatus.OK, (
        f'Убедитесь, что страница {url} доступна '
        'для неавторизованного пользователя.'
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, args',
    (
        ('users:profile', None),
        ('users:edit_profile', None),
        ('bag:add', None),
        ('bag:delete', pytest.lazy_fixture('token_in_bag_id_for_args')),
        ('bag:random', None)
    ),
)
def test_redirects(client, name, args):
    """Перенаправление неавторизованных пользователей на страницу логина."""
    login_url = reverse('login')
    url = reverse(name, args=args)
    expected_url = f'{login_url}?next={url}'
    response = client.get(url)
    assertRedirects(response, expected_url), (
        'Убедитесь, что неавторизованный пользователь перенаправляется '
        f'на страницу логина при переходе на страницу {url}.'
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    (
        (pytest.lazy_fixture('not_owner_client'), HTTPStatus.FORBIDDEN),
        (pytest.lazy_fixture('owner_client'), HTTPStatus.OK)
    ),
)
def test_delete_token_for_different_users(
    parametrized_client,
    expected_status,
    token_in_bag_id_for_args
):
    """Доступность страниц удаления жетона."""
    url = reverse('bag:delete', args=token_in_bag_id_for_args)
    response = parametrized_client.get(url)
    assert response.status_code == expected_status, (
        f'Убедитесь, что страница {url} доступна для авторизованного '
        'пользователя и недоступна для неавторизованного.'
    )
