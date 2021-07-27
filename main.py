import random

number = random.randrange(1, 100, 1)
n_guesses = 10
print("You have", n_guesses, "guesses")
user_num = input("Enter a number between 1 and 100:\n")
if user_num.isnumeric():
    user_num = int(user_num)
    if 1 <= user_num <= 100:
        while n_guesses > 0:
            if user_num > number:
                print("Lower number please!")
                n_guesses -= 1
                print("You have", n_guesses, "guesses left")
                user_num = int(input())
                if 1 <= user_num <= 100:
                    continue
                else:
                    print("Please enter a number between 1 and 100")
                    break
            elif user_num < number:
                print("Higher number please!")
                n_guesses -= 1
                print("You have", n_guesses, "guesses left")
                user_num = int(input())
                if 1 <= user_num <= 100:
                    continue
                else:
                    print("Please enter a number between 1 and 100")
                    break
            else:
                print("Congrats! You have guessed the right number in", 10-(n_guesses-1), "guesses")
                break
        if n_guesses == 0:
            print("Game Over!")
    else:
        print("Please enter a number between 1 and 100")
else:
    print("Invalid input!")
