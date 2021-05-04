# def is_palindrome(param):
#     reverse_string = param[::-1]
#     if reverse_string == param:
#         return True
#     return False

def is_palindrome(word):
    return word == word[::-1]

user_input = input('Enter string : ')

if is_palindrome(user_input):
    print(f'\'{user_input}\' is palindrome.')
else:
    print(f'\'{user_input}\' is not plaindrome.')