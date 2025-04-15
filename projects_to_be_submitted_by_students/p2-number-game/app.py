def computer_guess_number():
    print('Think of a number between 1 and 100.')
    print('After each guess, tell me if it is:')
    print("'h' for too high ")
    print("'l' for too low ")
    print("'c' for correct ")

    low =1
    high=100
    attemps=0

# use a while loop to keep guessing
    while True:
     guess = (low + high) //2
     attemps += 1

# guess the user feedback
     response = input(f'\nIS your number {guess}? (h/l/c): ').lower()

     if response == 'c':
        print(f'\nI got it! your number is {guess}!...')
        print(f'It took me {attemps} attemps.')
        break
     elif response == 'h':
        high = guess = -1
     elif response == 'l':
        low = guess +1
     else:
       print("Please enter 'h','l', or 'c' only...")
       attemps -= 1

# check if the range is valid
     if low > high:
       print('Hey! you have made a mistake somewhere...')
       print('The range of number is not valid.')
       break

# call the function
if __name__ == '__main__':
   while True:
      computer_guess_number()
      play_again = input('\n Would you like to play again? (yes/No):').lower()
      if play_again != 'yes':
         print('Thanks for playing!☺')
         break
         

