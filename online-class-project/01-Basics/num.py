# 04_random_numbers..........

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

import random

def main():
    for _ in range(N_NUMBERS):
      print(random.randint(MIN_VALUE,MAX_VALUE),end =' ')


if __name__ == '__main__':
    main()
    
       


