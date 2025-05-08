# logic.py
import random

def generate_number():
    return random.randint(1, 100)

def check_guess(number, guess):
    if guess == number:
        return "Correct!"
    elif guess < number:
        return "Too low!"
    else:
        return "Too high!"

def is_even(number):
    return number % 2 == 0