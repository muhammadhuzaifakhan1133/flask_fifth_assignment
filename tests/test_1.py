import sys
sys.path.append(".")
from flask.testing import FlaskClient
import pytest
from main import app


@pytest.fixture
def app():
    app.config.update({
        "TESTING": True,
    })
    print("Before yeild")
    yield app
    print("After yeild")

@pytest.fixture
def client(app) -> FlaskClient:
    return app.test_client()

def test_happy_login(client):
    response = client.post("/user/login", json={
        "email": "admin@gmail.com",
        "password": "admin"
    })
    data = response.json
    print(data)