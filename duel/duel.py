import random

player1_life = 50
player2_life = 50

player1_potions = 3
player2_potions = 3

heal = random.randint(16, 20)

player1_weapon = input("Player 1 choose your weapon: [1]Sword(10-15), [2]Axe(7-18), [3]Hammer(0-20)")

if player1_weapon == "1":
    p1_min_dps = 10
    p1_max_dps = 15
elif player1_weapon == "2":
    p1_min_dps = 7
    p1_max_dps = 18
else:
    p1_min_dps = 0
    p1_max_dps = 20

player2_weapon = input("Player 2 choose your weapon: [1]Sword(10-15), [2]Axe(7-18), [3]Hammer(0-20)")

if player2_weapon == "1":
    p2_min_dps = 10
    p2_max_dps = 15
elif player2_weapon == "2":
    p2_min_dps = 7
    p2_max_dps = 18
else:
    p2_min_dps = 0
    p2_max_dps = 20
    

player1_dps = random.randint(p1_min_dps, p1_max_dps)
player2_dps = random.randint(p2_min_dps, p2_max_dps)

def player1_attack():
    global player2_life
    x = player1_dps 
    player2_life -= x   
    return x

def player2_attack():
    global player1_life
    y = player2_dps
    player1_life -= y
    return y


def player1_potion():
    global heal
    global player1_life    
    global player1_potions  
    heal1 = heal  
    player1_life += heal1  
    player1_potions -= 1  
    return heal1

def player2_potion():
    global heal
    global player2_life    
    global player2_potions 
    heal2 = heal   
    player2_life += heal2  
    player2_potions -= 1
    return heal2

while player1_life > 0 and player2_life > 0:

    player1_action = input("Player 1 what do you wanna do? (you have " + str(player1_potions) + " potions and " + str(player1_life) + " life) [1]Attack, [2]UsePotion")
    
    if player1_action == "1":
        player1_attack()
        print("You dealt", player2_attack(), "damage to player 2")
    elif player1_action == "2":
        player1_potion()
        print("You healed", player1_potion(), "life")
    else:
        print(player1_action)

    player2_action = input("Player 2 what do you wanna do? (you have " + str(player1_potions) + " potions and " + str(player1_life) + " life) [1]Attack, [2]UsePotion")
    
    if player2_action == "1":
        player2_attack()
        print("You dealt", player1_attack(), "damage to player 2")
    elif player1_action == "2":
        player2_potion()
        print("You healed", player2_potion(), "life")
    else:
        print(player2_action)
        
    if player1_life <= 0:
        print("Player 2 wins")
    elif player2_life <= 0:
        print("Player 1 wins")

