
# def f_decorator(fun) : # decorator


#     def deco_fun() : 
#         print("Decoration Before calling function") 
#         fun() 
#         print(" Decoration Before calling function ") 

#     return  deco_fun # return all data


# def f() :
#     print(" python 3 tutorial ")

# ff = f_decorator(f)
# ff()



def f_decorator(fun) : 


    def deco_fun() : 
        print("Before decoration") 
        fun() 
        print(" after decoration  ") 

    return  deco_fun 

@f_decorator
def f1() :
    print(" Hello  from f1 function")

@f_decorator
def f2():
    print(" Hello  from f2 function ")

f1()
f2()


