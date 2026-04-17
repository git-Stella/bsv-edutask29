import pytest
import os
from unittest.mock import MagicMock
from src.util.dao import DAO


@pytest.fixture
def db():
    MagicMock(DAO)



#def test_create_():
    