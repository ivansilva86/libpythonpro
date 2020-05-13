from unittest.mock import Mock
from libpythonpro import github_api
import pytest

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/4458?v=4'
    resp_mock.json.return_value = {
        'login': 'ivan', 'id': 4458,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('ivan')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('ivansilva86')
    assert 'https://avatars3.githubusercontent.com/u/63621288?v=4' == url
