from http import HTTPStatus

import pytest
from django.urls import reverse


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
        'Убедитесь, что неавторизованный пользователь не имеет доступа к '
        f'эндпоинту {url}.'
    )


# @pytest.mark.parametrize(
#     'name, method, data',
#     (('api_v1:bag', 'get', None),
#      ('api_v1:random', 'get', None),
#     #  ('api_v1:add', 'post', {'token': pytest.lazy_fixture()}),
#     #  ('api_v1:delete', 'delete')
#      )
# )
# def test_get_bag_api(owner_client, name, method, data):
#     """Эндпоинты доступны для авторизованных пользователей."""
#     url = reverse(name)
#     response = getattr(owner_client, method)(
#         url,
#         headers=header
#         data=data)
#     assert response.status_code == HTTPStatus.OK, (
#         'Убедитесь, что авторизованный пользователь имеет доступа к '
#         f'эндпоинту {url}.'
#     )
