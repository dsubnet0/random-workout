import pytest


@pytest.mark.parametrize('mode', ['push', 'pull', 'legs'])
def test_modes(test_client, mode):
    response = test_client.get(f'/ppl/{mode}')
    assert response.status_code == 200
    assert b'1: ' in response.data


def test_bad_mode(test_client):
    '''
    A nonsense ppl mode should (for now) still return
    200 (it'll just be empty)
    '''
    response = test_client.get('/ppl/foo')
    assert response.status_code == 200
