"""Tests for the Flask app."""

import pytest

from hello import app as flask_app

HELLO_MESSAGE = "Hello, world!"
GOODBYE_MESSAGE = "Goodbye, world!"
HELLO_NAME_MESSAGE = "Hello, {}!"
WEATHER_MESSAGE = "Nice weather, ain't it?"


@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    flask_app.config['TESTING'] = True

    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client


def test_hello_world(client):
    """Should return a JSON response with a message saying 'Hello, world!'."""
    response = client.get('/')
    assert response.get_json() == {"message": HELLO_MESSAGE}
    assert response.status_code == 200


def test_goodbye_world(client):
    """Should return a JSON response with a message saying 'Goodbye, world!'."""
    response = client.get('/goodbye')
    assert response.get_json() == {"message": GOODBYE_MESSAGE}
    assert response.status_code == 200


def test_hello_name(client):
    """Should return a JSON response with a message using the provided name."""
    name = "Caroline"
    response = client.get(f'/hello/{name}')
    assert response.get_json() == {"message": HELLO_NAME_MESSAGE.format(name)}
    assert response.status_code == 200


def test_weather(client):
    """Should return a JSON response with a message about the weather."""
    response = client.get('/weather')
    assert response.get_json() == {"message": WEATHER_MESSAGE}
    assert response.status_code == 200
