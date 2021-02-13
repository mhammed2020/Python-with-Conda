class Person:
    def __init__(self,name="medo",job="enginner",age=20,salary=800):
        print(" init constructor")
        self.name = name
        self.job = job
        self.age = age
        self.salary = salary
    def firstName(self):
        print("Person first name is : {}".format(self.name))

    def personlName(self):
        print("the job is : {}".format(self.job))
    def personfullInfo(self):
        print("Person full information is : {} {} {} {}"
              .format(self.name, self.job,self.age,self.salary))

    def personfullName(self):
        print("Person full name is : {} {}"
              .format(self.name,self.job))