
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raises(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Umang', 'Agarwal', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())

print(emp_1.pay)
# emp_1.apply_raises()
# print(emp_1.pay)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06

print(emp_1.__dict__)

print (Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.apply_raises()
print(emp_1.pay)

print(Employee.num_of_emps)