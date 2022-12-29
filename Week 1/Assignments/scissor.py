import random

score=0
for i in range(5):
    user_move=int(input('Enter your choice: 0 for scissors, 1 for paper, 2 for rock?'))
    choice=["scissors","paper","rock"]
    num = random.randint(0,2)

    if user_move==num:
        print(f"Both you and computer selected {choice[num]}. Its a tie.\n")

    elif user_move==0:
        if num==1:
            print(f"you chose {choice[user_move]} and computer chose {choice[num]}")
            print("you won\n")
            score += 1
        else:
            print(f"you chose {choice[user_move]} and computer chose {choice[num]}")
            print("you lost\n")

    elif user_move==1:
        if num==2:
            print(f"you chose {choice[user_move]} and computer chose {choice[num]}")
            print("you won\n")
            score += 1
        else:
            print(f"you chose {choice[user_move]} and computer chose {choice[num]}")
            print("you lost\n")

    elif user_move==2:
        if num==0:
            print(f"you chose {choice[user_move]} and computer chose {choice[num]}")
            print("you won\n")
            score += 1
        else:
            print(f"you chose {choice[user_move]} and computer chose {choice[num]}")
            print("you lost\n")

    else:
        print("please select a valid choice.\n")
    print(f"you have {4-i} tries left.\n\n")

print(f"You got a total score of {score}")