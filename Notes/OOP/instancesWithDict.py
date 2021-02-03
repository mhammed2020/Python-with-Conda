class Person:
    
    perform = 1.27
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.salary = salary
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def tax(self):
        self.salary = int(self.salary*self.perform) # or Person.perform
    
    
obj1 = Person('medo', 'guedo', 4000)
obj2 = Person('amina', 'ouj', 2500)

print(obj1.__dict__) #dict with instance
print(Person.__dict__) # dict with class