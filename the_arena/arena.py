"""
Arena module. Used for all battles and modes.
"""
import random
import logging
from character import Hero

logging.basicConfig(filename='app.log', filemode='w',
                    format='[%(asctime)s]%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class Arena:
    """
    Arena class. Creates "instance" of arena. Controls several play modes.
    """

    def __init__(self, hero1: Hero, hero2: Hero):
        self.player = hero1
        self.cpu = hero2

    def player_move(self):
        """
        Computing player turn.
        Firstly, if CPU evaded, then if hit critical.
        :return: None
        """
        if random.randint(1, 100) > self.cpu.evasion:
            logging.info("Player hit the CPU. Calculating damage...")
            if random.randint(1, 100) < self.player.crit:
                logging.info("Player hit critical hit! CPU damaged for %s HP", self.cpu.atk * 2)
                self.cpu.hp -= self.player.atk * 2
            else:
                logging.info("Player hit simple hit. CPU damaged for %s HP", self.cpu.atk)
                self.cpu.hp -= self.player.atk
        else:
            logging.info("CPU dodged the hit.")

    def cpu_move(self):
        """
        Calculating CPU move.
        :return:
        """
        if random.randint(1, 100) > self.player.evasion:
            logging.info("CPU hit the Player. Calculating damage...")
            if random.randint(1, 100) < self.cpu.crit:
                logging.info("CPU hit critical hit! Player damaged for %s HP", self.player.atk * 2)
                self.player.hp -= self.cpu.atk * 2
            else:
                logging.info("CPU hit simple hit. Player damaged for %s HP", self.player.atk)
                self.player.hp -= self.cpu.atk

    def fight_till_death(self) -> str:
        """
        Begin the game until one of the heroes got 0 HP or less.
        :return: Loser name
        """
        """Test variant 1."""

        """
        while self.player.hp > 0 | self.cpu.hp > 0:
            logging.info("PLAYER HP - %s, CPU HP - %s", self.player.hp, self.cpu.hp)
            self.player_move()
            self.cpu_move()
        if self.player.hp < 0:
            return self.player.hero_name
        if self.cpu.hp < 0:
            return self.cpu.hero_name
        """

        # Todo Fix while loop
        while True:
            if self.player.hp > 0:
                if self.cpu.hp > 0:
                    logging.info("PLAYER HP - %s, CPU HP - %s", self.player.hp, self.cpu.hp)
                    self.player_move()
                    self.cpu_move()
                else:
                    break
            else:
                break
        if self.player.hp < 0:
            return self.player.hero_name
        elif self.cpu.hp < 0:
            return self.cpu.hero_name
