#Set Comprehension

#output = {1:1, 2:4, 3:9}

#Normal Method

s = set(list(range(1,11)))
print(s)
print(type(s))

#Comprehension

name = "Mintu"
new_set = {n[0] for n in name}
print(new_set)
print(type(new_set))