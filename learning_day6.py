#while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# password = ""
# while password != "claude1234":
#     password = input("Please enter a password: ")
# print("Access granted")

#break continue keywords

# for i in range(1,25):
#     print(i)
#     if i == 10:
#         break #to stop loop

# for i in range(1,25):
#     if i == 10:
#         continue #to skip current iteration ie 10
#     print(i)

#functions - is a block of code 
# def sum_of_n_number(number):
#     total_sum = 0
#     for i in range((number+1)):
#         total_sum += i
#     print(total_sum)
   
# sum_of_n_number(10)

# function to return a square of a number
# def square_num(number):
#     return number**2
# userInput = int(input("please enter a number: "))
# print(square_num(3))

# print times table with a function
# def times_table(number):
#     timesTableList = []
#     for i in range(1,11):
#         timesTableList.append(number * i)
#     return timesTableList

# userInput = int(input("Please enter a number: "))
# print(times_table(number=userInput))

# find a number if number is even or odd (print)
# def is_even_or_odd(number):
#     isEven = type(number / 2)
#     if isEven == 'int':
#         return 'even'
#     else:
#         return 'odd'
#     # if number%2 == 0:
#     #     return 'even'
#     # else:
#     #     return 'odd'
userInput2 = int(input("Please enter a number: "))
isEven = type(userInput2 / 2)
print(isEven)
# print(is_even_or_odd(number=userInput2))
