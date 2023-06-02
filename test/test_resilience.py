import unittest
from unittest.mock import patch
from character.character import Character
from skill.defensive.defensive_skill import DefensiveSkill
from skill.defensive.resilience import Resilience


class TestResilience(unittest.TestCase):

    def setUp(self):
        self.defender = Character("defender", 80, 60, 70, 60, 15)
        self.skill = Resilience('Resilience')
        self.attack_damage = 10  # You can change this based on your test case

    @patch('skill.defensive.resilience.random.randrange')
    def test_execute(self, mock_randrange):
        initial_health = self.defender.health

        # Case 1: No resilience applied
        mock_randrange.return_value = 21  # Greater than 20, so no resilience
        self.skill.execute(self.defender, self.attack_damage)
        self.assertEqual(self.defender.health, initial_health - self.attack_damage)

        # Resetting health for next test case
        self.defender.health = initial_health

        # Case 2: Resilience applied
        mock_randrange.return_value = 10  # Less than or equal to 20, so resilience is applied
        self.skill.execute(self.defender, self.attack_damage)
        self.assertEqual(self.defender.health, initial_health - self.attack_damage / 2)

        # Resetting health for next test case
        self.defender.health = initial_health

        # Case 3: Resilience not applied because it was used in the last turn
        self.skill.used_last_turn = True
        mock_randrange.return_value = 10  # Less than or equal to 20, but used in the last turn
        self.skill.execute(self.defender, self.attack_damage)
        self.assertEqual(self.defender.health, initial_health - self.attack_damage)


if __name__ == '__main__':
    unittest.main()
