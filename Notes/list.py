a = [1, 2, 3, 4, 5]

a.append(6)
a.append(7)
a.append(7)

#----------------------------
import datetime
class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height
    def __repr__(self):
        return self.name