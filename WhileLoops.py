### Part Two -- your code goes here. 
import random 
secret_number = random.randint(1, 100)
 
number = -1
while number != secret_number:
    number = int(input(" guess a number between 1 and 100:"))
    if number != secret_number:
        print("incorrect, keep guessing!")
    elif number == secret_number: 
        print("well done, you've guessed the correct number")
    
