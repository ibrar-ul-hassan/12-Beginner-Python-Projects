# 1. Madlibs
# 2. Guess the number (Computer)
# 3. guess the number (User)
# 4. Rock Paper Scissors
# 5. Hangman
# 6. Tic-Tac-Toe
# 7. Tic-Tac-Toe- AI
# 8. Binary Search
# 9. Minesweeper
# 10. Sudoku Solver
# 11. Photo Processing
# 12. markov Chain Composer



# # 1 Madlib
# adjective = input("Write an adjective: ")
# Your_Name = input("Tell me your name: ")
# Favourite_Animal = input("Which animal is most favourite one: ")

# madlib = f"Computer programming is very {adjective}. {Your_Name} wants to write code everyday.\
#  Stay cool and be a {Favourite_Animal}. I love you guys 5k times. Have Fun!"
 
# print(madlib)


# 2 Guess the number (Computer)
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, guess again. Too High!")
        elif guess < random_number:
            print("Sorry, guess again. Too Low!")
    print(f"Yahoo! You have guessed the right number {random_number}. Congrats")        

guess(10)