# Planetary Weight Calculator.........

def main():
    print("Welcome to the Planetary Weight Calculator!")
    print('------------------------------------')

weight_of_earth =float(input('Enter your weight on Earth '))

gravity_ratio ={
    'Mercury': 0.38,
    'Venus': 0.91,
    'Earth': 1.00,
    'Mars': 0.38,
    'Jupiter': 2.34,
    'Saturn': 1.06,
    'Uranus': 0.92,
    'Neptune': 1.19
}
# Calculate the weight on the selected planet..........
print('Select a planet to calculate your weight:')
for plannet in gravity_ratio.keys():
    print(plannet)

# Get the user's choice of planet
plannet_choice = input('Enter the name of the planet: ').title()

# Check if the planet is in the dictionary and calculate the weight............
if plannet_choice in gravity_ratio:
    weight_of_earth = weight_of_earth * gravity_ratio[plannet_choice]
    print(f'your weight on {plannet_choice} is: {weight_of_earth:.2f} kg')
else:
    print('Invalid plannet name enterd!')

if __name__ == "__main__":
    main()






