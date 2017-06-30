import random  # Import the random module

guessesTaken = 0  # Assign 0 to the variable guessesTaken

print('Hello! What is your name?')  # Print out to the console: 'Hello! What is your name?'
myName = input()  # Assign a string from the input(user input) to the variable myName

number = random.randint(1, 20)  # Assign a random integer between 1 and 20 to the variable number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Print out to the console: 'Well, ..., I am thinking of a number between 1 and 20.' and replace ... with value of the myName variable.

while guessesTaken < 6:  # Looping while the variable guessesTaken is less than 6, so maximum 5
    print('Take a guess.')  # Print out to the console: 'Take a guess.'
    guess = input()  # Assign a string from the input(user input) to the variable guess
    guess = int(guess)  # Cast the value of the variable guess to and integer. This should be inside a try-except block, cuz if guess isn't a number it drops an error.

    guessesTaken += 1  # Assing guessesTaken with a new number, this number is equal to guessesTaken + 1

    if guess < number:  # Check if the value of the guess (variable) is lower than the value of the thought number(value of the variable number)
        print('Your guess is too low.')  # Print out to the console: 'Your guess is too low.'

    if guess > number:  # Check if the value of the guess (variable) is higher than the value of the thought number(value of the variable number)
        print('Your guess is too high.')  # Print out to the console: 'Your guess is too high.'

    if guess == number:  # Check if the value of the guess (variable) is equal to the value of the thought number(value of the variable number)
        break  # Exit/break/return from the while loop

if guess == number:  # Check if the value of guess variable is equal to the value of number variable
    guessesTaken = str(guessesTaken)  # Cast the guessesTaken to string. Assign a new value to guessesTaken, which is equal to the string casted guessesTaken
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Print out tot he console: 'Good job, ..! You guessed my number in ... guesses!', replacing .. with the value of myName variable , and replacing ... with the value of the guessesTaken variable

if guess != number:  # Check if the value of guess variable is not equal to the value of number variable
    number = str(number)  # Cast the number variable to string. Assign a new value to number, which is equal to the string casted number
    print('Nope. The number I was thinking of was ' + number)  # Print out to the console: 'Nope. The number I was thinking of was ...', replacing ... with the value of number variable
