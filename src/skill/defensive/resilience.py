import random

from character.character import Character
from skill.defensive.defensive_skill import DefensiveSkill


class Resilience(DefensiveSkill):

    def __init__(self, name):
        super().__init__(name)
        self.used_last_turn = False
        self.chance_to_activate = 20

    # Logic for resilience
    def execute(self, defender: Character, attack_damage):
        if self.used_last_turn is False and random.randrange(0, 100) <= self.chance_to_activate:
            defender.health -= (attack_damage / 2)
            print(f"{defender.name} is defending with resilience "
                  f"and taking {attack_damage / 2} damage (health left: {defender.health})")
        else:
            defender.health -= attack_damage
            print(f"{defender.name} is defending and taking {attack_damage} damage (health left: {defender.health})")
