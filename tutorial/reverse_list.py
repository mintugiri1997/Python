def reverse_list(l):
    reverse_list = []
    for i in range(len(l)):
        reverse_list.append(l.pop())
    return reverse_list

input_list = list(range(1,5))

print(reverse_list(input_list))