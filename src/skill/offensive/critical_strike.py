import random

from character.character import Character
from skill.offensive.offensive_skill import OffensiveSkill


class CriticalStrike(OffensiveSkill):

    # Logic for critical strike
    def execute(self, attacker: Character, defender: Character):

        # Calculate the damage expected from a normal attack
        returned_damage = attacker.calculate_damage(defender)
        if random.randrange(0, 100) <= 10:
            if random.randrange(0, 100) <= 1:
                # Strike three times
                returned_damage *= 3
            else:
                # Strike two times
                returned_damage *= 2

            return returned_damage
        else:
            # Normal attack
            return returned_damage
