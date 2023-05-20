from include import *

#-----------------Player, Chests, Upgrades (Variable Declarations)-----------------#

inventory = [
    'Torch'
]

player = {
    "health": 100
}

chest = []

#-----------------Game Options-----------------#

def main_menu():
    print('''
████████╗██╗░░██╗███████╗  ███████╗░█████╗░██████╗░░██████╗░░█████╗░████████╗████████╗███████╗███╗░░██╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔════╝░██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗░██║
░░░██║░░░███████║█████╗░░  █████╗░░██║░░██║██████╔╝██║░░██╗░██║░░██║░░░██║░░░░░░██║░░░█████╗░░██╔██╗██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║░░██║██╔══██╗██║░░╚██╗██║░░██║░░░██║░░░░░░██║░░░██╔══╝░░██║╚████║
░░░██║░░░██║░░██║███████╗  ██║░░░░░╚█████╔╝██║░░██║╚██████╔╝╚█████╔╝░░░██║░░░░░░██║░░░███████╗██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝
██████╗░███████╗░█████╗░██╗░░░░░███╗░░░███╗
██╔══██╗██╔════╝██╔══██╗██║░░░░░████╗░████║
██████╔╝█████╗░░███████║██║░░░░░██╔████╔██║
██╔══██╗██╔══╝░░██╔══██║██║░░░░░██║╚██╔╝██║
██║░░██║███████╗██║░░██║███████╗██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝ 

''')
    #Main Menu Options
    print("*---Main Menu---*")
    print(" 1 - New Game")
    print(" 2 - Load Game")
    print(" 3 - Exit Game")
    print(" 4 - About")
    action = input("> ")
    return action

def new_game():
    print("\n*---New Game---*")
    print("As an archeologist driven by an insatiable thirst for knowledge and adventure, you find yourself at the entrance of a forgotten realm brimming with mysteries waiting to be unraveled.")
    print("The air is thick with anticipation, and a sense of ancient energy permeates the atmosphere.")
    print("As you enter the forgotten realm, you notice intricate carvings and symbols that hint at a civilization long lost to time.")
    print("The choice is yours, valiant archaeologist. The forgotten realm awaits your exploration, its mysteries yearning to be unearthed. May your path be guided by wisdom and tempered by a thirst for truth.")
    print("\nDo you wish to continue?")
    print(" [1] - Yes")
    print(" [2] - No")
    action = input("> ")
    if action == "1":
        stage_one()
    else:
        exit_game()
    
def load_game():
    return

def exit_game():
    sys.exit("Farewell, valiant archaeologist. Thank you for playing!")

def about_page():
    print("\n*---About Page---*")
    print("'Forgotten Realm' is an immersive text-based artsy sci-fi roguelike game that invites you to step into the shoes of an ambitious archaeologist.")
    print("This project was inspired by a randomly generated idea from https://seblague.github.io/ideagenerator/")
    print("Made by: https://github.com/NexusOblivion")

#-----------------Game Mechanics-----------------#

def command_handler(command):
    command = command[1:] #Removes the prefix from the command to help with identifying which command was used
    match command:
        case "help":
            print("\nIf you're feeling stuck or need assistance, you've come to the right place. Below you'll find a list of commonly used commands and tips to navigate through this exciting adventure:")
            print(" Inventory -  To check what items you're carrying, type '=inventory' or '=items.' This will provide you with a list of the items in your possession.")
            print(" Help - If you need assistance or a reminder of available commands, type '=help' to display this help message.")
            print(" Use - Utilize items in your inventory by using the '=use' command, followed by the item's name. For example, 'use sword' or 'use potion.'")
            print(" Examine - Look at an object or puzzle in better detail to learn clues to help you progress by using the '=examine' command")
        case "inventory":
            print("\nYou have the following items in your inventory:")
            print(inventory)
        case "use":
            return
        case "examine":
            return
        case "save":
            return
        case _:
            print("Command not recognised.")

def generate_chest(): #Generates a chest of 3 random items from the loot pool, with a chance to have an empty chest
    items_pool = ["Health Potion", "Elixir of Strength", "Leather Boots", "Leather Helmet", "Shield", "Gold Coins", "Cloth", "Ruby"] #Loot pool can be changed
    if random.randint(1, 10) == 3: #Small chance for a chest to be empty
        print(chest)
    else:
        for i in range(3): #For three items
            item = random.choice(items_pool) #Randomly pick something from the pool list
            chest.append(item) #and add it to the chest
        print(chest)


#-----------------Game Stages-----------------#

def stage_one():
    print("\nAs you wander into the forgotten realm, the dim light of your torch flickers cast eerie shadows on the walls.")
    print("You find yourself stumbling to the grand stone door of a chamber lost to time and push it open to reveal the vast emptiness beyond.")
    print("Stepping into the darkness, the atmosphere shifts sending a shiver down your spine.")
    print("\nSomething is watching" + '\x1B[3m' + ' you.' + '\033[0m\n') #Individual words placed in italics
    print("In the depths of the dimly lit chamber, its malevolent gaze lingers, but you dare not meet the eyes of the unseen.")
    print("Floating at the center of the chamber, the glow of an enigmatic artifact draws you closer with it's allure.")
    print("Summoning all your courage, you tighten your grip on the artifact, its power surging through your veins, ready to defend yourself against whatever lurks in the shadows")
    print("A low growl echoes through the air as it emerges from the darkness, maintained its unsettling gaze directed at you\n")
    print("Without warning, it lunges at you.")
    print("You barely sidestep the lunging strike and you're forced to defend yourself")
    print("\nDo you:")
    print(" [1] - Utilize the artifact in an attempt to deliever a focused blast")
    print(" [2] - Attempt a swift retreat towards the chamber's exit")
    while True: #Acts as a failsafe so that the only options are 1 or 2
        action = input("> ")
        if action == "1":
            stage_one_artifact()
            break
        elif action == "2":
            print("\nYou frantically attempt to return the the chambers exit, waving your torch around in a failed attempt to regain your barings.")
            print("There's no way out.")
            print("Turning in desperation, you clutch onto the artifact hoping that it will protect you from whatever it is.") 
            stage_one_artifact() #Both options lead to the same function, freedom will be introduced later on with a bigger choice tree
            break
        else:
            print("Please pick from one of the options listed!")

