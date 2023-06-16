# Guessing number game
import random
number_of_tries = 0

logo = """ 
  ________                                __  .__                                 ___.                ._.
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________| |
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \ |
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/\|
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   __
        \/            \/     \/     \/             \/     \/       \/            \/    \/     \/       \/                                                                                                                    

 """


def guessing_game():
    global number_of_tries
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = str(
        input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    if (difficulty == 'easy'):
        number_of_tries = number_of_tries + 5
    elif (difficulty == 'hard'):
        number_of_tries = number_of_tries + 10
    else:
        print("That is not an option")
    correct_number = random.randint(1, 100)
    print(f"Psst, the correct answer is {correct_number}")
    is_playing = True
    while (is_playing):

        print(
            f"You have {number_of_tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if (guess < correct_number):
            number_of_tries = number_of_tries - 1
            print("Too low.\nGuess again")

        elif (guess > correct_number):
            number_of_tries = number_of_tries - 1
            print("Too high.\nGuess again")

        elif (guess == correct_number):
            print(f"You got it! The answer was {correct_number}")
            is_playing = False

    if (number_of_tries == 0):
        print("You've run out of guesses, you lose.")
        is_playing = False


guessing_game()
