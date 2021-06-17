#in this exercise, I implement an iterative function to check if a string is a palindrome

#function definition
#takes the user's inputted string as the function's parameter
def palindromecheck(userstr):
    #uppercase letter is not the same as its equivalent lowercase letter
    #converts the string using the .lower() method
    #to lowercase letters to compare the letters correctly
    userstr = userstr.lower()
    #find the length of the term and run the loop for that length/2
    for x in range(0, int(len(userstr)/2)):
        #check if the second half of the word matches the first half of word reversed
        #by checking if the letters are the same
        if userstr[x] == userstr[len(userstr)-x-1]:
            #if they are the same, return True
            return True
        else:
            #otherwise, return False
            return False
#store the user's string input into this variable
userstr = input("What would you like to check for being a palindrome?")
print("True means that it is a palindrome, and false means it is not.")
#passes the user's inputted string into the function as an argument
#print what the function returns
print(palindromecheck(userstr))
