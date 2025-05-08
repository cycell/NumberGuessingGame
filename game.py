# game.py
from logic import generate_number, check_guess
from utils import get_valid_input

def main():
    number = generate_number()
    attempts = 0
    while True:
        guess = get_valid_input()
        attempts += 1
        result = check_guess(number, guess)
        print(result)
        if result == "Correct!":
            print(f"You won in {attempts} attempts!")
            break
if __name__ == "__main__":
    main()