import random

from skill.offensive.offensive_skill import OffensiveSkill
from skill.defensive.defensive_skill import DefensiveSkill


class Character:
    def __init__(self, name, health, strength, defence, speed, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck

        # Field added to check if a character is a hero and can use skills during the game
        # In the future this could be used when assigning skills (strategies) to heroes and villains
        self.hero = None

        self.skill = None

    def set_skill(self, skill):
        self.skill = skill

    def attack(self, defender):
        print(f"{self.name} is attacking {defender.name}")
        if self.skill and isinstance(self.skill, OffensiveSkill):
            # Calculate the damage expected from a skill
            print(f"{self.name} is using skill {self.skill.name}")
            return self.skill.execute(self, defender)
        else:
            # Calculate the damage expected from a normal attack
            returned_damage = self.calculate_damage(defender)

            # Regular attack if no skill is activated
            if random.randrange(0, 100) <= defender.luck:
                return returned_damage
            else:
                print(f"{defender.name} got lucky and avoided the attack!")
                return 0

    def defend(self, damage):
        if damage == 0:
            return
        if self.skill and isinstance(self.skill, DefensiveSkill):
            # Take into account the effect of a defensive skill
            self.skill.execute(self, damage)
        else:
            # By default, just take the damage
            self.health -= damage
            print(f"{self.name} is defending and taking {damage} damage (health left: {self.health})")

    def calculate_damage(self, defender):
        # Calculate the base damage of the attack
        return self.strength - defender.defence

    def __str__(self):
        return (f"Character '{self.name}':\n"
                f"\tHealth: {self.health}\n"
                f"\tStrength: {self.strength}\n"
                f"\tDefence: {self.defence}\n"
                f"\tSpeed: {self.speed}\n"
                f"\tLuck: {self.luck}\n"
                f"\tSkill: {self.skill.name if self.skill else 'None'}")
