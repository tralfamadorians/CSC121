'''Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.'''

from employee import Employee

def test_give_default_raise():
    '''Test that a standard raise is given'''
    bob = Employee('bob', 'jones', 100000)
    bob.give_raise()
    assert bob.salary == 105000 

def test_give_custom_raise():
    '''Test that a custom raise is given'''
    tom = Employee('tom', 'smith', 100000)
    tom.give_raise(10000)
    assert tom.salary == 110000 