# buildings

class Building:
    static = 1
    def __init__(self, x, y, width, length, max_hp):
        self.id = self.static
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.max_hp = max_hp
        self.hp = max_hp
        Building.static = Building.static + 1

    # function for taking damage
    def take_damage(self, village, damage):
        self.hp = self.hp - damage
        if self.hp <= 0.5*self.max_hp:
            village.turn_yellow(self)
        if self.hp <= 0.2*self.max_hp:
            village.turn_red(self)
        if self.hp < 0:
            village.remove_building(self)
            
            

    
    

# townhall classs
class Townhall(Building):
    def __init__(self, x, y):
        super().__init__(x, y, 3, 4, 500)
        self.building_array = []
        self.ascii()
        

    # import townhall from townhall.txt
    def ascii(self):
        file = open('src/townhall.txt', 'r')
        for line in file:
            self.building_array.append(line)
        file.close()

# cannon class
class Cannon(Building):
    def __init__(self, x, y):
        super().__init__(x, y, 3, 1, 400)
        self.building_array = []
        self.ascii()
        

    # import cannon from cannon.txt
    def ascii(self):
        file = open('src/cannon.txt', 'r')
        for line in file:
            self.building_array.append(line)
        file.close()

    # cannon shoot in range 5
    def shoot(self, village):
        for i in range(max(self.x-4,0), min(self.x+5+2,village.length-1)):
            for j in range(max(self.y-4,0), min(self.y+5,village.width-1)):
                if village.back_grid[i][j] < 0:
                    trp = village.get_troop(i,j)
                    if trp != None:
                        trp.take_damage(village, 10)
                    village.turn_white(self)
                    return
        village.turn_green(self)
        if self.hp <= 0.5*self.max_hp:
            village.turn_yellow(self)
        if self.hp <= 0.2*self.max_hp:
            village.turn_red(self)
        if self.hp < 0:
            village.remove_building(self)
                    

# hut class
class Hut(Building):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2, 300)
        self.building_array = []
        self.ascii()
        

    # import hut from hut.txt
    def ascii(self):
        file = open('src/hut.txt', 'r')
        for line in file:
            self.building_array.append(line)
        file.close()

# wall class
class Wall(Building):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, 200)
        self.building_array = []
        self.ascii()

    # import wall from wall.txt
    def ascii(self):
        file = open('src/wall.txt', 'r')
        for line in file:
            self.building_array.append(line)
        file.close()

