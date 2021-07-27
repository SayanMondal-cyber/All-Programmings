import os
import datetime
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHealth Management System")
clients = {
    "1": "Sayan",
    '2': "Sanjoy"
}
client_log = {
    "1": "add",
    "2": "retrieve"
}
log_choice = {
    "1": "exercise",
    "2": "food"
}


def getdate():
    return str(datetime.datetime.now())


for keys, items in clients.items():
    print("Press", keys, "for", items)

name = input()
if name == "1":
    for keys_log, items_log in client_log.items():
        print("Press", keys_log, "to", items_log)
    choice = input()
    if choice == "1":
        for keys_ex_di, values_ex_di in log_choice.items():
            print("Press", keys_ex_di, "to add", values_ex_di, "items")
        log_items_choice = input()
        if log_items_choice == "1":
            print("What do you want to add in exercise?")
            ex = input()
            if os.path.isfile('sayan-exercise.txt'):
                with open("sayan-exercise.txt", 'a') as op:
                    op.write("[" + getdate() + "]" + ex + "\n")
            else:
                with open("sayan-exercise.txt", 'x') as op:
                    op.write("[" + getdate() + "]" + ex + "\n")
            while True:
                print("Do you want to add any other exercise item? [Yes/No]")
                user_choice = input().capitalize()
                if user_choice == "Yes":
                    ex = input()
                    with open("sayan-exercise.txt", 'a') as op:
                        op.write("[" + getdate() + "]" + ex + "\n")
                elif user_choice == "No":
                    break
                else:
                    print("Invalid Choice")
                    break
            print("Exercise item is added successfully")
        elif log_items_choice == "2":
            print("What do you want to add in diet?")
            diet = input()
            if os.path.isfile('sayan-diet.txt'):
                with open("sayan-diet.txt", 'a') as op:
                    op.write("[" + getdate() + "]" + diet + "\n")
            else:
                with open("sayan-diet.txt", 'x') as op:
                    op.write("[" + getdate() + "]" + diet + "\n")
            while True:
                print("Do you want to add any other food item? [Yes/No]")
                user_choice = input().capitalize()
                if user_choice == "Yes":
                    diet = input()
                    with open("sayan-diet.txt", 'a') as op:
                        op.write("[" + getdate() + "]" + diet + "\n")
                elif user_choice == "No":
                    break
                else:
                    print("Invalid Choice")
                    break
            print("Food item is added successfully")
        else:
            print("Invalid input!!")
    elif choice == "2":
        for keys_ex_di, values_ex_di in log_choice.items():
            print("Press", keys_ex_di, "to retrieve", values_ex_di, "items")
        re_choice = input()
        if re_choice == "1":
            if os.path.isfile('sayan-exercise.txt'):
                with open("sayan-exercise.txt") as ret:
                    content = ret.read()
                    print(content)
            else:
                print("No exercise item exists yet!")
        elif re_choice == "2":
            if os.path.isfile('sayan-diet.txt'):
                with open("sayan-diet.txt") as ret:
                    content = ret.read()
                    print(content)
            else:
                print("No food item exists yet!")
    else:
        print("Invalid input!!")
elif name == "2":
    for keys_log, items_log in client_log.items():
        print("Press", keys_log, "to", items_log)
    choice = input()
    if choice == "1":
        for keys_ex_di, values_ex_di in log_choice.items():
            print("Press", keys_ex_di, "to add", values_ex_di, "items")
        log_items_choice = input()
        if log_items_choice == "1":
            print("What do you want to add in exercise?")
            ex = input()
            if os.path.isfile('sanjoy-exercise.txt'):
                with open("sanjoy-exercise.txt", 'a') as op:
                    op.write("[" + getdate() + "]" + ex + "\n")
            else:
                with open("sanjoy-exercise.txt", 'x') as op:
                    op.write("[" + getdate() + "]" + ex + "\n")
            while True:
                print("Do you want to add any other exercise item? [Yes/No]")
                user_choice = input.capitalize()
                if user_choice == "Yes":
                    ex = input()
                    with open("sanjoy-exercise.txt", 'a') as op:
                        op.write("[" + getdate() + "]" + ex + "\n")
                elif user_choice == "No":
                    break
                else:
                    print("Invalid Choice")
                    break
            print("Exercise item is added successfully")
        elif log_items_choice == "2":
            print("What do you want to add in diet?")
            diet = input()
            if os.path.isfile('sanjoy-diet.txt'):
                with open("sanjoy-diet.txt", 'a') as op:
                    op.write("[" + getdate() + "]" + diet + "\n")
            else:
                with open("sanjoy-diet.txt", 'x') as op:
                    op.write("[" + getdate() + "]" + diet + "\n")
            while True:
                print("Do you want to add any other food item? [Yes/No]")
                user_choice = input().capitalize()
                if user_choice == "Yes":
                    diet = input()
                    with open("sanjoy-diet.txt", 'a') as op:
                        op.write("[" + getdate() + "]" + diet + "\n")
                elif user_choice == "No":
                    break
                else:
                    print("Invalid Choice")
            print("Food item is added successfully")
        else:
            print("Invalid input!!")
    elif choice == "2":
        for keys_ex_di, values_ex_di in log_choice.items():
            print("Press", keys_ex_di, "to retrieve", values_ex_di, "items")
        re_choice = input()
        if re_choice == "1":
            if os.path.isfile('sanjoy-exercise.txt'):
                with open("sanjoy-exercise.txt") as ret:
                    content = ret.read()
                    print(content)
            else:
                print("No exercise item exists yet!")
        elif re_choice == "2":
            if os.path.isfile('sanjoy-diet.txt'):
                with open("sanjoy-diet.txt") as ret:
                    content = ret.read()
                    print(content)
            else:
                print("No food item exists yet!")
    else:
        print("Invalid input!!")
else:
    print("Invalid input!!")
