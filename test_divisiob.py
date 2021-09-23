from main import division, parity,rounded,size_less_a,first_int,size_more_a
import pytest
@pytest.mark.parametrize("a,b,expected_result",[(10,2,5)])
def test_division(a,b,expected_result):
    assert division(a,b)==expected_result


def test_parity():
    assert parity(7)

def test_rounded():
    assert rounded(5)

def test_size_less_a():
    a=4
    dict={"a":1, "b":2,"c":3}
    assert size_less_a(dict,a)
def test_first_int():
    key="a"
    dict = {"a": 1, "b": 2, "c": 3}
    assert first_int(dict,key)
@pytest.mark.parametrize("dict,a",[({"a":1, "b":2,"c":3},4)])
def test_size_more_a(dict,a):
    assert size_more_a(dict,a)