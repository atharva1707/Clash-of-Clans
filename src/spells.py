import numpy as np
import colorama as c

# spell class
class Spell:
    def __init__(self,speed_factor, damage_factor, heal_factor):
        self.activated = 0 
        self.speed_factor = speed_factor
        self.damage_factor = damage_factor
        self.heal_factor = heal_factor

    def activate(self, troop):
        self.activated = 1

class Heal(Spell):
    def __init__(self):
        super().__init__(1,1,1.5)

    def activate(self, King, Barbarians):
        self.activated = 1
        King.hp = min(King.max_hp, King.hp * self.heal_factor)
        for troop in Barbarians:
            troop.hp = min(troop.max_hp, troop.hp * self.heal_factor)

    def deactivate(self):
        self.activated = 0


class Rage(Spell):
    def __init__(self):
        super().__init__(2,2,1)

    def activate(self, King, Barbarians):
        if(self.activated):
            return
        self.activated = 1
        King.damage = King.damage * self.damage_factor
        for troop in Barbarians:
            troop.damage = troop.damage * self.damage_factor

    def deactivate(self):
        self.activated = 0
        