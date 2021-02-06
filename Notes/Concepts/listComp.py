l=[i for i in range(10) ]

# more  examples
list1 = list(range(1,10))

new_list = [i*i for i in list1 ]
print(new_list)

list1 = list(range(1,20))
new_list =[]
for i in list1 :
    if i%2 ==0 :
        new_list.append(i)
print(new_list)