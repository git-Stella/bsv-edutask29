import pytest
from src.util.helpers import hasAttribute

@pytest.fixture
def obj():
    return {'name': 'jane'}

@pytest.mark.unit
def test_hasAttribute_True(obj):
    #print("Systems checking")
    #obj = {'name': 'jane'}
    res = hasAttribute(obj, "name")
    assert res is True

@pytest.mark.unit
def test_hasAttribute_False(obj):
    #print("Systems checking")
    #obj = {'name': 'jane'}
    res = hasAttribute(obj, "height")
    assert res is False

@pytest.mark.unit
def test_hasAttribute_Empty():
    #print("Systems checking")
    #obj = {}
    res = hasAttribute(None, "height")
    assert res is False
