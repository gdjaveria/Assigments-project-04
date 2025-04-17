# 03_guess_my_number............

import random

def main():
    secret_number = random.randint(1, 100)
    print('Welcome to the Guess My Number game!')
    print('I have selected a number between 1 and 100. Can you guess it?')

    guess = int(input('Enter your guess: '))

    while guess != secret_number:
        if guess < secret_number:
            print('Too low! Try again.')
        else:
            print('Too high! Try again.')
        guess = int(input('Enter your guess: '))

    print('Congratulations! You guessed the number!')

if __name__ == '__main__':
    main()
    
       


