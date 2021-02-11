
def f_decorator(fun) : # decorator


    def deco_fun() : 
        print("Decoration Before calling function") 
        fun() 
        print(" Decoration Before calling function ") 

    return  deco_fun # return all data


def f() :
    print(" python 3 tutorial ")

ff = f_decorator(f)
ff()