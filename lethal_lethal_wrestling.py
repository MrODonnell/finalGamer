class Wrestler:
    """This is the beginning of a class for the wrestler"""

    def __init__(self, name, mass, sig_moves, fin_moves):
        self.name = name
        self.mass = mass
        self.sig_moves = sig_moves
        self.fin_moves = fin_moves

class Moves:
    """This is the beginning of a class for moves"""

    def __init__(self, name):
        self.gen_moves = gen_moves

class Weapons:
    """This is the beginning of a class for weapons"""

    def __init__(self, name):
        self.weapons = weapons

class Matches:
    """This is the beginning of a class for matches"""

    def __init__(self, name):
        self.stipulations = stipulations

class Payperviews:
    """This is the beginning of a class for the payperview"""

    def __init__(self, name):
        self.payperviews = payperviews

class Championships:
    """This is the beginning of a class for the championships"""

    def __init__(self, name):
        self.championships = championships 

def checkInput(someInput):
    print(str(len(someInput.strip())))
    return someInput

print("Hello")


wrestlers = {'Sanaa', 'Bidziil', 'Ishita', 'Hào', 'Adela', 'The Bionic Man'}
mass = {'Sanaa': 201, 'Bidziil': 190, 'Ishita': 205 , 'Hào': 182 , 'Adela': 180 , 'The Bionic Man': 290 }
sig_moves = {'Sanaa': "Spinning Crane Leg Kick", 'Bidziil': "Lunar Assault" , 'Ishita': "Sleeper Headlock" , 'Hào': "Elevated Elbow Smash", 'Adela': "Firework Neckbreaker", 'The Bionic Man': "Bionic Elbow Drop"}
fin_moves = {'Sanaa': "Praying Mantis", 'Bidziil': "Supernova Body Bomb" , 'Ishita': "Octopus Grip", 'Hào': "Flying Chokeslame", 'Adela': "Two-Handed Gut Buster", 'The Bionic Man': "Shooting Star Spinning Kick"}

print("\n\n")
print(wrestlers)
print("\n\n")
print(mass)
print("\n\n")
print(sig_moves)
print("\n\n")
print(fin_moves)
print("\n\n")

user_names = ["Sanaa", "Bidziil","Ishita", "Hào", "Adela","The Bionic Man"]
user_response = ''
user_name = ''    

def validate(un, un_list):
    global user_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            user_name = list_item
            return False
        count += 1
    return True

while validate(user_response, user_names):
    user_response = input("What champion name would you like to use? ")

champion = Wrestler(user_name, mass[user_name], sig_moves[user_name], fin_moves[user_name])
print(champion.mass)


while validate(user_response, user_names):
    user_response = input("What challenger name would you like to use? ")

challenger = Wrestler(user_name, mass[user_name], sig_moves[user_name], fin_moves[user_name])
print(challenger.mass)

# The values of the signature moves
spinning_crane_leg_kick = 15
lunar_assualt = 25
sleeper_headlock = 20
elevated_elbow_smash = 15
firework_neckbreaker =25
bionic_elbow_drop = 15

# The values of the finishing moves
praying_mantis = 20
supernova_body_bomb = 25
octopus_grip = 20
flying_chokeslam = 15
two_handed_gut_buster = 15
shooting_star_spinning_kick = 25



# character_name = ''
# while character_name 
# character_name = input("Pick a Wrestler: ")

# opponent_name = input("Pick an Opponent: ")


gen_moves = {"Dropkick", "DDT", "Sharpshooter", "Moonsault"}
print("\n\n")
print(gen_moves)

genMove_names = ["Dropkick", "DDT","Sharpshooter", "Moonsault"]
user_response = ''
genMove_name = ''    

def validate1(un, un_list):
    global genMove_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            genMove_name = list_item
            return False
        count += 1
    return True

while validate1(user_response, gen_moves):
    user_response = input("What generic move would your champion like to use? ")


while validate1(user_response, gen_moves):
    user_response = input("What generic move would your challenger like to use? ")

print("the generic move name is: " + user_response + " -- " + genMove_name)
print(genMove_names)

dropkick = 10
DDT = 5
Sharpshooter = 20
Moonsault = 20



# genWrestler_name = input("Pick a Generic Move for Your Character: ")
# genOpponent_name = input("Pick a Generic Move for Your Opponent: ")


