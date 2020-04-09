class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        # print(self.first + ' ' + self.last)
        return f'{self.first} {self.last}'

emp1 = Employee('Rohit1', 'Kumar1', 50001)
emp2 = Employee('Rohit2', 'Kumar2', 50002)

print(emp1.email)
print(emp2.email)

#Both below are same
print(emp1.fullname())
print(Employee.fullname(emp1))
# emp1.first = 'Rohit'
# emp1.last = 'Kumar'

# emp2.first = 'Rohit2'
# emp2.last = 'Kumar2'
# emp2.last1 = 'Kumar21'

# print(emp2.last1)
