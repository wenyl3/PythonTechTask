import unittest
from unittest.mock import patch
from character.character import Character
from skill.offensive.offensive_skill import OffensiveSkill
from skill.defensive.defensive_skill import DefensiveSkill
from skill.offensive.critical_strike import CriticalStrike
from skill.defensive.resilience import Resilience


class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.character1 = Character("Hero", 100, 80, 50, 40, 25)
        self.character2 = Character("Villain", 90, 70, 45, 40, 30)

    def test_calculate_damage(self):
        expected_damage = self.character1.strength - self.character2.defence
        actual_damage = self.character1.calculate_damage(self.character2)
        self.assertEqual(actual_damage, expected_damage)

    @patch('character.character.Character.calculate_damage', return_value=30)
    @patch('character.character.random.randrange')
    def test_attack(self, mock_randrange, mock_damage):
        # Test attack without any skill
        mock_randrange.return_value = 15
        damage = self.character1.attack(self.character2)
        self.assertEqual(damage, mock_damage.return_value)

    @patch('character.character.Character.calculate_damage', return_value=30)
    @patch('character.character.random.randrange')
    def test_attack_with_skill(self, mock_randrange, mock_damage):
        # Test attack with an offensive skill
        mock_randrange.side_effect = [5, 15]
        self.character1.set_skill(CriticalStrike('Critical Strike'))
        damage = self.character1.attack(self.character2)
        self.assertEqual(damage, mock_damage.return_value * 2)

    def test_defend(self):
        # Test defend without any skill
        self.character2.defend(30)
        self.assertEqual(self.character2.health, 90 - 30)

    @patch('character.character.random.randrange')
    def test_defend_with_skill(self, mock_randrange):
        # # Test defend with a defensive skill
        mock_randrange.return_value = 15
        self.character2.set_skill(Resilience('Resilience'))
        self.character2.defend(30)
        self.assertEqual(self.character2.health, 90 - 30 / 2)


if __name__ == '__main__':
    unittest.main()
