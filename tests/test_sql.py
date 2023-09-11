import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import pytest

from lib.sql import *

def test_execute_sql_exception():
    db_conn = db_operations("mysql+pymysql://fake_db_conn")
    with pytest.raises(Exception):
        assert db_conn.execute_sql(sql="Select 1;")

def test_test_conn():
    with pytest.raises(Exception):
        assert db_operations.test_conn(None) == None

def test_execute_sql():
    with pytest.raises(Exception):
        assert db_operations.execute_sql(None) == None


