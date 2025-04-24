import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_token_ordering(owner_client, create_bag):
    """На странице профиля жетоны отображаются по порядку."""
    url = reverse('users:profile')
    response = owner_client.get(url)
    tokens_list = response.context.get('tokens')
    token_ordering = [token.token.ordering for token in tokens_list]
    sorted_token_ordering = sorted(token_ordering)
    assert token_ordering == sorted_token_ordering, (
        'Убедитесь, что на странице профиля жетоны отсортированы по порядку.')
