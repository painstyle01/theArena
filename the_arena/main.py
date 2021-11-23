"""
Main game executable script.
"""
import colorama

from arena import Arena
from character import Hero
from equipment import Weapon, Trinket, Armor

colorama.init(autoreset=True)

if __name__ == '__main__':
    player_name = input("Enter your hero name [leave blank for random name]: ")

    if player_name == "":
        hero1 = Hero()
    else:
        hero1 = Hero(player_name)

    hero2 = Hero("Arthas Menethil, The Lich King")

    cpu_arm = Armor()
    cpu_weap = Weapon()
    cpu_tri = Trinket()

    hero2.equip(cpu_weap)
    hero2.equip(cpu_arm)
    hero2.equip(cpu_tri)

    print(
        f"{colorama.Fore.BLACK}{colorama.Back.WHITE} You woke up in strange hall with guards. "
        f"You got a piece of paper in your hand:")
    print(f"{colorama.Fore.CYAN}{hero1.hero_name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{hero1.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{hero1.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {hero1.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{hero1.evasion}\n")

    print(
        f"{colorama.Fore.BLUE}[The King] Welcome to the Arena, "
        f"{colorama.Fore.GREEN}{hero1.hero_name}{colorama.Fore.BLUE}.\n"
        f"Since {colorama.Fore.LIGHTRED_EX}{hero2.hero_name}{colorama.Fore.BLUE} "
        f"ready for fight, {hero1.hero_name} "
        f"get you equipment.")
    print(f"{colorama.Back.WHITE}{colorama.Fore.BLACK}"
          f"The door opens, and Blacksmith enters the room.")
    print(f"{colorama.Fore.BLUE}[Blacksmith] Hey'ya. "
          f"Need some items to get rid of that guy? Here, take a look.")
    arm1, arm2, arm3 = Armor(), Armor(), Armor()
    weap1, weap2, weap3 = Weapon(), Weapon(), Weapon()
    tri1, tri2, tri3 = Trinket(), Trinket(), Trinket()
    print('[Blacksmith] Take a look at that weapon.')
    print('1)')
    print(f"{colorama.Fore.CYAN}{weap1.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{weap1.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{weap1.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {weap1.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{weap1.evasion}\n")
    print('2)')
    print(f"{colorama.Fore.CYAN}{weap2.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{weap2.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{weap2.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {weap2.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{weap2.evasion}\n")
    print('3)')
    print(f"{colorama.Fore.CYAN}{weap3.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{weap3.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{weap3.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {weap3.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{weap3.evasion}\n")
    choice = input("[Blacksmith] Which one will you use? [1, 2, 3] ")
    if int(choice) == 1:
        hero1.equip(weap1)
    if int(choice) == 2:
        hero1.equip(weap2)
    if int(choice) == 3:
        hero1.equip(weap3)

    print('[Blacksmith] Take a look at my best armor.')
    print('1)')
    print(f"{colorama.Fore.CYAN}{arm1.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{arm1.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{arm1.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {arm1.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{arm1.evasion}\n")
    print('2)')
    print(f"{colorama.Fore.CYAN}{arm2.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{arm2.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{arm2.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {arm2.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{arm2.evasion}\n")
    print('3)')
    print(f"{colorama.Fore.CYAN}{arm3.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{arm3.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{arm3.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {arm3.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{arm3.evasion}\n")
    choice = input("[Blacksmith] Which one will you use? [1, 2, 3] ")
    if int(choice) == 1:
        hero1.equip(arm1)
    if int(choice) == 2:
        hero1.equip(arm2)
    if int(choice) == 3:
        hero1.equip(arm3)

    print('[Blacksmith] My son got some "lucky amulets" for you. Select one of them..')
    print('1)')
    print(f"{colorama.Fore.CYAN}{tri1.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{tri1.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{tri1.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {tri1.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{tri1.evasion}\n")
    print('2)')
    print(f"{colorama.Fore.CYAN}{tri2.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{tri2.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{tri2.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {tri2.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{tri2.evasion}\n")
    print('3)')
    print(f"{colorama.Fore.CYAN}{tri3.name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{tri3.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{tri3.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {tri3.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{tri3.evasion}\n")
    choice = input("[Blacksmith] Which one will you use? [1, 2, 3] ")
    if int(choice) == 1:
        hero1.equip(tri1)
    if int(choice) == 2:
        hero1.equip(tri2)
    if int(choice) == 3:
        hero1.equip(tri3)

    print(f"\n{colorama.Fore.BLACK}{colorama.Back.WHITE} "
          f"Suddenly, paper in your hand starts to shake:")
    print(f"{colorama.Fore.CYAN}{hero1.hero_name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{hero1.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{hero1.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {hero1.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{hero1.evasion}\n")
    print(
        f"{colorama.Fore.BLACK}{colorama.Back.WHITE}"
        f"At the second, you appears in Arena. You can see the enemy's info.")
    print(f"{colorama.Fore.CYAN}{hero2.hero_name}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.RED}❤️{hero2.hp}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.LIGHTGREEN_EX}⚔️{hero2.atk}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.YELLOW}🩸️   {hero2.crit}\n"
          f"{colorama.Fore.RESET}{colorama.Fore.MAGENTA}⚡️{hero2.evasion}\n")
    arena = Arena(hero1, hero2)

    print('Let the battle begin!')
    print(f"Today we lost {arena.fight_till_death()}.")