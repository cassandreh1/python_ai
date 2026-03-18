#conditional statement
#pass is used to ignore empty if blocks 

# st = 'red'
# st = input("Please enter a signal color : ") 

# if st == 'grenn':
#     print("Please Stop here")
# elif st == 'yellow':
#     print("please be ready")
# else:
#     print("GO from here")

##Loop

# types of loops: for, while, do while

# for i in range(1,100):
#     print("Welcome to all of you at techie solution")

#print a table in a for loop return in list from 1 - 10

userInput = input("Please enter a number: ")
intFormat = int(userInput)
timesTableList = []

for i in range(1,11):
    timesTableList.append(intFormat * i)

print(timesTableList)


#calculate N natural number sum
userInput2 = input("Please enter a number: ")
intFormat2 = int(userInput2)
sum = 0

for i in range((intFormat2 + 1)):
    sum += i

print(sum)