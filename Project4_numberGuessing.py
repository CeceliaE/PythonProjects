#in this project, I build a number guessing game

#import the random module
import random

#create an empty list to track the number of attempts
attempts_list = []

#function definition for the scoring aspect
def show_score():
    #if the attempts list is empty, let the user know that there
    #is no current high score
    if len(attempts_list) <= 0:
        print("There is no current high score.")
    #otherwise find the minimum number for the attempts list as the high score
    else:
        print("The current high score is {}".format(min(attempts_list)))

#function definition
#this function will get called if the user wants to play the game
#or if the user wants to play the game again
def play_game():
    #will track the number of attempts the user takes to guess the right number
    total_attempts = 0
    #variable stores a random number between 1 and 99
    value = random.randint(1, 99)
    #stores the user's guess of what that number could be
    guess = int(input("Please input a number between 1 and 99 as your guess "))
    #calls the function show score to either display the high score
    #or let the user know there is not one
    show_score()
    
    #using a while loop to check if the guessed number matches the randomly #generated number
    while yes_or_no == "Y" or yes_or_no == "y":
        #if the guess is not in the valid range
        #have the user guess a number in the valid range
        if guess < 1 or guess > 99:
            guess = int(input("Please choose a number within the range of 1-99!"))
        #if the guess is too high have the user guess a lower number
        elif guess > value:
            print("That's too high!")
            guess = int(input("Please guess lower!"))
            #increment the user's number of attempts
            total_attempts += 1
        #if the guess is too low have the user guess a higher number
        elif guess < value:
            print("That's too low!")
            guess = int(input("Please guess higher!"))
            #increment the user's number of attempts
            total_attempts += 1
        #if the guess is equal to the randomly generated number
        #let the user know they guessed correctly
        elif guess == value:
            print("That's right!")
            #increment the user's number of attempts
            total_attempts += 1
            #append the number of guesses it took the user to guess correctly
            #to the attempts list
            attempts_list.append(total_attempts)
            print("Congratulations! You took this amount of attempts to win: {}".format(total_attempts))
            
            #check if the user wants to play again and store it in this variable
            second = input("Would you like to play again? Please choose 'Y' for yes and 'N' for no.")
            #if the user responds with Y or y, play again and reset attempts count
            if second == "Y" or second == "y":
                play_game()
                total_attempts = 0
                show_score()
            #if the user responds with N or n, break out of the while loop
            #and exit the program
            elif second == "N" or second == "n":
                print("You have chosen not to play again. Thank you for playing!")
                break
                exit()
            #any other response is invalid
            #break out of the while loop and exit the program
            elif second != "Y" or second != "y" or second != "N" or second != "n":
                print("Input is invalid. Please run the game again.")
                break
                exit()

#store the user's input in this string variable          
yes_or_no = input("Do you want to play the number guessing game? Please answer Y for yes and N for no.")
#if the user does not want to play the game, the function will not get called
if yes_or_no == "N" or yes_or_no == "n":
    print("You have chosen not to play the game.")
#otherwise, call the function    
elif yes_or_no == "Y" or yes_or_no == "y":
    play_game()






