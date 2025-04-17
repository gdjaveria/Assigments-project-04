
# Welcome to the High-Low Game.........
import random

round = 5

def main():
    print('welcome to the High-Low Game!')
    print("----------------------")

score = 0 

for i in range(round):
    print(f'Round', i + 1)

    computer_number: int = random.randint(1,100)
    user_number:int = random.randint(1,100)
    print(f'user number is ' , user_number)

    choice:str = input('DO You think your number is higher or lower than the computer number? ')
    higher_correct : bool = choice == 'higher' and user_number > computer_number
    lower_correct : bool = choice == 'lower' and user_number < computer_number

    if higher_correct or lower_correct:
        print('you are correct! The computer number was', computer_number)
        score += 1
    else:
        print('you are incorect! The computer number was', computer_number)

    print('your score is', score)
    print('----------------------')

    print('Thank you for playing.......!')

if __name__ == "__main__":
    main()


    






        









