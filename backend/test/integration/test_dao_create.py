from src.util.dao import DAO
import pytest
from unittest.mock import patch
import pymongo

@pytest.fixture
def database():
    dao = DAO('todo')
    yield dao
    dao.drop()

def test_create_example(database):
    assert database

def validator_criteria(database):
    data = {"something": "nothing"}
    result = database.create(data)
    assert result is Exception