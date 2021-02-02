my_array = [1,2,3,4,5]
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
# 1

#
for i in my_array:
    print(i)
# 1
# 2
# 3
# 4
# 5

my_array = [1,2,3,4,5]
my_array.append(6)
#  [1, 2, 3, 4, 5, 6]

my_array = [1,2,3,4,5]
my_array.insert(0,0)
#[0, 1, 2, 3, 4, 5]



my_array = [1,2,3,4,5]
my_extnd_array = [7,8,9,10]
my_array.extend(my_extnd_array)
# [1, 2, 3, 4, 5, 7, 8, 9, 10]

my_array = [1,2,3,4,5]
my_array.remove(4)
#  [1, 2, 3, 5]


my_array = [1,2,3,4,5]
my_array.pop()
# [1, 2, 3, 4]





my_array =  [1,2,3,4,5]
print(my_array.index(5))
# 5
my_array = [1,2,3,3,5]
print(my_array.index(3))
# 3



my_array = [1,2,3,4,5]
my_array.reverse()
# [5, 4, 3, 2, 1]

my_array = [1,2,3,3,5]
my_array.count(3)
# 2




my_char_array = ['g','e','e','k']
# array('c', 'geek')
print(str(my_char_array))
# geek



c = list(range(0,10))
print(c)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



#Multidimensional arrays

lst=[[1,2,3],[4,5,6],[7,8,9]]
print (lst[0])
#output: [1, 2, 3]
print (lst[1])
#output: [4, 5, 6]
print (lst[2])
#output: [7, 8, 9]



print (lst[0][0])
#output: 1
print (lst[0][1])
#output: 2

lst[0]=[10,11,12]

lst[1][2]=15

# Lists in lists in lists in..
[[[111,112,113],[121,122,123],[131,132,133]],[[211,212,213],[221,222,223],[231,232,233]],[[311,312,
313],[321,322,323],[331,332,333]]]




[[[111,112,113],[121,122,123],[131,132,133]],\
[[211,212,213],[221,222,223],[231,232,233]],\
[[311,312,313],[321,322,323],[331,332,333]]]