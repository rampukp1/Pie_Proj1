import app
import pytest

@pytest.fixture
def client():
    app.app.testing = True
    return app.app.test_client()

def test_octocat_gists(client):
    response = client.get('/octocat')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    if response.json:
        assert "id" in response.json[0]
        assert "url" in response.json[0]
