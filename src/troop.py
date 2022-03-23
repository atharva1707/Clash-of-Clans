import numpy as np
import colorama as c
import math


# troop class
class Troop:
    static = -1
    def __init__(self,x,y,hp):
        self.x = x
        self.y = y
        self.max_hp = hp
        self.hp = hp
        self.id = self.static
        self.static -= 1
        self.movement_speed = 1 



    def take_damage(self, village, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            village.remove_troop(self)

    def attack(self, x_attack, y_attack, damage, village):
        building = village.get_building(x_attack,y_attack)
        if building != None:        
            building.take_damage(village, damage)

# King class
class King(Troop):
    def __init__(self,x,y,village):
        super().__init__(x,y,500)
        self.axe = 0
        self.damage = 50
        self.ascii = 'K^'
        self.last_move = 'w'
        village.add_troop(self)

    # funciton to move king
    def temp(self):
        print(self.x, self.y)
        
    def move(self, move, villafe):
        if(self.hp<0):
            return
        villafe.remove_troop(self)
        self.last_move = move
        if move == 'a':
            self.ascii = '<K'
            if self.y > 0:
                # check if there is a building in the way
                if villafe.back_grid[self.x][self.y-1] == 0:
                    self.y -= 1
                
        elif move == 'd':
            self.ascii = 'K>'
            if self.y < villafe.length - 1:
                # check if there is a building in the way
                if villafe.back_grid[self.x][self.y+1] == 0:
                    self.y += 1

        elif move == 'w':
            self.ascii = 'K^'
            if self.x > 0:
                # check if there is a building in the way
                if villafe.back_grid[self.x-1][self.y] == 0:
                    self.x -= 1

        elif move == 's':
            self.ascii = 'Kv'
            if self.x < villafe.width - 1:
                # check if there is a building in the way
                if villafe.back_grid[self.x+1][self.y] == 0:
                    self.x += 1
        if self.axe == 1 :
            self.ascii = 'KA'
        villafe.add_troop(self)

    def battack(self,village):
        x_attack = self.x
        y_attack = self.y
        if self.last_move == 'w':
            if self.x > 0:
                x_attack = self.x - 1
                y_attack = self.y
        elif self.last_move == 's':
            if self.x < village.width - 1:
                x_attack = self.x + 1
                y_attack = self.y
        elif self.last_move == 'a':
            if self.y > 0:
                x_attack = self.x
                y_attack = self.y - 1
        elif self.last_move == 'd':
            if self.y < village.length - 1:
                x_attack = self.x
                y_attack = self.y + 1

        self.attack(x_attack, y_attack, self.damage, village)

    def lattack(self,village):
        b = []
        for i in range(max(self.x-4,0), min(self.x+5,village.length-1)):
            for j in range(max(self.y-4,0), min(self.y+5,village.width-1)):
                if village.back_grid[i][j] > 0:
                    b.append(village.get_building(i,j))
                unique_building = set(b)
        for i in unique_building:
            i.take_damage(village, self.damage)


                
    

    # display health using colorama
    def display_health(self):
        print('\t\t\tKings Health: ', end='')
        for i in range(math.ceil(10*self.hp/self.max_hp)):
            if i <= 1:
                print(c.Back.RED + '  ', end='')
            elif i <=4:
                print(c.Back.YELLOW + '  ', end='')
            else:
                print(c.Back.GREEN + '  ', end='')
        print(c.Style.RESET_ALL)
        

# Barbarian class
class Barbarian(Troop):
    def __init__(self,x,y,village):
        super().__init__(x,y,50)
        self.damage = 25
        self.ascii = 'BB'
        self.last_move = 'w'
        village.add_troop(self)
        

    def move(self,village):
        village.remove_troop(self)
        x_dir = village.direction[self.x][self.y][0]
        y_dir = village.direction[self.x][self.y][1]
        x_change = 0 
        y_change = 0
        if x_dir == 0:
            if(y_dir>0):
                y_change = 1
            else:
                y_change = -1
        elif y_dir == 0:
            if(x_dir>0):
                x_change = 1
            else:
                x_change = -1
        else:
            if(x_dir>0):
                x_change = 1
            else:
                x_change = -1    
        if village.back_grid[self.x+x_change][self.y+y_change]==0 :   
            self.x += x_change
            self.y += y_change
        else:
            self.attack(self.x+x_change, self.y+y_change, self.damage, village)
        village.add_troop(self)
        

