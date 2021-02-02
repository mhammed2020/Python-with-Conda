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

