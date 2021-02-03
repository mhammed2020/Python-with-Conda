class Person:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

obj1 = Person('Corey', 'Schafer', 50000)
obj2 = Person('Test', 'Employee', 60000)