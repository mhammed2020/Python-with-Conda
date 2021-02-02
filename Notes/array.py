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