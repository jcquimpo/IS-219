'''Calculator Tests'''
from calculator import Calculator

def test_addition():
    '''Addition function Test'''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Subtraction function Test'''
    assert Calculator.subtract(2,2) == 0

def test_divide():
    '''Division function Test'''
    assert Calculator.divide(2,2) == 1

def test_multiply():
    '''Multiplication function Test'''
    assert Calculator.multiply(2,2) == 4
