import time
import random


def print_pause(message_to_print):
    print (message_to_print)
    time.sleep(1)


def intro(items, monster):
    print_pause('You are on a wide field.')
    print_pause('Your mission, remember, is to migrate north to King Edward.')
    print_pause('For that, you must cross the bridge to the north.')
    print_pause('In the south, a mill faces the sun.')
    print_pause('In the east is a cave.')


def start_choice(items, monster):
    print_pause('Where would you like to go now?')
    choice = input('''1. Bridge
2. Mill
3. Cave
''')

    if choice == '1':
        bridge(items, monster)
    elif choice == '2':
        mill(items, monster)
    elif choice == '3':
        cave(items, monster)
    else:
        bad_input()
        start_choice(items, monster)


def bad_input():
    print_pause('Sorry, i do not understand.')


def win_game(items, monster):
    print_pause('Congratulations, the road to King Edward is now open.')
    print_pause('Would you like to play again?')
    choice = input('''1. Yes
2. No
''')
    if choice == '1':
        play_game()
    elif choice == '2':
        print_pause('Goodbye')
    else:
        bad_input()
        win_game(items, monster)


def loose_game(items, monster):
    print_pause('Would you like to play again?')
    choice = input('''1. Yes
2. No
''')
    if choice == '1':
        play_game()
    elif choice == '2':
        print_pause('Goodbye')
    else:
        bad_input()
        loose_game(items, monster)


def bridge(items, monster):
    print_pause("You're standing in front of the bridge.")
    print_pause('A ' + monster
                + ' is guarding the bridge in front of you.')
    if 'Troll' in monster:
        bridge_troll(items, monster)
    elif 'Witch' in monster:
        bridge_witch(items, monster)


def bridge_witch(items, monster):
    print_pause('She screams with that shrill voice of hers:')
    print_pause('YOU MUST NOT PASS')
    print_pause('and attacks you immediately')
    if 'Sword' in items:
        print_pause('You draw your magic sword.')
        print_pause('When the witch sees the sword, her face is filled with pure fear.'
                    )
        print_pause('Instead of attacking you, she runs away.')
        win_game(items, monster)
    else:
        print_pause("Defenceless without a weapon you are completely at the witch's mercy."
                    )
        print_pause('She kills you without any problem and without any mercy.'
                    )
        loose_game(items, monster)


def bridge_troll(items, monster):
    print_pause('The troll looks at you grimly.')
    print_pause('He speaks to you in his deep voice:')
    print_pause('NO TRANSIT WITHOUT GOLD, HOOMAN')
    if 'Gold' in items:
        print_pause('Fortunately you have the gold from the mill with you.'
                    )
        print_pause('Would you like to...')
        choice = input('''1. Pay the Troll
2. Fight the Troll
''')
        if choice == '1':
            print_pause('You pay the Troll.')
            win_game(items, monster)
        elif 'Sword' in items:
            print_pause('You draw your magic sword.')
            print_pause('When the troll sees the sword, his face is filled with pure fear.'
                        )
            print_pause('Instead of attacking you, he runs away.')
            win_game(items, monster)
        else:
            loose_game(items, monster)
    elif 'Sword' in items:
        print_pause('Fortunately you have the sword from the cave with you.'
                    )
        print_pause('You draw your magic sword.')
        print_pause('When the troll sees the sword, his face is filled with pure fear.'
                    )
        print_pause('Instead of attacking you, he runs away.')
        win_game(items, monster)
    else:
        print_pause("Without sword and gold you are helplessly at the troll's mercy."
                    )
        print_pause('He kills you without immediately.')
        loose_game(items, monster)


def mill(items, monster):
    print_pause('You enter the mill.')
    print_pause("There's nothing exciting to discover here.")
    print_pause('A door leads into the bedroom.')
    print_pause('Would you like to...')
    choice = input('''1. Leave the mill
2. Enter the bedroom
''')
    if choice == '1':
        print_pause('You leave the mill and go back to the field.')
        start_choice(items, monster)
    if choice == '2':
        mill_bedroom(items, monster)
    else:
        bad_input()
        mill(items, monster)


def mill_bedroom(items, monster):
    print_pause('The bedroom looks tidy.')
    if 'Gold' in items:
        print_pause('There is nothing special to discover here')
    else:
        print_pause("There's a sack of gold next to the big bed on the nightstand.\n"
                    )
        print_pause('Would you like to...')
        choice = \
            input('''1. Take the Gold
2. Leave the gold and leave the mill
''')
    if choice == '1':
        print_pause('You take the gold with you and leave the mill.\n')
        items.append('Gold')
        start_choice(items, monster)
    elif choice == '2':
        print_pause('You leave the gold and leave the mill back to the field.\n'
                    )
        start_choice(items, monster)
    else:
        bad_input()
        mill_bedroom(items, monster)


def cave(items, monster):
    print_pause('You enter the cave.')
    print_pause('There is nothing unusual to see here...')
    print_pause('except...')
    print_pause('you discover a sword leaning against the stone in a corner.'
                )
    print_pause('You take the sword with you and leave the cave.')
    items.append('Sword')
    start_choice(items, monster)


def play_game():
    items = []
    monster_pool = ['Troll', 'Witch']
    monster = random.choice(monster_pool)
    intro(items, monster)
    start_choice(items, monster)


play_game()
