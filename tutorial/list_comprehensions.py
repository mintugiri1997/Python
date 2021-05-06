#List Comprehension

#output = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  
        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  
        # [2, 4, 6, 8, 10]
        # [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]
        # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#Normal Method

square_list = []
for item in range(1,11):
    square_list.append(item**2)
print(square_list)

#Comprehension Method

square_list_comprehension = [item**2 for item in range(1,11)]
print(square_list_comprehension)

#Comprehension with  if condition

square_list_comprehension_condition = [item for item in range(1,11) if item%2 ==0]
print(square_list_comprehension_condition)

#Comprehension with  if else condition

new_list = [item**2 if (item%2 == 0) else -item for item in range(1,11)]
print(new_list)

#Comprehension with nested list

nested_list = [[i for i in range(1,4)] for j in range(3)]
print(nested_list)


