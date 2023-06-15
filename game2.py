import random
from functools import partial

# Define the base class for characters
class Character:
    def __init__(self, name, type, maxHP):
        self.name = name
        self.type = type
        self.maxHP = maxHP
        self.newHP = maxHP
    
    def attack(self, target):
        pass  # Implemented in derived classes
    
    def defend(self):
        pass  # Implemented in derived classes
    
    def takeDamage(self, damage):
        self.newHP -= damage
    
    def isKnockedOut(self):
        return self.newHP <= 0
