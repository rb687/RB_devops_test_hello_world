import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import pytest
from unittest.mock import patch, MagicMock, Mock
from main import app

@pytest.fixture
def client():
    app.config.update({"testing": True})
    with app.test_client() as client:
        yield client

def test_hello_world_health_check_message(client):
    resp = client.get("/")
    assert b"I am up and running" in resp.data

def test_hello_world_health_check_status_code(client):
    resp = client.get("/")
    assert resp.status_code == 200


@patch("main.is_username_valid", Mock(return_value=True))
@patch("main.user_exists", Mock(return_value=True))
@patch("main.get_dob_message", Mock(return_value="1993-09-09"))
def test_hello_world_get_success(client):
    resp = client.get("/Hello/richa")
    assert b"1993-09-09" in resp.data


@patch("main.is_username_valid", Mock(return_value=True))
@patch("main.user_exists", Mock(return_value=False))
@patch("main.get_dob_message", Mock(return_value=None))
def test_hello_world_get_204(client):
    resp = client.get("/Hello/richa")
    assert resp.status_code == 204

@patch("main.is_username_valid", Mock(return_value=False))
@patch("main.user_exists", Mock(return_value=False))
@patch("main.get_dob_message", Mock(return_value=None))
def test_hello_world_get_400(client):
    resp = client.get("/Hello/richa123")
    assert resp.status_code == 400


@patch("main.is_request_valid", Mock(return_value=True))
@patch("main.update_db", Mock(return_value=True))
@patch("main.get_dob_message", Mock(return_value=None))
def test_hello_world_put_success(client):
    mock_data = {'dateOfBirth': '1993-09-09'}
    resp = client.put("/Hello/richa", json=mock_data)
    assert resp.status_code == 204

@patch("main.is_request_valid", Mock(return_value=False))
def test_hello_world_put_failure(client):
    mock_data = {'dateOfBirth': '1993-09-09'}
    resp = client.put("/Hello/richa", json=mock_data)
    assert resp.status_code == 400

@patch("main.is_request_valid", Mock(return_value=False))
def test_hello_world_put_failure(client):
    mock_data = {'dateOfBirth': '1993-09-09'}
    resp = client.post("/Hello/richa", json=mock_data)
    assert resp.status_code == 405
