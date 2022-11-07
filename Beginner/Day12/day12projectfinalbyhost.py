from random import randint
from art import logo

EASY_LEVEL_TERMS = 10
HARD_LEVEL_TERMS = 5
print(logo)


def check_answer(guess, answer, turns):
    """check the answer against guess. Return the number of terms remaining"""
    if guess > answer:
        print("Too low.")
        return turns - 1
    elif guess < answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}.")


def set_difficulty():
    level = input("Choose your difficulty. Type 'easy' or 'hard'.\n")
    if level == "easy":
        return EASY_LEVEL_TERMS
    else:
        return HARD_LEVEL_TERMS


def game():
    print("Welcome.\n")
    print("Guess between 1 to 100.\n")
    answer = randint(1, 100)
    print(answer)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the letter.\n")
        guess = int(input("Enter a number:\n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again!")


game()
