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

# do this task with list comp
new_list =[ i for i in list1 if i%2==0 ]
print(new_list)


# new_list = filter(lambda i: i>15 ,list1 )
print(new_list)
new_list = list(filter(lambda i: i>15 ,list1 )) # conversion
print(new_list)
for x in new_list:
  print(x)
  
new_list =[(i,j) for i in "python" for j in range(4)]
print(new_list)