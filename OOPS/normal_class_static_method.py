class Employee:
    num_emp = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_emp += 1
    def fullname(self): #regular method
        # print(self.first + ' ' + self.last)
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amt): #class method
        cls.raise_amount = amt

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return Employee(first, last, pay)

    @staticmethod #no relation to class variables or instances, nly logical connection
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Rohit1', 'Kumar1', 50001)
emp2 = Employee('Rohit2', 'Kumar2', 50002)

Employee.set_raise_amount(1.05)
# Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp3 = Employee.from_string('Rohit3-Kumar3-50003')
print(emp3.email)

import datetime
my_date = datetime.date(2017, 7, 11)
print(Employee.isworkday(my_date))
