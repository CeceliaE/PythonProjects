#in this exercise, I implement the Fibonacci Sequence iteratively. 

#storing user's input in this variable. casting to an int
nterm = int(input("How many terms do you want of the Fibonacci sequence?"))
#n1 and n2 are the first and second terms of the sequence
n1 = 0
n2 = 1
iter = 0
#if the user input is negative, asks the user to enter a positive interger
#because the number of terms needs in the Fibonacci Sequence is positive
if nterm <= 0:
    print("Please input a positive integer.")
#if the user only wants the first term, print the value of n1
elif nterm == 1:
    print("This is your Fibonacci sequence.")
    print(n1)
#otherwise, enter the while loop
else:
    print("This is your Fibonacci sequence.")
    #end the while loop once the number of iterations reaches the number
    #of terms the user wants the Fibonacci Sequence for
    while iter < nterm:
        #calculate the next term in sequence by adding the previous 2 terms
        next = n1 + n2
        #print of the terms in order
        print(n1)
        #update the values of n1 and n2
        n1 = n2
        n2 = next
        #update the iteration to the next
        iter += 1