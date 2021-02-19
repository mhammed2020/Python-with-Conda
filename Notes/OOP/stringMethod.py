# str1 = "Nour Eddine"
# print(str1,len(str1))
# str2 = "     Nour Eddine     "
# print(str2,len(str2))
#
# name = "tom" # a string
# mychar = 'a' # a character
# print(name)
# print(mychar)
#
# name1 = str() # this will create empty string object
# name2 = str("newstring") # string object containing 'newstring'
# print(name1)
# print(name2)

# Python String  Method
str22 = "        Hello morocco      "
# print(str22,len(str22))
# # strip method
# print(str22.strip())
# print(str22.lstrip())
# print(str22.rstrip())
# strip args ... space is the default args
str22 = "Amazing     Hello morocco     Bye"
# print(str22.strip()) # strip method not working ??
# str22 = "---------     Hello morocco     ------"
# print(str22.strip()) # strip method not working ??
# print(str22.strip("-")) # passing new args
# print(str22.rstrip("-")) # passing new args
# print(str22.lstrip("-")) # passing new args

# str22 = "casa     Hello morocco     casa"
# print(str22.strip()) # strip method not working ??
# print(str22.strip("casa")) # passing new args
# print(str22.rstrip("casa")) # passing new args
# print(str22.lstrip("casa")) # passing new args

# title,capitalize method.
a = "i love apples, apple are my favorite fruit"
# print(a.title())
# print(a.capitalize())
# print(a.upper()) # test lower

#zfill
# a,b,c,d ="2","22","222","2222"
# print(a)
# print(a.zfill(4))
# print(b.zfill(4))
# print(c.zfill(4))
# print(d.zfill(4))

# split method ------------------------------------------------------
# a = "i love apples, apple are my favorite fruit"
# print(a.split()) # space is the default separator args
# a = "iloveapples,appleare my favorite fruit"
# print(a.split()) # space is the default separator args

# a = "i love - apples, - apples are - my favorite fruit"
# print(a.split("-")) # space is the default separator args

# # maxsplit args
# a = "i love - apples, - apple are - my favorite-fruit"
# print(a.split("-")) # space is the default separator args
# print(a.split("-",3)) # space is the default separator args

# maxsplit args from right
# a = "i love - apples, - apple are - my favorite-fruit"
# print(a.split("-")) # space is the default separator args
# print(a.rsplit("-",3)) # space is the default separator args

# center method
#
# name = " Guido van Rossum "
# print(name.center(30))  # space default
# print(name.center(30,"-"))
# print(name.center(30,"*"))

# count method

name = """ Van Rossum was born and science raised in the Netherlands, where he received 
a master's degree in mathematics and 
computer science from Rossum the University of 
Amsterdam in 1982 """
# print(name.count("science"))
# print(name.count("and"))
# #count args
# print(name.count("and",0,50)) #
#
# # swapcase
# name = " Guido van Rossum "
# print(name.swapcase())
# new_name = name.swapcase()
# print(new_name.swapcase())

# logical test
# name = "Guido van Rossum "
# print(name.startswith("G"))
# print(name.startswith("i"))
# print(name.startswith("G",1,10)) # passing args to startswith

# name = "Guido van Rossum"
# print(name.endswith("G"))
# print(name.endswith("m"))
# print(name.endswith("n",3,9)) # passing args to startswith

# substring
name = "Guido van Rossum python "
# print(name.index("n")) # returns the index
# # print(name.index("n",0,5)) # returns the index ValueError: substring not found
# print(name.index("n",0,10))
#find
# print(name.find("n")) # returns the index
# print(name.find("n",0,5)) # returns -1
# print(name.find("n",0,10))

#rjust , ljust

# name = " Guido van Rossum python "
# print(name.rjust(len(name)+10)) # space is the default args
# print(name.rjust(len(name)+10,"-"))


# name = " Guido van Rossum python "
# print(name.ljust(len(name)+10)) # space is the default args
# print(name.ljust(len(name)+10,"-"))

#replace method

# name = ' Guido van Rossum python is number one '
# print(name.replace("number one","the best")) # accepts mores args
# name = ' Guido van Rossum python is number one van Rossum one  Guido van Rossum python is one '
# print(name)
# print(name.replace("one","the best")) # accepts mores args
# print(name.replace("one","the best",2)) # replace 2 times

# join --from list to string vs split
names = [ "Guido", "van Rossum", "python" ,"number one"]
print(names)
print(" ".join(names))
x = " ".join(names)
print(x,type(x))

