import random
import string

def generate_password(length=12, use_digits = True, use_special = True):
    letters =string.ascii_letters
    digits =string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_+;?' if use_special else ''

# Combine all characters based on user preferences
    all_charcters = letters + digits + special_chars 

# make sure password contains at least one character from each selected category
    password = [ 
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),]

    if use_digits:
            password.append(random.choice(digits))
    if use_special:
            password.append(random.choice(special_chars))

# fill the rest of the password length with random choices from all characters
    while len(password) < length:
            password.append(random.choice(all_charcters))

    random.shuffle(password)
    return ''.join(password)

# user input for password length and character types
length = int(input('Enter the password length(like 12):'))
use_digits = input('Include digits?(y/n):').strip().lower() == 'y'
use_special = input('Inculde special characters? (y/n):').strip().lower() =='y'

# Generate and display password
password = generate_password(length, use_digits, use_special)
print(f'Generated password:{password}')





   