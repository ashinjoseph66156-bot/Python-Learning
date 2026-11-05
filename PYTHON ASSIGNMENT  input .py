
import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)

# Set maximum attempts
attempts = 3

# Guessing logic
while attempts > 0:

    # Ask the user to guess the number
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check whether the guess is in the valid range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    # Reduce attempts
    attempts -= 1

    # Check the guessed number
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Too low. Try again.")

# Execute when all attempts are used
else:
    print("Better luck next time!")
# 2 user input

number = int(input("Enter the number for which you want the multiplication table: "))

# Generate multiplication table from 1 to 10
for i in range(1, 11):

    # Calculate multiplication
    result = number * i

    # Display the multiplication table
    print(number, "x", i, "=", result)
# 3 guessing logic

# Define a function to calculate BMI
def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    return bmi


# Get weight from the user
weight = float(input("Enter your weight in kg: "))

# Get height from the user
height = float(input("Enter your height in meters: "))

# Call the function
result = calculate_bmi(weight, height)

# Display the BMI
print("Your BMI is:", round(result, 2))



