# List Practice.............

#  Create a list of fruits and print it..........
my_list =['kiwi','banana','apple','orange','grape','mango']

# return the element at the specified index.
def get_elemt(my_list,index):
    if 0 <= index < len(my_list):
        return f'The elemnt at index {index} is {my_list[index]}'
    return 'Index out of range'

# modifying the element at the specified index...........
def modify_elemnt(my_list, index,new_value):
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value # modifying list element
        return f'Element at index {index} change from {old_value} to {new_value}'
    return 'Index out of range'

# return a new list that contains the elements from the specified start index to the end index (exclusive)........
def slice_list(my_list, start, end):
    if 0 <= start < len(my_list) and 0 <= end < len(my_list):
        return f'sliced list: {my_list[start:end]}'
    return('Invalid slice indices')

# Create a game that allows the user to interact with the list.............
def list_game():
    print('Welcome to the list game!')
    my_list = ['kiwi', 'banana', 'apple', 'orange', 'grape', 'mango']

    while True:
        print('\nCurrent list:', my_list)
        print('Choose an option:')
        print('1. Get element at index')
        print('2. Modify element at index')
        print('3. Slice list')
        print('4. Exit')
        choice = input('Enter your choice (1-4): ')
        

        if choice == '1':
            index = int(input('Enter index of the element you want to get: '))
            print(get_elemt(my_list , index))
        elif choice == '2':
            index = int(input('Enter index of element you want to modify:' ))
            new_value = input('Enter new value: ')
            print(modify_elemnt(my_list , index , new_value))
        elif choice == '3':
            start = int(input('Enter start index for slicing: '))
            end = int(input('Enter end index for slicing: '))
            print(slice_list(my_list , start , end))
        elif choice == '4':
           print('Exiting the game. Goodbye!')
           print('Thank you for playing!')
           break
        else:
           print('Invalid choice. Please try again.')

if __name__ == '__main__':
    list_game()
    



        
       




  




    

   
   