import pytest
from src.util.helpers import hasAttribute

@pytest.fixture
def obj():
    return {"name": "Jane"}


@pytest.mark.unit
def test_hasAttribute_True(obj):
    res = hasAttribute(obj, "name")
    assert res == True


@pytest.mark.unit
def test_hasAttribute_False(obj):
    res = hasAttribute(obj, "age")
    assert res == False


# @pytest.mark.unit
# def test_hasAttribute_None():
#     res = hasAttribute(None, "age")
#     assert res == False
