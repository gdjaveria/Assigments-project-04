def madlib_game():
    print('welocome to the madlib game')
    print('please enter the following words')

    adjective = input('enter an adjective:')
    noun= input('enter a noun:')
    verb =input('enter a verb:')
    adverb = input('enter an adverb:')
    place = input('enter a place:')

    print('\n Here is your madlib story:')
    print("--------------------------------")
    print(f'Today i went to the {place} and saw a {adjective} {noun}.')
    print(f'I saw a {noun} that {verb} {adverb} across the road.')
    print(f'Everyone around was amazed!')
    print('--------------------------------')

if __name__ == "__main__":
    madlib_game()
