import random

# Function to play the game.......
def play_game():
    choices =["Rock","Paper","Scissors"]
    player_score = 0
    computer_score = 0

# Loop to play the game multiple times.......
while True:
    print ('Enter your choice: Rock, Paper or Scissors')
    player_choice = input('Enter your chice: (Rock, Paper, Scissors) or quit to end:').lower()

# Check if the player wants to quit the game.......
    if player_choice == 'quit':
      break
    
# input validation for the player..........
    if player_choice not in choices:
       print('Invalid choice! please try again..')
       continue

# computer make a choice 
    computer_choice = random.choice(choices)

# show the choices made by the player and the computer.........
print(f'\n you choose: {player_choice}')
print(f'\n computer choose: {computer_choice}')

#  check who wins the game..........
if player_choice == computer_choice:
    print('It is a tie!')
elif ((player_choice == 'rock' and computer_choice == 'scissors') or
      (player_choice == 'scissors' and computer_choice == 'paper') or
      (player_choice == 'paper and computer_choice == 'rock')
      ):
      
      print ('You win!')
      plyer_score += 1
      else:
      print('computer wins')
      computer_score += 1

# show the score of the player and the computer........
print(f'\n Score - you : {player_score} computer: {computer_score}')

# show the final score 
print ('\n=== Game Over ===')
print (f'Final Score - you: {player_score} computer: {computer_score}')
if player_score > computer_score:
print('Congratulations! You win!')
elif computer_score > player_score:
print('computer wins! Better luck next time!')
else:
print ('It's a tie game!)
       
if __name__ == '__main__':
print ('Welcome to Rock, Paper, Scissors Game!')
play_game()