
def f_Generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
res =f_Generator() 
print(next(res))
print("hello flask")
print(next(res))
print("hello flask")
print(next(res))
print("hello flask")
print(next(res))

#----- with loop
for i in res :
    print(i)