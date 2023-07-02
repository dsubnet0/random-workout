from serve import app
from pytest import fixture

@fixture(scope='module')
def test_client():
    app.config['TESTING'] = True

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
