'''Operation Tests'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Addition Test'''
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Addition failed"

def test_operation_subtract():
    '''Subtraction Test'''
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtraction failed"

def test_operation_multiply():
    '''Multiplication Test'''
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiplication failed"

def test_operation_divide():
    '''Division Test'''
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Division failed"

def test_divide_by_zero():
    '''Divide by 0 Test'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
