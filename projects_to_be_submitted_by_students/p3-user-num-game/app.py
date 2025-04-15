import random

# GENERATE A RANDOM NUMBER BETWEEN 1 AND 100 AND ASK THE USER TO GUESS IT.....
def guess_the_number():
    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts =5
    print ('Welcome to guess the number game!')
    print('I am a thinking number between 1 and 100. You have {max_attempts} to guess it...')

# get the number from the user guess........
    while attempts < max_attempts:
         try:
              guess = int(input('Enter your guess:'))
              attempts += 1

# check if guess is correct or not........
              if guess == secret_number:
                 print(f'Congratulations! You have guessed the number in {attempts} attempts!')
                 return
              elif guess < secret_number:
                 print('Too low! choose a higher number')
              else:
                 print('Too high! choose a lower number')

# show the remaing attempts to the user........
              print (f'Attemps remaing:{max_attempts - attempts}')

         except ValueError:
               print('Invalid input! Please enter a number')
               continue

    print(f'\nGame over! The number was {secret_number}')

if __name__ =='__main__':
     while True:
         guess_the_number()
         play_again = input('Do you want to play again? (yes/no):').lower()
         if play_again == 'no':
             print('Thank you for playing! good bye!')
             break


       
                


 