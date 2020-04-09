class Employee:
    num_emp = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_emp += 1
    def fullname(self):
        # print(self.first + ' ' + self.last)
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
#Class variables are variables that are shared among all the variable of the class
emp1 = Employee('Rohit1', 'Kumar1', 50001)
emp2 = Employee('Rohit2', 'Kumar2', 50002)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

#Changing the class variable with class name, reflects in all the instance
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
#But changing using a instance actually creates new instance variable
emp1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
#raise amounr is present as class variable, can be seen in dict of emp1
print(emp1.__dict__)
print(Employee.__dict__)

print(Employee.num_emp)
