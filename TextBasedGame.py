def show_instructions():
    # print a main menu and the commands
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: 'go South', 'go North', 'go East', 'go West'")
    print("Add to Inventory: 'pickup [item name]'")


rooms = {
    "Master Bedroom": {'go South': 'Family Room', 'go East': 'Bathroom', 'item': 'Drums'},
    "Family Room": {'go North': 'Master Bedroom', 'go West': 'Gaming Room', 'go East': 'Dining Room', 'go South': 'Guest Bedroom', 'item': 'Simon Says Game'},
    "Bathroom": {'go West': 'Master Bedroom', 'item': 'Elmo Doll'},
    "Guest Bedroom": {'go North': 'Family Room', 'go East': 'Toddler Bedroom', 'item': 'Piano'},
    "Dining Room": {'go North': 'Kitchen', 'go West': 'Family Room'},
    "Gaming Room": {'go East': 'Family Room', 'item': 'BOP It'},
    "Kitchen": {'go South': 'Dining Room', 'item': 'Dancing Duck Musical Toy'},
    "Toddler Room": {'go West': 'Guest Bedroom', 'item': 'Dragon'}  # villain
}

items_collected = []


def play_again():
    print("\nDo you want to play again? (y or n)")

    # convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        exit()


def game_over(reason):
    # print the "reason" in a new line (\n)
    print("\n" + reason)
    print("Game Over!")
    # ask player to play again or not by activating play_again() function
    play_again()


def master_bedroom():
    # some prompts
    print("\nYou are now in the master bedroom!")
    print('Inventory: ' + str(items_collected))
    print('You see a ' + rooms['Master Bedroom']['item'] + ' on the ground.')
    print('There is a door to the South')
    print('There is a door to the East')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    if answer.lower() == 'east' or answer.lower() == 'go east':
        bathroom()
    elif answer.lower() == 'south' or answer.lower() == 'go south':
        family_room()
    elif answer.lower() == 'pickup' or answer == 'pickup ' + rooms['Master Bedroom']['item']:
        if 'Drums' not in items_collected:
            items_collected.append(rooms['Master Bedroom']['item'])
            print("\nNice, you picked up " + rooms['Master Bedroom']['item'])
            master_bedroom()
        else:
            print("\nItem already in inventory!")
            master_bedroom()
    else:
        print("Command not understood!")
        show_instructions()
        master_bedroom()


def family_room():
    # some prompts
    print("\nYou are now in the family room!")
    print('Inventory: ' + str(items_collected))
    print('You see a ' + rooms['Family Room']['item'] + ' on the ground.')
    print('There is a door to the North')
    print('There is a door to the South')
    print('There is a door to the East')
    print('There is a door to the West')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Family Room": {'go North': 'Master Bedroom', 'go West': 'Gaming Room', 'go East': 'Dining Room', 'go South': 'Guest Bedroom', 'item': 'Simon Says Game'}

    if answer.lower() == 'north' or answer.lower() == 'go north':
        master_bedroom()
    elif answer.lower() == 'south' or answer.lower() == 'go south':
        guest_bedroom()
    elif answer.lower() == 'west' or answer.lower() == 'go west':
        gaming_room()
    elif answer.lower() == 'east' or answer.lower() == 'go east':
        dining_room()
    elif answer.lower() == 'pickup' or answer == 'pickup ' + rooms['Family Room']['item']:
        if rooms['Family Room']['item'] not in items_collected:
            items_collected.append(rooms['Family Room']['item'])
            print("\nNice, you picked up " + rooms['Family Room']['item'])
            family_room()
        else:
            print("\nItem already in inventory!")
            family_room()
    else:
        print("Command not understood!")
        show_instructions()
        family_room()


def bathroom():
    # some prompts
    print("\nYou are now in the bathroom!")
    print('Inventory: ' + str(items_collected))
    print('You see a ' + rooms['Bathroom']['item'] + ' on the ground.')
    print('There is a door to the West')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Bathroom": {'go West': 'Master Bedroom', 'item': 'Elmo Doll'},
    if answer.lower() == 'west' or answer.lower() == 'go west':
        master_bedroom()
    elif answer.lower() == 'pickup' or answer == 'pickup ' + rooms['Bathroom']['item']:
        if rooms['Bathroom']['item'] not in items_collected:
            items_collected.append(rooms['Bathroom']['item'])
            print("\nNice, you picked up " + rooms['Bathroom']['item'])
            bathroom()
        else:
            print("\nItem already in inventory!")
            bathroom()
    else:
        print("Command not understood!")
        show_instructions()
        master_bedroom()


