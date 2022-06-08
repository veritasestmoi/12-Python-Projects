# guess the number  
import random

def guess(x):
    random_number = random.randint(1,x) #return between 1 and x (both included)
    guess = 0
    counter = 0
    while guess != random_number:
        guess = int(input(f'Enter a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry. Pick a bigger number')
            counter+= 1
        elif guess > random_number:
            print('Sorry. Pick a smaller number')
            counter+= 1
            
    print(f'You did it! The answer is {x} \nYou took {counter} tries to guess it!\n\n')
    
        
guess(10) # calling the def 