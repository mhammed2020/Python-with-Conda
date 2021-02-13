# class Velo:
#     roues = 2
#     var1 = " hello "
#     var2= " buna"
#     def __init__(self, marque, prix, poids):
#         self.marque = marque
#         self.prix = prix
#         self.poids = poids

#     def f(a):
#         print("inside f")

# velo = Velo(marque="Peugeot", prix=500, poids=100)
# print(velo.var1)
# print(velo.var2)


# velo_01 = Velo("btwin", 250, 15)
# velo_02 = Velo("rockrider", 170, 12)

# print(velo_01.roues) # 2
# print(velo_02.roues) # 2

# print(velo_01.marque) # btwin
# print(velo_02.marque) # rockrider'




# class Velo:
#     roues = 2
#     def __init__(self, marque, prix, poids):
#         self.marque = marque
#         self.prix = prix
#         self.poids = poids

#     def rouler(self):
#         print("Wouh, ça roule mieux avec un vélo {} !".format(self.marque))

# # create new object
# velo_01 = Velo("btwin", 250, 15)


class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)


#

class Opers:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def div(self):
        print(self.num1/self.num2)
    def multi(self):
        print(self.num1*self.num2)

mathO = Opers(4,2)
mathO1 = Opers(3,6)

#--------------------------

mathO.sum()
mathO1.sum()
mathO.div()
mathO.sub()
mathO.multi()