#Set Comprehension

#output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        # <class 'set'>
        # {'M', 'n', 'i', 't', 'u'}
        # <class 'set'>

#Normal Method

s = set(list(range(1,11)))
print(s)
print(type(s))

#Comprehension

name = "Mintu"
new_set = {n[0] for n in name}
print(new_set)
print(type(new_set))