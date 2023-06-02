import unittest
from unittest.mock import patch
from character.character import Character
from skill.offensive.offensive_skill import OffensiveSkill
from skill.offensive.critical_strike import CriticalStrike


class TestCriticalStrike(unittest.TestCase):

    def setUp(self):
        self.attacker = Character("attacker", 80, 60, 70, 60, 15)
        self.defender = Character("defender", 80, 60, 70, 60, 15)
        self.skill = CriticalStrike("Critical Strike")

    @patch('random.randrange')
    def test_execute(self, mock_randrange):
        normal_damage = self.attacker.calculate_damage(self.defender)

        # Case 1: Normal attack
        mock_randrange.return_value = 11
        self.assertEqual(self.skill.execute(self.attacker, self.defender), normal_damage)

        # Case 2: Double damage
        mock_randrange.side_effect = [5, 2]  # first roll <= 10 (activate skill), second roll > 1 (double damage)
        self.assertEqual(self.skill.execute(self.attacker, self.defender), 2 * normal_damage)

        # Case 3: Triple damage
        mock_randrange.side_effect = [5, 0]  # first roll <= 10 (activate skill), second roll <= 1 (triple damage)
        self.assertEqual(self.skill.execute(self.attacker, self.defender), 3 * normal_damage)


if __name__ == '__main__':
    unittest.main()
