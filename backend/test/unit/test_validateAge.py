import pytest
import unittest.mock as mock

from src.util.helpers import ValidationHelper

@pytest.fixture
def sut(age: int):
    mockedusercontroller = mock.MagicMock()
    mockedusercontroller.get.return_value = {'age': age}
    mockedsut = ValidationHelper(usercontroller=mockedusercontroller)
    return mockedsut

