# This is a blacjack game
import random
# Ask user if they want to play
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []
user_score = 0
cpu_score = 0


def resetDeck():
    global your_cards
    global computer_cards
    your_cards.clear()
    computer_cards.clear()


def scoreCheck():
    global user_score
    global cpu_score

    if cpu_score == user_score:
        print(
            f"    Your final hand: {your_cards}, final score: {user_score}")
        print(
            f"      Computer's final hand: {computer_cards}, final score: {cpu_score}")
        print("It's a draw!")
        is_playing = False
        return

    elif user_score > cpu_score and user_score <= 21:
        print(
            f"    Your final hand: {your_cards}, final score: {user_score}")
        print(
            f"      Computer's final hand: {computer_cards}, final score: {cpu_score}")
        print("You've beat the computer, you've won!")
        is_playing = False
        return

    elif cpu_score > user_score and cpu_score <= 21:
        print(
            f"    Your final hand: {your_cards}, final score: {user_score}")
        print(
            f"      Computer's final hand: {computer_cards}, final score: {cpu_score}")
        print("CPU has better hand, you lose!")
        is_playing = False
        return

    elif user_score > 21:
        print(
            f"    Your final hand: {your_cards}, final score: {user_score}")
        print(
            f"      Computer's final hand: {computer_cards}, final score: {cpu_score}")
        print("You went over. You lose")
        is_playing = False
        return

    elif user_score == 21:
        print(f"    Your cards: {your_cards}, current score: {user_score}")
        print(
            f"      Computer's cards: {computer_cards}, computer score: {cpu_score}")
        print("Blackjack!")
        is_playing = False
        return


def playBlackjack():
    global user_score
    global cpu_score
    playing = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
    if (playing == 'y'):
        is_playing = True
    elif (playing == 'n'):
        is_playing = False

    while is_playing == True:
        my_score = 0
        computer_score = 0
        if (user_score > 21):
            print(
                f"    Your final hand: {your_cards}, final score: {user_score}")
            print(
                f"      Computer's final hand: {computer_cards}, final score: {cpu_score}")
            print("You went over. You lose")
            is_playing = False
            return

        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        for i in your_cards:
            user_score += i
        for i in computer_cards:
            cpu_score += i
        print(f"    Your cards: {your_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        while cpu_score < 17 and user_score <= 21:
            cpu_score = 0
            computer_cards.append(random.choice(cards))
            for i in computer_cards:
                cpu_score += i

        while user_score < 21 and is_playing == True:
            answer = input(
                "Type 'y' for another card or 'n' to pass: ").lower()
            if(answer == 'y'):
                user_score = 0
                your_cards.append(random.choice(cards))
                for i in your_cards:
                    user_score += i
                print(
                    f"    Your cards: {your_cards}, current score: {user_score}")
                print(f"    Computer's first card: {computer_cards[0]}")
            elif (answer == 'n'):
                scoreCheck()
                is_playing = False


playBlackjack()
resetDeck()
prompt = input(
    "Would you like to play again? Type 'y' for yes 'n' for no: ").lower()
if (prompt == 'y'):
    play_again = True
    playBlackjack()
elif(prompt == 'n'):
    play_again = False
    print("Thanks for playing!")

while(play_again == True):
    resetDeck()
    playBlackjack()
    print(prompt)
