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

# Define specific character classes with different types and attacks
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, "Warrior", 100)
    
    def attack(self, target):
        attackDamage = random.randint(10, 20)
        target.takeDamage(attackDamage)
        print(f"{self.name} attacked {target.name} with a sword for {attackDamage} damage!")
    
    def defend(self):
        defenseBonus = random.randint(5, 10)
        self.newHP += defenseBonus
        if self.newHP > self.maxHP:
            self.newHP = self.maxHP
        print(f"{self.name} defended and restored {defenseBonus} health.")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Mage", 80)
    
    def attack(self, target):
        spellDamage = random.randint(15, 25)
        target.takeDamage(spellDamage)
        print(f"{self.name} cast a spell on {target.name} for {spellDamage} damage!")
    
    def defend(self):
        defenseBonus = random.randint(3, 8)
        self.newHP += defenseBonus
        if self.newHP > self.maxHP:
            self.newHP = self.maxHP
        print(f"{self.name} used a protective shield and restored {defenseBonus} health.")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "Archer", 90)
    
    def attack(self, target):
        arrowDamage = random.randint(12, 18)
        target.takeDamage(arrowDamage)
        print(f"{self.name} shot an arrow at {target.name} for {arrowDamage} damage!")
    
    def defend(self):
        defenseBonus = random.randint(2, 5)
        self.newHP += defenseBonus
        if self.newHP > self.maxHP:
            self.newHP = self.maxHP
        print(f"{self.name} took cover and restored {defenseBonus} health.")
