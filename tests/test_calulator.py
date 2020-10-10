import pytest
import os
print(os.getcwd())
from PCalculator import calculator

def tests_add_floats():
    assert calculator.add(2.0,4.5) == 6.5

def tests_add_str():
    assert calculator.add('2') == 2
    

def tests_add_integer():
    assert calculator.add(2,4,1,4) == 11
    assert calculator.add(2,4) == 6
