class Person:
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.salary = salary

obj1 = Person('medo', 'guedo', 50000)
obj2 = Person('amina', 'ouj', 60000)
obj1.email

print(obj1.email)
print(obj2.email)