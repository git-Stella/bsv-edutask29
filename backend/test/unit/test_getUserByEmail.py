import pytest
from src.controllers.usercontroller import UserController
import unittest.mock as mock

#I dont have to test dao
#So I can just tell the dao to return that it does not exist
###
@pytest.mark.unit
def test_get_user_by_email_invalid():
    mockedDao = mock.MagicMock()
    mockedController = UserController(dao=mockedDao)
    with pytest.raises(ValueError):
        mockedController.get_user_by_email('test')

#email valid but does not exist
@pytest.mark.unit
def test_get_user_by_email_invalid_no_exists():
    mockedDao = mock.MagicMock()
    mockedController = UserController(dao=mockedDao)
    #mockedDao.find.return_value = Exception
    with pytest.raises(ValueError):
        mockedController.get_user_by_email('test')

#email valid but does not exist
@pytest.mark.unit
def test_get_user_by_email_valid_no_exists():
    mockedDao = mock.MagicMock()
    mockedController = UserController(dao=mockedDao)
    #mockedDao.find.return_value = Exception
    with pytest.raises(Exception):
        mockedController.get_user_by_email('correct@mail.coop')

#email valid and does exist
@pytest.mark.unit
def test_get_user_by_email_valid_exists():
    mockedDao = mock.MagicMock()
    mockedController = UserController(dao=mockedDao)
    mockedDao.find.return_value = ['correct@mail.coop']
    validationRes = mockedController.get_user_by_email('correct@mail.coop')
    assert validationRes == 'correct@mail.coop'
