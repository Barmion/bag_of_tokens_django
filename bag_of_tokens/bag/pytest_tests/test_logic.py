from http import HTTPStatus

import pytest
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertRedirects

from bag.models import Bag

pytestmark = pytest.mark.django_db


def test_user_can_add_token(owner_client, token):
    """Зарегистрированный пользователь может добавить жетон в мешок."""

    url = reverse('bag:add')

    response = owner_client.post(url,
                                 data={'token': token.id})
    assertRedirects(
        response,
        reverse_lazy('users:profile'),
        msg_prefix='После добавления жетона пользователь '
                   'должен перенаправляться на страницу профиля.'
    )
    assert Bag.objects.count() == 1, (
        'Убедитесь, что жетон создаётся в базе данных. '
        f'Ожидаемое число жетонов 1, полученное {Bag.objects.count()}.'
    )
    assert Bag.objects.first().id == token.id, (
        'Убедитесь, что жетон, переданный в форму, '
        'соответстувует жетону, созданному в базе данных.'
    )


def test_anonymous_user_cant_add_token(client, token):
    """Незарегистрированный пользователь не может добавить жетон."""
    url = reverse('bag:add')
    response = client.post(url, data={'token': token.id})
    login_url = reverse('login')
    expected_url = f'{login_url}?next={url}'
    assertRedirects(
        response,
        expected_url,
        msg_prefix='При попытке незарегистрированного пользователя'
                   'отправить форму добавления жетона,'
                   'он должен быть перенаправлен на страницу логина.'
    )
    assert Bag.objects.count() == 0, (
        'Убедитесь, что жетон не создаётся в базе данных. '
        f'Ожидаемое число жетонов 0, полученное {Bag.objects.count()}.'
    )


def test_owner_can_delete_token(owner_client, token_in_bag):
    """Пользователь может удалить жетон из своего мешка."""

    url = reverse('bag:delete', args=(token_in_bag.id,))
    response = owner_client.post(url)
    assertRedirects(
        response,
        reverse('users:profile'),
        msg_prefix='После удаления жетона пользователь '
                   'должен перенаправляться на страницу профиля.'
    )
    assert Bag.objects.count() == 0, (
        'Убедитесь, что жетон удаляется из базы данных. '
        f'Ожидаемое число жетонов 0, полученное {Bag.objects.count()}.'
    )


def test_not_owner_cant_delete_token(not_owner_client, token_in_bag):
    """Пользователь может удалить жетон из чужого мешка."""

    url = reverse('bag:delete', args=(token_in_bag.id,))
    response = not_owner_client.post(url)
    assert response.status_code == HTTPStatus.FORBIDDEN, (
        'Пользователь не должен иметь право на удаление чужих жетонов.'
    )
    assert Bag.objects.count() == 1, (
        'Убедитесь, что жетон не удаляется из базы данных. '
        f'Ожидаемое число жетонов 1, полученное {Bag.objects.count()}.'
    )
