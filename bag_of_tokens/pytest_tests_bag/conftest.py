import pytest
from django.test.client import Client
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from bag.models import Bag, Token
from pytest_tests_bag.data import TOKENS


@pytest.fixture
def owner(django_user_model):
    return django_user_model.objects.create(username='owner',
                                            password='test',
                                            email='owner@test.com')


@pytest.fixture
def not_owner(django_user_model):
    return django_user_model.objects.create(username='notowner',
                                            password='test',
                                            email='notowner@test.com')


@pytest.fixture
def owner_client(owner):
    client = Client()
    client.force_login(owner)
    return client


@pytest.fixture
def not_owner_client(not_owner):
    client = Client()
    client.force_login(not_owner)
    return client


@pytest.fixture
def create_tokens():
    for token in TOKENS:
        Token.objects.create(
            name=token.get('fields').get('name'),
            char=token.get('fields').get('char'),
            sticker_id=token.get('fields').get('sticker_id'),
            image=token.get('fields').get('image'),
            ordering=token.get('fields').get('ordering'))


@pytest.fixture
def token():
    return Token.objects.create(
        name=TOKENS[0].get('fields').get('name'),
        char=TOKENS[0].get('fields').get('char'),
        sticker_id=TOKENS[0].get('fields').get('sticker_id'),
        image=TOKENS[0].get('fields').get('image'),
        ordering=TOKENS[0].get('fields').get('ordering'))


@pytest.fixture
def token_in_bag(token, owner):
    return Bag.objects.create(token=token, owner=owner)


@pytest.fixture
def token_in_bag_char(token_in_bag):
    return token_in_bag.token.char


@pytest.fixture
def token_in_bag_id_for_args(token_in_bag):
    return (token_in_bag.id,)


@pytest.fixture
def random_token(create_tokens):
    return Token.objects.order_by('?').first()


@pytest.fixture
def random_token_char(random_token):
    return random_token.char


@pytest.fixture
def create_bag(random_token, owner):
    for _ in range(10):
        Bag.objects.create(owner=owner, token=random_token)


@pytest.fixture
def owner_client_api(owner):
    client = APIClient()
    token = RefreshToken.for_user(owner).access_token
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
