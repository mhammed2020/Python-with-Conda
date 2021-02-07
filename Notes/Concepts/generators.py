list1 = [x * 2 for x in range(4)] 
for i in list1:
 print(i)
 
 
 def generator():
     list1 = range(4)
     for i in list1:
        yield i*2
