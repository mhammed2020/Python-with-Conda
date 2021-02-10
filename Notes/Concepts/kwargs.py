# def f() : 
#     for i in range(10) : 
#         print (' inside function')

# f()


#-----------------

# def sum_function(a,b):
#         s = (a+b)/2
#         print ("sum is ",s)
# sum_function(20,34)

#-------------------------
def sum_function2(*listInput):
    s = 0
    for i in listInput :
        s += i
    print ("avg is ",s/(len(listInput)))
    print (listInput)
sum_function2(1,2,3,4,5,6,7,8,9,10)



def print_me(**values):
      for key, value in values.items():
    print("{} = {}".format(key,value))
print_me(one = 1,two = 2,three = 3,four = 4,five = 5)
