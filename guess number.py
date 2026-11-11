import random
target = random.randint(1, 50)
guess = 0
attempts = 0
while guess != target:
    guess=int(input("Guess the number (1-50):"))
    attempts +=1
    if guess<target:
        print("Too Low!")
    elif guess>target:
        print("Too High!")
    else:
        print("Correct!")
print(f"You guessed it in {attempts} attempts.")
