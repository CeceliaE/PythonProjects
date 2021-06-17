#in this project, I build a rock, paper, scissors game

#import the random module
import random

#function definition
#this function will get called if the user wants to play the game
#or if the user wants to play the game again
def play_game():
    while yes_or_no == "y":
        #if yes, then it will ask the user to choose an option
        user_choice = input("Please choose rock, paper, or scissors")
        choices = ["rock", "paper", "scissors"]
        #if the user's choice is not a valid option from the list,
        #ask for user input again
        if user_choice not in choices:
            print("Please choose one of the options.")
            user_choice = input("Please choose rock, paper, or scissors")
        
        #using the choice() method to randomly select 
        #the computer's choice from the list choices
        #and store it in this variable
        computer_choice = random.choice(choices)
        
        #let the player know what their choice and the computer's choice were
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        
        #compare the user's choice and the computer's choice
        #use a series of if and elif statements to go through every
        #possible combination and print the corresponding won/lost statement
        if user_choice == computer_choice:
            print("This game has ended with a tie.")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You have won.")
        elif user_choice == "rock" and computer_choice == "paper":
            print("You have lost.")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You have won.")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You have won.")
        elif user_choice == "scissors" and computer_choice == "rock":
            print("You have lost.")
        elif user_choice == "paper" and computer_choice == "scissors":
            print("You have lost.")
        
        #ask the user if they want to play the game again 
        #and store it in this variable
        play_again = input("Would you like to play again? Please select yes or no.")
        #if the user wants to play game, call the function again
        if play_again == "yes":
            play_game()
        #otherwise, exit the program
        elif play_again == "no":
            exit()

#store the user's input in this string variable
yes_or_no = input("Do you want to play the rock paper scissors game? Please answer Y for yes and N for no.")
#if the user does not want to play the game, the function will not get called
if yes_or_no == "N" or yes_or_no == "n":
    print("You have chosen not to play the game.")
#otherwise, call the function
elif yes_or_no == "Y" or yes_or_no == "y":
    play_game()
#if the user input's in anything other than Y, y, N, or n
#ask the user to input in one of the valid options
else:
    print("Please choose a valid option.")
    yes_or_no = input("Do you want to play the rock paper scissors game? Please answer Y for yes and N for no.")
