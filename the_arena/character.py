"""
Character module
"""
import random
import names

class Hero:
    """
    Hero instance. Generates with random stats.
    """
    def __init__(self, name=names.get_full_name()):
        self.atk = random.randint(1, 10)
        self.hp = random.randint(100, 200)
        self.evasion = random.randint(1, 20)
        self.crit = random.randint(1, 5)
        self.hero_name = name

    def equip(self, item):
        """
        Adds stats from item for hero.
        :param item: Any item instance
        """
        self.atk = self.atk + item.atk
        self.hp = self.hp + item.hp
        self.evasion = self.evasion + item.evasion
        self.crit = self.crit + item.crit
