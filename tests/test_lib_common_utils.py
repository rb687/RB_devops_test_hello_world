import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.common_utils import *
from datetime import datetime, date, timedelta
import pytest
from unittest.mock import patch, MagicMock, Mock


def test_is_request_valid_more_than_one_key():
    mock_req = {
        'dateofbirth': '2012-08-09',
        'fake': 'key'
    }
    assert is_request_valid(mock_req) is False

def test_is_request_valid_wrong_val_date_of_birth():
    mock_req = {
        'dateofbirth': '2012-08-09'
    }
    assert is_request_valid(mock_req) is False

def test_is_request_valid_success():
    mock_req = {'dateOfBirth': '2012-08-09'}
    assert is_request_valid(mock_req) is True

def test_is_dob_format_valid_success():
    date = "2012-08-09"
    assert is_dob_format_valid(date) is True

def test_is_dob_format_valid_failure():
    date = "08-09-2023"
    assert is_dob_format_valid(date) is False

def test_is_dob_before_today_failure():
    date = "2024-08-09"
    assert is_dob_before_today(date) is False


def test_is_dob_before_today_success():
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    assert is_dob_before_today(yesterday) is True
    
def test_is_dob_valid_success():
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    assert is_dob_valid(yesterday) is True

def test_is_dob_valid_failure():
    tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    assert is_dob_valid(tomorrow) is False
    
@patch("lib.common_utils.get_dob", Mock(return_value=datetime.today().strftime('%Y-%m-%d')))
def test_get_dob_message_0_day():
    assert "Happy Birthday!" in get_dob_message("fakeuser")

@patch("lib.common_utils.get_dob", Mock(return_value=(datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')))
def test_get_dob_message_2_day():
    assert "Your birthday is in 2 day (s)" in get_dob_message("fakeuser")


def test_is_username_valid_success():
    username = "richa"
    assert is_username_valid(username) is True

def test_is_username_valid_failure():
    username = "richa1"
    assert is_username_valid(username) is False

