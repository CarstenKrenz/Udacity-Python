import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def bad_input():
    print_pause("Sorry, i do not understand.")

def intro(items,monster):
    print_pause("You are on a wide field.")
    print_pause("Your mission, remember, is to migrate north to King Edward.")
    print_pause("For that, you must cross the bridge to the north.")
    print_pause("In the south, a mill faces the sun.")
    print_pause("In the east is a cave.")

def start_choice(items,monster):
    print_pause("Where would you like to go now?")
    choice = input("1. Bridge\n"
                   "2. Mill\n"
                   "3. Cave\n")
    if choice == "1":
        bridge(items,monster)
    elif choice == "2":
        mill(items,monster)
    elif choice == "3":
        cave(items,monster)

def win_game(items,monster):
    print_pause("Congratulations, the road to King Edward is now open.")
    print_pause("Would you like to play again?")
    choice = input("1. Yes\n"
                   "2. No\n")
    if choice == "1":
        play_game()
    elif choice == "2":
        print_pause("Goodbye")
    else:
        bad_input()
        win_game(items,monster)

def loose_game(items,monster):
    print_pause("Would you like to play again?")
    choice = input("1. Yes\n"
                   "2. No\n")
    if choice == "1":
        play_game()
    elif choice == "2":
        print_pause("Goodbye")
    else:
        bad_input()
        loose_game(items,monster)

def bridge(items,monster):
    print_pause("You're standing in front of the bridge.")
    print_pause("A " + monster + " is guarding the bridge in front of you.")
    if "Troll" in monster:
        bridge_troll(items,monster)


def bridge_troll(items,monster):
    print_pause("The troll looks at you grimly.")
    print_pause("He speaks to you in his deep voice:")
    print_pause("NO TRANSIT WITHOUT GOLD, HOOMAN")
    print_pause("Would you like to...")
    choice = input("1. Pay the Troll\n"
                   "2. Fight the Troll\n")
    if choice == "1":
        if "Gold" in items:
            print_pause("You pay the Troll.")
            win_game(items,monster)
        elif "Sword" in items:
            print_pause("You draw your magic sword.\n")
            print_pause("When the troll sees the sword, his face is filled with pure fear.\n")
            print_pause("Instead of attacking you, he runs away.\n")
            win_game(items,monster)
        else:
            loose_game(items,monster)

    if choice == "2":
        mill_bedroom(items,monster)

def mill(items,monster):
    print_pause("You enter the mill.")
    print_pause("There's nothing exciting to discover here.")
    print_pause("A door leads into the bedroom.")
    print_pause("Would you like to...")
    choice = input("1. Leave the mill\n"
                   "2. Enter the bedroom\n")
    if choice == "1":
        print_pause("You leave the mill and go back to the field.")
        start_choice(items,monster)
    if choice == "2":
        mill_bedroom(items,monster)


def mill_bedroom(items,monster):
    print_pause("The bedroom looks tidy.")
    if "Gold" in items:
        print_pause("There is nothing special to discover here")
    else:
        print_pause("There's a sack of gold next to the big bed on the nightstand.\n")
        print_pause("Would you like to...")
        choice = input("1. Take the Gold\n"
                       "2. Leave the gold and leave the mill\n")
    if choice == "1":
        print_pause("You take the gold with you and leave the mill.\n")
        items.append("Gold")
        start_choice(items,monster)
    elif choice == "2":
        print_pause("You leave the gold and leave the mill back to the field.\n")
        start_choice(items,monster)
    else:
        bad_input()
        mill_bedroom(items,monster)


def cave(items,monster):
    print_pause("You're standing in front of the bridge.")
    print_pause("A +monster+ is guarding the bridge in front of you.")


def play_game():
    items = []
    monster_pool = ["Troll", "Witch"]
    monster = random.choice(monster_pool)
    print_pause(monster)
    intro(items,monster)
    start_choice(items,monster)

play_game()



# def intro(items,monster):
#     print_pause("You have just arrived at your new job!")
#     print_pause("You are in the elevator.")

# def first_floor(items,monster):
#     print_pause("You push the button for the first floor.")
#     print_pause("After a few moments, you find "
#                 "yourself in the lobby.")
#     if "ID Card" in items,monster:
#         print_pause("The clerk greets you, but she has already given you your ID card,\n"
#                     "so there is nothing more to do here now.")
#         ride_elevator(items,monster)
#     else:
#         print_pause("The clerk greets you and gives you your ID card.")
#         items,monster.append("ID Card")
#         ride_elevator(items,monster)

# def second_floor(items,monster):
#     print_pause("You push the button for the second floor.")
#     print_pause("After a few moments, you find yourself "
#                 "in the human resources department.")
#     if "Handbook" in items,monster:
#         print_pause("The HR folks are busy at their desks.\n"
#                     "There doesn't seem to be much to do here.")
#         ride_elevator(items,monster)
#     elif "ID Card" in items,monster:
#         print_pause("The head of HR greets you.")
#         print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
#         items,monster.append("Handbook")
#         ride_elevator(items,monster)
#     else:
#         print_pause("The head of HR greets you.")
#         print_pause("He has something for you, but says he can't\n"
#                     "give it to you until you go get your ID card.")
#         ride_elevator(items,monster)

# def third_floor(items,monster):
#     print_pause("You push the button for the third floor.")
#     print_pause("After a few moments, you find yourself "
#                 "in the engineering department.")
#     if "ID Card" in items,monster:
#         print_pause("You use your ID card to open the door.")
#         if "Handbook" in items,monster:
#             print_pause("Fortunately, you got that from HR!" 
#                         "Congratulatons! You are ready to start your\n"
#                         "new job as vice president of engineering!")
#         else:
#             print_pause("Your program manager greets you and tells you\n"
#                         "that you need to have a copy of the\n"
#                         "employee handbook in order to start work.")
#             ride_elevator(items,monster)
#     else:
#         print_pause("Unfortunately, the door is locked and you can't get in.")
#         print_pause("It looks like you need some kind of key card to open the door.\n"
#                     "You head back to the elevator.")
#         ride_elevator(items,monster)

# def ride_elevator(items,monster):
#     print_pause("Please enter the number for the "
#                 "floor you would like to visit:")
#     floor = input("1. Lobby\n"
#                   "2. Human resources\n"
#                   "3. Engineering department\n")
#     if floor == '1':
#         first_floor(items,monster)
#     elif floor == '2':
#         second_floor(items,monster)
#     elif floor == '3':
#         third_floor(items,monster)


# def play_game():
#     items,monster = []
#     intro(items,monster)
#     ride_elevator(items,monster)

# play_game()