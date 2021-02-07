def decorator_func(function): # function as arguments

    def new_function(a, b): 
        print('Add 2 numbers  {} and {}'.format(a, b))
        res = function(a, b) 
        print('Result : {}'.format(res))
        return res
    return new_function 

@decorator_func
def addition(a,b) :
    return a+ b
addition(1, 2)
