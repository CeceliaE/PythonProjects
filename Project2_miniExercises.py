#Exercise 1
#function uses an if statement to check if their product is greater than 1000
#if so, returns the sum
#otherwise, returns the product
def multiplicationfunction(x, y):
    if x * y >= 1000:
        return (x + y)
    else:
        return (x * y)
#x and y are int variables
x = int(input("Please enter an integer."))
print()
y = int(input("Please enter another integer."))
print("If the product of these two integers is greater than 1000, then this is the sum. If it is less than 1000, this is the product.")
#function call with x and y variables as arguments
print(multiplicationfunction(x, y))
print()

#Exercise 2 
print("If a number on this list is divisible by 5")
#a list of numbers
listofnumbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#iterate through the list of numbers
#if the number is greater than 150, end the loop iteration
for number in listofnumbers:
    if (number > 150):
        break
    #otherwise, display all the numbers that are divisible by 5
    elif (number % 5 == 0):
        print(number)
print()

#Exercise 3
#asks users for input to store in each of two variables, rangestart and rangeend, #to create a range of numbers
rangestart = int(input("Please enter an integer as the start of your range"))
rangeend = int(input("Please enter an integer as the end of your range"))
#using a for loop, iterate through the range of numbers (inclusive)
#display all the prime numbers in the range of numbers
#prime numbers are greater than 1 and their only factors are 1 and themselves
for x in range(rangestart,rangeend+1):
    if x > 1:
        for i in range(2,x):
            if (x % i ) == 0:
                break
        else:
            print(x)
print()

#Exercise 4
#function takes in a string parameter
#and it returns the number of vowels in the string
def vowelfunction(word):
    #variable to store the count
    count = 0
    #iterate through every character in the string
    for char in word:
        #if the character is a vowel
        if char in "aeiouAEIOU":
            #increment the count by one
            count = count + 1
    #after the loop ends, return the count
    return(count)
#asks the user for string input and stores it in this variable
word = input("Please enter a word")
#calls the function with the user's string as the argument
print(vowelfunction(word))
print()

#Exercise 5
#created two lists with the following values
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#create an empty list to store elements that are common between the lists
new_list = []

#check the lengths of the lists and compare them
#if b is the longer list, iterate through all the values in a
#and if those values are also in b and not in the new list
#add those values to the new list (removes the duplicates)
if len(b) > len(a):
    for number in a:
        if number in b and number not in new_list:
            new_list.append(number)
#do the same if list a is longer than list b
if len(a) > len(b):
    for number in b:
        if number in a and number not in new_list:
            new_list.append(number)
#print the new list with the non-duplicate values between list a and list b
print(new_list)