weapons = {'Thumbtacks', 'Steel Folding Chair', 'Table', 'Ladder', 'Trash Can', 'Barbed Wire Baseball Bat', 'Handcuffs', 'Kendo Sticks', 'Sledgehammer'}
print("\n\n")
print(weapons)

weapons_names = ["Thumbtacks", "Steel Folding Chair","Table", "Ladder", "Trash Can", "Barbed Wire Bat", "Handcuffs", "Kendo Sticks", "Sledgehammer"]
user_response = ''
weapon_name = ''    

def validate2(un, un_list):
    global weapon_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            weapon_name = list_item
            return False
        count += 1
    return True

while validate(user_response, weapons_names):
    user_response = input("What weapon would your champion like to use? ")

while validate(user_response, weapons_names):
    user_response = input("What weapon would your challenger like to use? ")

print("the weapons name is: " + user_response + " -- " + weapon_name)
print(weapons_names)

Thumbtacks = 20
steel_folding_chair = 10
Table = 10
Ladder = 25
trash_can = 10
barbed_wire_baseball_bat = 15
Handcuffs = 5
kendo_sticks = 15
sledgehammer = 15

# weaponWrestler_name = input("Pick a Weapon for Your Character: ")
# weaponOpponent_name = input("Pick a Weapon for Your Opponent: ")


stipulations = {'I Quit Match', 'Ladder Match', 'Pinfall Match', 'Submission Match', 'Pinfall Anywhere Match', 'Time Limit Match'}
print("\n\n")
print(stipulations)
# stip_name = input("Pick a Match Stipulation: ")


stipulations_names = ["I Quit Match", "Ladder Match","Pinfall Match", "Submission Match", "Pinfall Anywhere Match", "Time Limit Match"]
user_response = ''
stipulation_name = ''    

def validate3(un, un_list):
    global stipulation_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            stipulation_name = list_item
            return False
        count += 1
    return True

while validate(user_response, stipulations_names):
    user_response = input("What stipulation would you like to have? ")

print("the stipulation name is: " + user_response + " -- " + stipulation_name)
print(stipulations_names)


payperviews = {'Lethal Ladders', 'Lethal World', 'Lethal Empire', 'Lethal Tournament', 'Heavyweight Tournement', 'Lightweight Tournement', 'Lethal Cage', 'Nothing Left to Lose'}
print("\n\n")
print(payperviews)
ppv_name = input("Pick a Payperview: ")

payperviews_names = ["Lethal Ladders", "Lethal World","Lethal Empire", "Lethal Tournament", "Heavyweight Tournement", "Lightweight Tournement", "Lethal Cage", "Nothing Left to Lose"]
user_response = ''
payperview_name = ''    

def validate4(un, un_list):
    global payperview_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            payperview_name = list_item
            return False
            count += 1
    return True

while validate(user_response, payperviews_names):
    user_response = input("What payperview would you like to fight at? ")

print("the payperview name is: " + user_response + " -- " + payperview_name)
print(payperviews_names)


championships = {'Lightweight Championship', 'Intercontinental Championship', 'Heavyweight Championship', 'Lethal Championship',
                 'Universal Championship', 'Ultimate Championship', 'United States Championship'}
print("\n\n")
#print(championships)
# champ_name = input("Pick a Championship: ")

championships_names = ["Universal Champioship", "Lightweight Championship","Intercontinental Championship", "Heaveyweight Championship",
                       "Lethal Championship", "Ultimate Championship"]
user_response = ''
championships_name = ''    

def validate5(un, un_list):
    global championships_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            championships_name = list_item
            return False
        count += 1
    return True

while validate(user_response, championships_names):
    user_response = input("What championship would you like to fight for? ")

print("the championships name is: " + user_response + " -- " + championship_name)
print(championships_names)




count = 0
for x in wrestlers:
    if x.lower() == champion_name.lower():
        if x != champion_name:
            champion_name = champion_name.title()
        champion = Wrestler(champion_name, mass[champion_name], sig_moves[champion_name], fin_moves[champion_name])
        count += 1
        # print(count)
    del wrestlers[count]
    count = 0

    for x in wrestlers:
        if x.lower() == challenger_name.lower():
            if x != challenger_name:
                challenger_name = challenger_name.title()
        challenger = Wrestler(challenger_name, mass[challenger_name])
        count += 1
        # print(count)
    del wrestlers[count]



#opponent = Wrestler(opponent_name, mass[opponent_name])

run = True

while run:
    ans = input("\n say something: ")
    print("your answer was: " + ans)

    if ans == 'quit':
        run = False


print("Goodbye!")
