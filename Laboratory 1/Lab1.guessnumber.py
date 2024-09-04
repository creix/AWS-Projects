import random

r = random.randint(0, 20)
while True:
    try:
        guess = int(input("Enter the guessed number:"))
        if(guess > r):
            print("too high")
        elif(guess < r):
            print("too low")
        else:
            break

    except ValueError:
        print("input numbers please")
    
print("You guessed correctly")