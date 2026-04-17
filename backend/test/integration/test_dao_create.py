from src.util.dao import DAO
import pytest
import os
#from unittest.mock import patch, MagicMock
#import pymongo

@pytest.fixture
def database():
    #setup
    #using todo cause it is the simplest in static/validators
    theDao = DAO('todo')
    yield theDao
    #teardown
    theDao.drop()

#Just testing so the database and dao connection works, not relevant with later tests
#This was just while setting up
#def test_create_example(database):
#    assert database




