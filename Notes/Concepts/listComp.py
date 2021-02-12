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

# list comprehension

list1 = ["medo", "houma", "jeams", "mady", "mola", "karim"]

res = filter(lambda name: name.startswith("m"), list1)

print(res)
for i in res:
      print(i)

# 2 method with simple for loop
l=[]
for i in list1 :
    if i.startswith("m"):
        print(i)
        l.append(i)
print(l)

#--------------------------------------

#  list comp with nested loop
l = [ (i,j) for i in ["x","y","z"] for j in[1,2] ]
print(l)


#  list comp with dictionaries and others objects
list1 =["medo","mamado","ahmed","Amina","wael"]
list2 =["casa","bamako","paris","berlin","rabat"]
# with list comprehesnion can match 2 lists using zip function
print(list1,list2)
a =zip(list1,list2)
print(a)
print(type(a))
print(list(zip(list1,list2)))