def guest_bedroom():
    # some prompts
    print("\nYou are now in the guest bedroom!")
    print('Inventory: ' + str(items_collected))
    print('You see a ' + rooms['Guest Bedroom']['item'] + ' on the ground.')
    print('There is a door to the North')
    print('There is a door to the East')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Guest Bedroom": {'go North': 'Family Room', 'go East': 'Toddler Bedroom', 'item': 'Piano'}

    if answer.lower() == 'north' or answer.lower() == 'go north':
        family_room()
    elif answer.lower() == 'east' or answer.lower() == 'go east':
        toddler_room()
    elif answer.lower() == 'pickup' or answer == 'pickup ' + rooms['Guest Bedroom']['item']:
        if rooms['Guest Bedroom']['item'] not in items_collected:
            items_collected.append(rooms['Guest Bedroom']['item'])
            print("\nNice, you picked up " + rooms['Guest Bedroom']['item'])
            guest_bedroom()
        else:
            print("\nItem already in inventory!")
            guest_bedroom()
    else:
        print("Command not understood!")
        show_instructions()
        guest_bedroom()


def dining_room():
    # some prompts
    print("\nYou are now in the dining room!")
    print('Inventory: ' + str(items_collected))
    print('There is a door to the North')
    print('There is a door to the West')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Dining Room": {'go North': 'Kitchen', 'go West': 'Family Room'}
    if answer.lower() == 'north' or answer.lower() == 'go north':
        kitchen()
    elif answer.lower() == 'west' or answer.lower() == 'go west':
        family_room()
    else:
        print("Command not understood!")
        show_instructions()
        dining_room()


def gaming_room():
    # some prompts
    print("\nYou are now in the gaming room!")
    print('Inventory: ' + str(items_collected))
    print('There is a door to the East')
    print('You see a ' + rooms['Gaming Room']['item'] + ' on the ground.')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Gaming Room": {'go East': 'Family Room', 'item': 'BOP It'},
    if answer.lower() == 'east' or answer.lower() == 'go east':
        family_room()
    elif answer.lower() == 'pickup' or answer == 'pickup ' + rooms['Gaming Room']['item']:
        if rooms['Gaming Room']['item'] not in items_collected:
            items_collected.append(rooms['Gaming Room']['item'])
            print("\nNice, you picked up " + rooms['Gaming Room']['item'])
            gaming_room()
        else:
            print("\nItem already in inventory!")
            gaming_room()
    else:
        print("Command not understood!")
        show_instructions()
        gaming_room()


def kitchen():
    # some prompts
    print("\nYou are now in the kitchen!")
    print('Inventory: ' + str(items_collected))
    print('There is a door to the South')
    print('You see a ' + rooms['Kitchen']['item'] + ' on the ground.')
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Kitchen": {'go South': 'Dining Room', 'item': 'Dancing Duck Musical Toy'}
    if answer.lower() == 'south' or answer.lower() == 'go south':
        dining_room()
    elif answer.lower() == 'pickup' or answer == 'pickup ' + rooms['Kitchen']['item']:
        if rooms['Kitchen']['item'] not in items_collected:
            items_collected.append(rooms['Kitchen']['item'])
            print("\nNice, you picked up " + rooms['Kitchen']['item'])
            kitchen()
        else:
            print("\nItem already in inventory!")
            kitchen()
    else:
        print("Command not understood!")
        show_instructions()
        kitchen()


def toddler_room():
    # some prompts
    print("\nYou are now in the toddler room")
    print('Inventory: ' + str(items_collected))
    print('There is a door to the West')
    print("You see a big dragon! You have the option to 'fight'")
    print('--------------------------')
    print('Enter your move:')

    # take input()
    answer = input(">")

    # "Toddler Room": {'go West': 'Guest Bedroom', 'item': 'Dragon'}  # villain
    if answer.lower() == 'west' or answer.lower() == 'go west':
        guest_bedroom()
    elif answer.lower() == 'fight':
        if len(items_collected) == 6:
            print("You fuse the items and create a magical sword to slay the dragon.")
            game_over("You win!")
        else:
            game_over(
                "You didn't have all the items needed to defeat the dragon! It eats you.")
    else:
        print("Command not understood!")
        show_instructions()
        toddler_room()


def start():
    master_bedroom()


# start the game
start()
