class Velo:
    roues = 2
    var1 = " hello "
    var2= " buna"
    def __init__(self, marque, prix, poids):
        self.marque = marque
        self.prix = prix
        self.poids = poids

    def f(a):
        print("inside f")

#create object == instantiate
velo = Velo(marque="Peugeot", prix=500, poids=100)
print(velo.var1)
print(velo.var2)


velo_01 = Velo("btwin", 250, 15)
velo_02 = Velo("rockrider", 170, 12)

print(velo_01.roues) # 2
print(velo_02.roues) # 2

print(velo_01.marque) # btwin
print(velo_02.marque) # rockrider'