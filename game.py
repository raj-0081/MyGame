import random
secret = random.randint(1, 20)
attempts = 5
print("Guess a number between 1 and 20")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Correct! You won!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("You lost")

print("Game over")
print("The secret number was", secret)
print("Thanks for playing!")