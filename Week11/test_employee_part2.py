'''Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.'''

import pytest
from employee import Employee

@pytest.fixture
def sample_employee():
    '''An employee available to all test functions'''
    return Employee('bob', 'jones', 100000)

def test_give_default_raise(sample_employee):
    '''Test that a standard raise is given'''
    sample_employee.give_raise()
    assert sample_employee.salary == 105000 

def test_give_custom_raise(sample_employee):
    '''Test that a custom raise is given'''
    sample_employee.give_raise(10000)
    assert sample_employee.salary == 110000 