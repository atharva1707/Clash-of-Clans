import numpy as np
import colorama as c
from src.input import *
from src.building import *
from src.village import Village
from src.troop import *
from src.spells import *
import os
import time 
import json



village = Village(30,30)
village.display()

# array to store input
input_array = []

# add townhall to village
townhall = Townhall(12,13)
cannon1 = Cannon(14,8)
cannon2 = Cannon(14,21)
hut1 = Hut(10,8)
hut2 = Hut(19,8)
hut3 = Hut(19,20)
hut4 = Hut(10,20)
hut5 = Hut(16,14)
village.add_building(townhall)
village.add_building(cannon1)
village.add_building(cannon2)
village.add_building(hut1)
village.add_building(hut2)
village.add_building(hut3)
village.add_building(hut4)
village.add_building(hut5)  
king = King(5,5,village)

Walls = []
for i in range (0,30):
    Walls.append(Wall(7,i))
    village.add_building(Walls[i])
for i in range (0,30):
    Walls.append(Wall(22,i))
    village.add_building(Walls[i+30])

for i in range (8,22):
    Walls.append(Wall(i,11))
    village.add_building(Walls[i+60-8])

for i in range (8,22):
    Walls.append(Wall(i,18))
    village.add_building(Walls[i+74-8])

village.display()

Barbarians = [] 
heal = Heal()
rage = Rage()
barb_deploy = 0
os.system('stty -echo')
while 1:
    start_time = time.time()
    imp = input_to(Get(),0.25)
    input_array.append(imp)
    if imp == 'q':
        break
    elif imp == 'w':
        king.move('w', village)
    elif imp == 's':
        king.move('s', village)
    elif imp == 'a':
        king.move('a', village)
    elif imp == 'd':
        king.move('d', village)

    elif imp == ' ':
        if king.axe :
            king.lattack(village)
        else:
            king.battack(village)

    elif imp == '1':
        if barb_deploy == 20:
            continue
        Barbarians.append(Barbarian(1,1,village))
        barb_deploy += 1
    elif imp == '2':
        if barb_deploy == 20:
            continue
        Barbarians.append(Barbarian(1,27,village))
        barb_deploy += 1
    elif imp == '3':
        if barb_deploy == 20:
            continue
        Barbarians.append(Barbarian(27,27,village))
        barb_deploy += 1


    elif imp == 'l':
        king.axe = 1 - king.axe
        village.remove_troop(king)
        if king.axe ==1 :
            king.ascii = 'KA'
        else:
            if king.last_move == 'w':
                king.ascii = 'K^'
            elif king.last_move == 's':
                king.ascii = 'Kv'
            elif king.last_move == 'a':
                king.ascii = 'K<'
            elif king.last_move == 'd':
                king.ascii = 'K>'
        village.add_troop(king)

    elif imp == 'h':
        heal.activate(king,Barbarians)

    elif imp == 'r':
        rage.activate(king,Barbarians)

    elif imp == 't':
        village.remove_troop(king)
        king.hp = king.max_hp
        village.add_troop(king)

    for barbarian in Barbarians:
        barbarian.move(village)
    if(cannon1.hp>=0):
        cannon1.shoot(village)
    if(cannon2.hp>=0):
        cannon2.shoot(village)
    os.system('clear')
    village.display()
    king.display_health()
    print('\t\t\tBarbarians left = ' + str(20 - barb_deploy))
    for barbarian in Barbarians:
        if barbarian.hp <= 0:
            Barbarians.remove(barbarian)
    end = village.check_end()
    if(end == 1):
        print('\n\n\nYAYY YOU WON')
        break
    elif(end == 2):
        if king.hp <= 0 and barb_deploy == 20:
            print('\n\n\nYOU LOST')
            break
    end_time = time.time()
    time.sleep(0.1 - min(end_time - start_time,0.1))
    
    
os.system('stty echo')



# input file name
input_file = input('Save game as: ')


# store input array in a json file in a folder
with open('replays/' + input_file + '.json', 'w') as outfile:
    json.dump(input_array, outfile)
