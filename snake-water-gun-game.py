import random
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSnake Water Gun Game\n\n")
choice = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}
comp = ["s", "w", "g"]
round_num = 1
comp_marks, user_marks = 0, 0
for keys, values in choice.items():
    print(f"Press {keys} to choose {values}")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tComputer Score\t\t\t", "Your Score")


def lose():
    global comp_marks
    comp_marks += 1
    print("You lost and computer won\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  1    \t\t\t\t\t0")


def tie():
    print("Tie between you and computer\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  0    \t\t\t\t\t0")


def win():
    global user_marks
    user_marks += 1
    print("You won and computer lost\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  0    \t\t\t\t\t1")


def pr_choice():
    print(f"You have chosen {choice[user_choice]}")
    print(f"Computer has chosen {choice[comp_choice]}")


while round_num <= 10:
    print(f"Round No. {round_num}")
    user_choice = input("Enter your choice:\n")
    comp_choice = random.choice(comp)
    if user_choice == "s" or user_choice == "w" or user_choice == "g":
        if user_choice == comp_choice:
            pr_choice()
            tie()
        elif user_choice == "s" and comp_choice == "w":
            pr_choice()
            win()
        elif user_choice == "w" and comp_choice == "s":
            pr_choice()
            lose()
        elif user_choice == "s" and comp_choice == "g":
            pr_choice()
            lose()
        elif user_choice == "g" and comp_choice == "s":
            pr_choice()
            win()
        elif user_choice == "w" and comp_choice == "g":
            pr_choice()
            win()
        elif user_choice == "g" and comp_choice == "w":
            pr_choice()
            lose()
    else:
        print("Invalid Input!")
    round_num += 1
print(f"Your total marks = {user_marks}")
print(f"Computer's total marks = {comp_marks}")
if user_marks > comp_marks:
    print("Well Done! You have won the match")
elif user_marks == comp_marks:
    print("Tie between you and computer")
else:
    print("Computer has won the match. Better Luck Next Time!")
