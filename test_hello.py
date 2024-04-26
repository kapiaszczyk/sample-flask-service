"""Tests for the Flask app."""

import pytest

from hello import app as flask_app

HELLO_MESSAGE = "Hello, world!"

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
