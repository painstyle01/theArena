"""
Equipments for characters
"""
import random

weap_name = ["Axe", "Mace", "Dual Swords", "Sword", "Rapier", "Bow"]
armor_name = ['Dragon Chestplate', "Frostiron Chestplate",
              "Enchanted Leather Chestplate", "Magic Wood Chestplate"]
trinket_name = ["Ring", "Necklace", "Earring", "Cloak", "Hood"]

cool_words = ['of Doom', "of Revenge", "of the King",
              'filled with magic', "of Rivia", "of Shadows", "of Power",
              "of Tarrasque"]


class Weapon:
    """
    Weapon class. Main stats - ATK and CRIT
    """
    def __init__(self):
        self.atk = random.randint(1, 20)
        self.hp = random.randint(10, 20)
        self.evasion = random.randint(1, 3)
        self.crit = random.randint(1, 5)
        self.name = random.choice(weap_name) + " " + random.choice(cool_words)


class Armor:
    """
    Armor class. Main stat - HP
    """
    def __init__(self):
        self.atk = random.randint(1, 3)
        self.hp = random.randint(200, 300)
        self.evasion = random.randint(1, 3)
        self.crit = random.randint(1, 3)
        self.name = random.choice(armor_name) + " " + random.choice(cool_words)


class Trinket:
    """
    Trinket class. Small boost to all stats.
    """
    def __init__(self):
        self.atk = random.randint(1, 7)
        self.hp = random.randint(50, 100)
        self.evasion = random.randint(1, 10)
        self.crit = random.randint(1, 5)
        self.name = random.choice(trinket_name) + " " + random.choice(cool_words)
