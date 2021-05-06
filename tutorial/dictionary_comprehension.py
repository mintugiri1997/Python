#Dictionary Comprehension

#output = {1: 1, 2: 4, 3: 9}
        # {1: 1, 2: 4, 3: 9}
        # 1:odd
        # 2:even
        # 3:odd
        # 4:even
        # 5:odd
        # 6:even
        # 7:odd
        # 8:even
        # 9:odd
        # 10:even

#Normal Method

new_dictionary = {}
for i in range(1,4):
    new_dictionary[i] = i**2
print(new_dictionary)

#Comprehension Method
dict_comprehension = {i:i**2 for i in range(1,4)}
print(dict_comprehension)

#Comprehension with  if else condition
odd_even = {i:("even" if i%2 == 0 else "odd") for i in range(1,11)}
for k,v in odd_even.items():
    print(f"{k}:{v}")
