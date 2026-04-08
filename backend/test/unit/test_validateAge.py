import pytest
import unittest.mock as mock

from src.util.helpers import ValidationHelper
from src.util.dao import DAO

from src.controllers.usercontroller import UserController

def test_validateAge():
    dao_obj = DAO(collection_name='user')
    usercontroller = UserController()
    validationhelper = ValidationHelper(usercontroller)


    mockedusercontroller = mock.MagicMock()
    mockedusercontroller.get.return_value = {"age": 17}



    validationhelper.validateAge();
    

