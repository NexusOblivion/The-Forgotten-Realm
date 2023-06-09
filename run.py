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
        case "inv":
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
    if random.randint(1, 10) == 3: #Small chance for a chest to be empty, could be reused to become a chance that it is a mimic instead to add random events?
        print("\nUnlucky, the chest was empty!")
    else:
        for i in range(3): #For three items
            item = random.choice(items_pool) #Randomly pick something from the pool list
            chest.append(item) #and add it to the chest
        inventory.extend(chest)
        #TO DO: potentially change the string formatting to use items = ", ".join(chest) then print them out
        print("\nThe following items: " + str(chest) + " were added to your inventory!")


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
    print("\nExcept for one.\n")
    print("You notice it in the center, a serpent coiled around a staff. A rush of anticipation surges through you as you realize this is a test of your intelligence, a challenge waiting to be conquered.")
    print("Your mind races, searching for connections, seeking patterns, and drawing upon your lacking knowledge of ancient civilizations and symbolism.\n")
    print("How do you proceed?")
    print(" [1] - Rotate the circle to reorient the staff")
    print(" [2] - Attempt to decode the scriptures")
    while True:
        action = input("> ")
        if action == "1":
            print("\nYou begin to gently rotate the puzzle, looking for patterns or hoping for a lucky alignment.")
            print("As you continue the rotational exploration, a glimmer of hope emerges. You notice that as you turn the puzzle, certain symbols or markings on the serpent align with corresponding features on the staff")
            print("You become more methodical in your rotations, noting the specific alignments that occur at different angles.")
            print("With each rotation, you seem to draw closer to the conclusion of this quest")
            print("A specific alignment catches your eye.")
            print("Filled with anticipation and determination, you reach the most natural alignment. The door swings open, revealing what lies beyond")
            stage_three()
        elif action == "2":
            print("\nYou look closely at the serpent and staff, noting down any unique markings you observe")
            print("Using your limited understanding of the lost relics of the realm, you rack your brain for references to ancient mythologies or subtle symbolisms")
            print("After some time, you discover that the markings reveal a message:")
            print("\n'Let the cyclical nature guide your hand.'\n")
            print("As you contemplate the enigmatic puzzle, you recall the message's intriguing directive.")
            print("A realisation overwhelms you as you turn the puzzle to match the cyclic nature of the serpents path")
            print("The door swings open, revealing what lies beyond")
            stage_three()

        else:
            print("Please input an appropriate choice from the list given")

def stage_three():
    print("\nA sense of awe washes over you")
    print("Before you stands a sight you could have never prepared to see when intially setting out to explore this realm.")
    print("A hidden, unknown ancient city, thriving with life stared back at you.")
    print("The air is filled with a scent of antiquity mixed with a vibrant energy that pulses through the streets. Sunlight spills in through towering structures, casting long shadows on the cobblestone below")
    print("The city resonates with the hum of activity as all forms of life navigate through the streets - vendors hawking their wares, their attire reflects the fashion of a bygone time, with flowing robes, intricate patterns, and accessories that speak of craftsmanship")
    print("\nYou hesistantly begin to walk among them, taking note of their attire which reflects the fashion of a bygone time, with flowing robes, intricate patterns, and accessories that speak of craftsmanship")
    print("As you wander through the ancient city further, you stumble upon a narrow alleyway that seems to beckon you with whispered secrets.")
    print("A flickering lantern casts eerie shadows on the worn cobblestones. Ahead, you notice a small, weathered door partially ajar.") #The start of opening up the world to the player
    print("What will you do?")
    print(" [1] - Continue exploring the main streets")
    print(" [2] - Enter the alleyway and investigate the half open door") #TO DO: rewrite this to be seperate lines
    while True: #TO DO: potentially make a function for this as the failsafe is used multiple times
        action = input("> ")
        if action == "1":
            print("You override the primal temptation to explore the mystifying alleyway and continue through the bustling markets lost to time")
            print("Approaching a nearby merchant, your footsteps echoed against the dying sense of the streets drawing the attention of all those around")
            print("Your prescence wasn't welcomed.")
            print("Eager to learn about what the f*ck this place was, you lean in and engage with the elderly man")
            #TO DO: create a function that handles the bulk of NPC dialogue?
        elif action == "2":
            print("\nThe alleyway draws you closer as the sinister shadows dance beneath your feet.")
            print("With a cautious grip, you nudge the door open and it emits a squeal protesting the years of neglect.")
            print("\nA sudden gust of stale air laced with a touch of mustiness envelops you, brushing against your face")
            print("As you step into the room, the feeble illumination struggles to penetrate the layers of dust that cling to every surface")
            print("Cobwebs hang delicately from the ceiling, their intricate threads glistening with age.")
            print("Faded portraits hung askew on the walls, their subjects long lost to history")
            print("\nIn one corner, partly obscured by the gloom, an old chest barely stands, the wood cracked and faded")
            print("With a sense of anticipation, you shuffle over to the corner and open the chest")
            generate_chest()
            while True: 
                command = input("> ") 
                if command.startswith("="): 
                    command_handler(command)
                    break
            print("Your heart races with excitment as you hit the ???/")
            print("You make your way out of the alleyway, stepping out into the sunlight the virbance of the unknown world envelops your senses.")
        else:
            print("Please pick from one of the options listed!")

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