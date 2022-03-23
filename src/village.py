# class for village

import numpy as np
import colorama as c

class Village:
    # function to initialise village
    def __init__(self,x,y):
        self.width  = x
        self.length = y
        self.front_grid = []
        self.back_grid = []
        self.buildings = []
        self.troops = []
        self.min_dist = []
        self.direction = []
        for i in range(self.width):
            self.front_grid.append([])
            self.back_grid.append([])
            for j in range(self.length):
                self.front_grid[i].append(c.Back.LIGHTGREEN_EX + "  " + c.Style.RESET_ALL)
                self.back_grid[i].append(0)




    # function to print village
    def display(self):
        # print('\033[1;1H', end="")
        print('\n\n\n\t\t\t',end='')
        print('▒'*(self.width*2+4))
        for i in range(self.length):
            print('\t\t\t▒▒',end='')
            for j in range(self.width):
                print(self.front_grid[i][j],end='')
            print('▒▒')
        print('\t\t\t',end='')
        print('▒'*(self.width*2+4))
        print('\n\n\n',end='')
    
    # function to add building to village
    def add_building(self,building):
        for i in range(building.width):
            for j in range(building.length):
                self.front_grid[building.x+i][building.y+j] = c.Back.GREEN +  building.building_array[i][2*j] + building.building_array[i][2*j+1] +c.Style.RESET_ALL
                self.back_grid[building.x+i][building.y+j] = building.id
        self.buildings.append(building)
        self.min_dist = self.make_grid()

    # function to turn building green
    def turn_green(self,building):
        for i in range(building.width):
            for j in range(building.length):
                self.front_grid[building.x+i][building.y+j] = c.Back.GREEN +  building.building_array[i][2*j] + building.building_array[i][2*j+1] +c.Style.RESET_ALL
                self.back_grid[building.x+i][building.y+j] = building.id

    # function to turn building yellow
    def turn_yellow(self,building):
        for i in range(building.width):
            for j in range(building.length):
                self.front_grid[building.x+i][building.y+j] = c.Back.YELLOW +  building.building_array[i][2*j] + building.building_array[i][2*j+1] +c.Style.RESET_ALL
                self.back_grid[building.x+i][building.y+j] = building.id

    # function to turn building red
    def turn_red(self,building):
        for i in range(building.width):
            for j in range(building.length):
                self.front_grid[building.x+i][building.y+j] = c.Back.RED +  building.building_array[i][2*j] + building.building_array[i][2*j+1] +c.Style.RESET_ALL
                self.back_grid[building.x+i][building.y+j] = building.id

    # function to turn building white
    def turn_white(self,building):
        for i in range(building.width):
            for j in range(building.length):
                self.front_grid[building.x+i][building.y+j] = c.Back.BLUE +  building.building_array[i][2*j] + building.building_array[i][2*j+1] +c.Style.RESET_ALL
                self.back_grid[building.x+i][building.y+j] = building.id

    # funtion to remove building
    def remove_building(self,building):
        for i in range(building.width):
            for j in range(building.length):
                self.front_grid[building.x+i][building.y+j] = c.Back.LIGHTGREEN_EX + "  " + c.Style.RESET_ALL
                self.back_grid[building.x+i][building.y+j] = 0

                
        # remove building from list
        for i in range(len(self.buildings)):
            if self.buildings[i].id == building.id:
                self.buildings.pop(i)
                break

        self.min_dist = self.make_grid()

    # function to add troop
    def add_troop(self,troop):
        self.front_grid[troop.x][troop.y] = c.Back.LIGHTBLUE_EX + troop.ascii + c.Style.RESET_ALL
        self.back_grid[troop.x][troop.y] = troop.id
        self.troops.append(troop)

    
    # function to remove troop
    def remove_troop(self,troop):
        self.front_grid[troop.x][troop.y] = c.Back.LIGHTGREEN_EX + "  " + c.Style.RESET_ALL
        self.back_grid[troop.x][troop.y] = 0
        for i in range(len(self.troops)):
            if self.troops[i].id == troop.id:
                self.troops.pop(i)
                break


    # funtinon to get building by building id
    def get_building(self,x,y):
        id = self.back_grid[x][y]
        for i in range(len(self.buildings)):
            if self.buildings[i].id == id:
                return self.buildings[i]
        return None

    # function to get troop by troop id
    def get_troop(self,x,y):
        id = self.back_grid[x][y]
        for i in range(len(self.troops)):
            if self.troops[i].id == id:
                return self.troops[i]
        return None

    # function to make a grid which stores direction to closest building
    def make_grid(self):
        grid = []
        self.direction = []
        for i in range(self.width):
            grid.append([])
            self.direction.append([])
            for j in range(self.length):
                grid[i].append(5000)
                self.direction[i].append((0,0))          
        for x in range(self.width):
            for y in range(self.length):
                if self.back_grid[x][y] <= 0:
                    continue
                if self.back_grid[x][y] >  8:
                    continue
                for i in range(self.width):
                    for j in range(self.length):
                        if grid[i][j] > abs(x-i)+abs(y-j):
                            grid[i][j] = abs(x-i)+abs(y-j)
                            self.direction[i][j] = ((x-i,y-j))
        return grid

    # function to check game end
    def check_end(self):
        flag = 1
        for i in range(len(self.buildings)):
            if self.buildings[i].id <= 8:
                flag = 0
                break
        if flag == 1 :
            return 1
        if len(self.troops) == 0 :
            return 2
        return 0
            








