d = {} # empty dict
d = {'key': 'value'} # dict with initial values


# Also unpacking one or multiple dictionaries with the literal syntax is possible
# makes a shallow copy of otherdict
# d = {**otherdict}
# also updates the shallow copy with the contents of the yetanotherdict.
# d = {**otherdict, **yetanotherdict}



# d = {k:v for k,v in [('key', 'value',)]}
d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])
# c 3
# b 2
# a 1

for key, value in d.items():
    print(key, value)
# c 3
# b 2
# a 1
