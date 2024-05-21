import pytest


@pytest.mark.one
def test_method1():
    x=10
    y=20
    assert x==y


@pytest.mark.two
def test_method2():
    a=2
    b=3
    assert a + b == 5

def test_method3():
    x=10
    y=10
    assert x==y


@pytest.mark.two
def test_method4():
    a=2
    b=2
    assert a + b == 7
