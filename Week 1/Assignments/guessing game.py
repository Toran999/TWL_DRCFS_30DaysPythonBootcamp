import random

num = random.randint(1,10)
t=5
for i in range(t):
    guess = int(input("Enter your guess here: "))
    if guess > 10 or guess < 1:
        print("Guess a number between 1 and 10.")
    else:
        if guess == num:
            print("*"*50)
            print(f"yay! you got the correct guess in {i+1} tries.")
            print("*"*50)
            break
        elif guess > num:
            print("*"*50)
            print("your guess is larger")
            print("*"*50)
        else:
            print("*"*50)
            print("your guess is smaller")
            print("*"*50)  

        if i==t-1:
            print(f"You lost....{num} was the answer.")      