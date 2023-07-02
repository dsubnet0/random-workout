def test_raw(test_client):
    response = test_client.get('/raw/2')
    assert response.status_code == 200
    assert b'1: ' in response.data
    assert b'2: ' in response.data
