
import random

#list of words........
words=['apple','banana','cherry','date','grape','kiwi','mango','orange','raspberry','strawberry']

word = random.choice(words)
guessed_letters =[]
attempts = 6

print ('welcome to the game of hangman!')
print(f'The word has {len(word)} letters you have {attempts} attempts to guees it')
print("_" * len(word))

# intialize the display word.....
display_word = "_" * len(word)

while attempts > 0:
    guess= input("\nGuess a letters:").lower()

    if len(guess) !=1 or not guess.isalpha():
        print('please write a single letter')
        continue
    if guess in guessed_letters:
        print('you have already guessed that letter and choose another letter')
        continue
    guessed_letters.append(guess)

#check if the letter is in the word........
    if guess in word:
        print('you correctly guessed a letter')
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(display_word)
    else:
        attempts -=1
        print(f'wrong guess! you have {attempts} attempts left')
        print(display_word)

#check if the word is guessed.......
    if '_' not in display_word:
        print('\n Congratulations you have guessed the word:', word)
        break
   
# only show game over message if the word is not guessed
if '_' in display_word:
    print('\n Game over! The word was:',{word})

