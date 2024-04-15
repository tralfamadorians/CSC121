'''11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.'''

class Employee:
    '''Collect basic employee information'''

    def __init__(self, first, last, salary):
        '''Store name and salary info'''
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase = 5000):
        '''$5000 raise'''
        self.salary += increase