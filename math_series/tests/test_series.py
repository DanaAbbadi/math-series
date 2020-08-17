from math_series import __version__
from math_series.series import a,fib,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_a():
    assert a == 6

def test_fib3(): 
    expected = 2
    received = fib(3)
    assert expected == received

def test_fib7():
    expected = 13
    received = fib(7)
    assert expected == received


def test_lucas5():
    expected = 11
    received = lucas(5)
    assert expected == received

def test_lucas7():
    expected = 29
    received = lucas(7)
    assert expected == received

def test_sumfib7():
    expected = 13
    received = sum_series(7)
    assert expected == received

def test_sumLucas7():
    expected = 29
    received = sum_series(7,first=2,second=1)
    assert expected == received
