# import numpy  as np 
# list1 = ' '.join([str(i) for i in np.random.randint(10,size=100)])

# print(list1)

import re
x = "*****" + '{:^10}'.format('bonjour') + "***"
print(x)



def function_avg(**args):
    sum = 0
    
    for i in args :
        sum+=i
    print("avg is ", sum/(len(args)))
    print(args)