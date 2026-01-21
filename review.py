# #Review Python chapters 3-8
# average = float(input('Enter your average: '))
# while average < 0 or average > 100:
#     if average == -999:
#         print('Exit the Program')
#         break
#     else:
#         average = float(input('Enter your average (0-100): '))

# if average != -999:
#     if average >= 90:
#         letter_grade = 'A'
#     elif average >= 80 and average < 90:
#         letter_grade = 'B'
#     elif average >= 70 and average < 80:
#         letter_grade = 'C'
#     elif average >= 60 and average < 70:
#         letter_grade = 'D'
#     else:
#         letter_grade = 'F'
#     print(f'average = {average:.2f}\tfinal grade = {letter_grade}')

# #CONDITIONAL IF 
# hours = 55
# hourly_rate = 20.50
# pay = (hours - 40) * 1.5 * hourly_rate + 40 * hourly_rate if hours > 40 else hours * hourly_rate
# print(f'\nPay = ${pay:.1f}')

# #random number
# import random

# # random.seed(12345)
# rand_num =random.randint(1, 100)
# rand_num1 = random.randrange(1,100)

# print(f'\nRandom number generated: {rand_num}')

# #generate random character from a-z
# ch = random.randint(ord('A'), ord('Z'))
# print(f'Random character generated: {chr(ch)}')

# #str functions
# num = input('Enter a number:')
# while not num.isdigit():
#     print('Enter number only')
#     num = input('Enter a number:')

# print(f'The number entered: {num}')

# #check for vowel
# sentence = input('Enter a sentence: ')
# vowels = 'aeiouAEIOU'

# count = 0
# for ch in sentence:
#     if ch in vowels:
#         count += 1
# print(f'Number of vowels: {count}')

# vowelless = [ch for ch in sentence.lower() if ch not in vowels]
# print(f'The sentence without vowels: {vowelless}\n')
# vowelless_str = ''.join(vowelless)
# print(vowelless_str)

#global variable
# glb_num = 10
# print(f'id:{id(glb_num)}, value: {glb_num}')
# def modify_global():
#     """modify global variable"""
#     global glb_num
#     glb_num = 20
#     local = glb_num + 10
#     print(f'Inside function - id:{id(glb_num)}, value: {glb_num}, local: {local}')
# modify_global()
# print(f'Outside function - id:{id(glb_num)}, value: {glb_num}')

#unpacking arguments
# def make_sandwich(*ingredients):
#     """Make a sandwich with the given ingredients."""
#     for ingredient in ingredients:
#         print(f'Adding {ingredient} to your sandwich.')
#     print('Your sandwich is ready!\n')
# make_sandwich('ham', 'cheese', 'lettuce', 'tomato')





#prime number check
# def is_prime(num):
#     """Check if a number is prime."""
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

#check palindrome
# def is_palindrome(s):
#     """Check if a string is a palindrome."""
#     s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
#     return s == s[::-1]

# word = input("Enter a word or phrase: ")
# if is_palindrome(word):
#     print(f'"{word}" is a palindrome.')
# else:
#     print(f'"{word}" is not a palindrome.')


#list
numbers = [10,50,20,40,30]
print(f'Sum of numbers: {sum(numbers)}')
print(f'Maximum number: {max(numbers)}')
print(f'Minimum number: {min(numbers)}')
print(f'Index of max value of numbers: {numbers.index(max(numbers))}')
print(f'Index of min value of numbers: {numbers.index(min(numbers))}')
print(f'Reversed list: {list(reversed(numbers))}')