from src.util.dao import DAO
import pytest
import json
import os
#from unittest.mock import patch, MagicMock
import pymongo
from bson import json_util
from bson.objectid import ObjectId
from unittest.mock import patch

@pytest.fixture
def database():
    #setup
    #using todo cause it is the simplest in static/validators
    mockValidator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["description"],
            "properties": {
                "description": {
                    "bsonType": "string",
                    "description": "the description of a todo must be determined",
                    "uniqueItems": True
                }, 
                "done": {
                    "bsonType": "bool"
                }
            }
        }
    }
    with patch('src.util.validators') as MockValidator:
        MockValidator.return_value = mockValidator
        theDao = DAO('todo')
        yield theDao
        #teardown
        theDao.drop()

#Just testing so the database and dao connection works, not relevant with later tests
#This was just while setting up
#def test_create_example(database):
#    assert database

@pytest.mark.integration
def test_valid_key_val_pair(database):
    data = {'description': 'words'}
    res = database.create(data)
    assert '_id' in res
    assert isinstance(res['_id']['$oid'], str)

@pytest.mark.integration
def test_invalid_key(database):
    with pytest.raises(pymongo.errors.WriteError):
        data = {'willy_wonka': 'words'}
        database.create(data)

@pytest.mark.integration
def test_invalid_type(database):
    with pytest.raises(pymongo.errors.WriteError):
        data = {'description': 1}
        database.create(data)