def stage_one_artifact():
    print("\nYour hands press hard onto the pulsating artifact as it's immense energy surges through your veins.")
    print("It unleashes a cataclysmic force in the direct of it. Oblierating it in an instant. The room quakes from the raw power generated as the creature's decrepit remains crumble to the ground. ")
    print("You stand amongst the aftermath, shaken by harnessing such destructive power.")
    print("\nWhat.. was that?")
    stage_two()

def stage_two():
    print("\nAs the dust settles, you survey the scene before you, your heart still pounding from the overwhelming energy that coursed through your veins.")
    print("The once formidable creature that had threatened your existence now lay in a heap of rubble, its presence extinguished forever.")
    print("The danger has passed, but the room remains a shattered testament to the battle that took place.")
    print("\nAmidst the debris strewn chamberm, a glimmer amongst the chaos catches your attention")
    print("Did the artifact shatter? Was it another artifact?")
    print("You cautiously approach the source of the light and discover a magnificent blade half buried in rubble recently thrown across the room.")
    print("You grasp the hilt, adorned with intricate engravings, firmly and feel the rush of power through your fingertips")
    print("The artifact you obtained earlier, the one responsible for unleashing the cataclysmic force, fuses seamlessly with the sword, merging its power with the weapon.")
    print("The room trembles once again, but this time it's not from destruction. It's as if the very space recognizes the union of the sword and artifact, resonating with an ancient power reborn.")
    print("\n\x1B[3mYou\033[0m were the chosen one. ")
    print("\n> You can use the 'inventory' command with the = prefix to see what items you possess")
    print("> Use of commands will be controlled. The game will give tooltips using the > prefix! Use =help to see all commands")
    inventory.append('Sword') #Adds the sword to the inventory, .extend does not work as it adds the individual characters instead of the string. Extend can be used to add another array, eg. a chest
    while True: #Story will not continue until a command is entered
        command = input("> ") #Command returns as =input
        if command.startswith("="): #Checks if the input follows command syntax before it reaches the function - it does not need to be checked twice
            command_handler(command)
            break
    print("\nYou begin to wonder, why me, a random archelogist?")
    print("What other secrets does this empire hold?")
    print("\nWith no option to leave the chamber, and trying to shake off what you just witnessed, you venture further and come across far end of the passage")
    print("As you shone your light agaisnt the edges of the room, a large circular pattern emerged, revealing a series of interconnected symbols etched into the stone.")
    print("It was a puzzle waiting to be deciphered")
    print("The symbols mimicked shapes of which you have never seen before")
    print("Except for one.")
    print("You notice it in the center, a serpent coiled around a staff. A rush of anticipation surges through you as you realize this is a test of your intelligence, a challenge waiting to be conquered.")
    print("Your mind races, searching for connections, seeking patterns, and drawing upon your lacking knowledge of ancient civilizations and symbolism.")
    print("How do you proceed?")
    print(" [1] - Rotate the circle to reorient the staff")
    print(" [2] - Attempt to decode the scriptures")
    while True:
        action = input("> ")
        if action == "1":
            print("You begin to gently rotate the puzzle, looking for patterns or hoping for a lucky alignment.")
            print("As you continue the rotational exploration, a glimmer of hope emerges. You notice that as you turn the puzzle, certain symbols or markings on the serpent align with corresponding features on the staff")
            print("You become more methodical in your rotations, noting the specific alignments that occur at different angles.")
            print("With each rotation, you seem to draw closer to the conclusion of this quest")
            print("A specific alignment catches your eye.")
            print("Filled with anticipation and determination, you reach the most natural alignment. The door swings open, revealing what lies beyond")
            stage_three()
        elif action == "2":
            print("You look closely at the serpent and staff, noting down any unique markings you observe")
            print("Using your limited understanding of the lost relics of the realm, you rack your brain for references to ancient mythologies or subtle symbolisms")
            print("After some time, you discover that the markings reveal a message:")
            print("'Let the cyclical nature guide your hand.'")
            print("As you contemplate the enigmatic puzzle, you recall the message's intriguing directive.")
            print("A realisation overwhelms you as you turn the puzzle to match the cyclic nature of the serpents path")
            print("The door swings open, revealing what lies beyond")
            stage_three()

        else:
            print("Please input an appropriate choice from the list given")

def stage_three():
    return

if __name__ == '__main__':
    match main_menu():
        case "1":
            new_game()
        case "2": 
            load_game()
        case "3":
            exit_game()
        case "4":
            about_page()
        case _: 
            print("fail safe")