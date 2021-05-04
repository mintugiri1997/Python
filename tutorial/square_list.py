def square_list(l):
    square_list = []
    for i in l:
        square_list.append(i**2)
    return square_list

input_list = list(range(1,11))

print(square_list(input_list))