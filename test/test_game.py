import unittest
from unittest.mock import MagicMock, patch

from game import Game
from character.hero import Hero
from character.villain import Villain
from skill.skill_type_enum import SkillTypeEnum


class TestGame(unittest.TestCase):

    @patch('character.character.Character.attack', return_value=10)
    @patch('character.character.Character.defend')
    @patch('skill_factory.SkillFactory.create_skill')
    def test_game_run(self, mock_create_skill, mock_defend, mock_attack):
        # Creating a Hero and Villain
        hero = Hero("Hero", 100, 70, 50, 40, 30)
        villain = Villain("Villain", 90, 70, 40, 50, 25)

        # Creating a Game
        game = Game(hero, villain)

        # Mocking the skill factory to return a MagicMock (to avoid dealing with actual skills)
        mock_skill = MagicMock()
        mock_create_skill.return_value = mock_skill

        # Running the game
        game.start()

        # Ensuring that the mocks were called the correct number of times
        self.assertEqual(mock_defend.call_count, game.max_turns)
        self.assertEqual(mock_attack.call_count, game.max_turns)
        self.assertEqual(mock_create_skill.call_count, 2)

    @patch('character.character.Character.attack', return_value=50)
    @patch('character.character.Character.defend')
    @patch('skill_factory.SkillFactory.create_skill')
    def test_hero_wins(self, mock_create_skill, mock_defend, mock_attack):
        # Creating a Hero with normal health and a Villain with low health
        hero = Hero("Hero", 100, 70, 50, 40, 30)
        villain = Villain("Villain", 10, 60, 40, 50, 25)  # Low health for villain

        # Creating a Game
        game = Game(hero, villain)

        # Mocking the skill factory to return a MagicMock (to avoid dealing with actual skills)
        mock_skill = MagicMock()
        mock_create_skill.return_value = mock_skill

        # Running the game
        with patch('builtins.print') as mocked_print:
            game.start()

        # Ensuring that the game ends with hero's win
        mocked_print.assert_called_with("The hero wins!")

    @patch('character.character.Character.attack', return_value=50)
    @patch('character.character.Character.defend')
    @patch('skill_factory.SkillFactory.create_skill')
    def test_villain_wins(self, mock_create_skill, mock_defend, mock_attack):
        # Creating a Hero with low health and a Villain with normal health
        hero = Hero("Hero", 10, 60, 35, 40, 20)  # Low properties for hero
        villain = Villain("Villain", 100, 70, 40, 50, 25)

        # Creating a Game
        game = Game(hero, villain)

        # Mocking the skill factory to return a MagicMock (to avoid dealing with actual skills)
        mock_skill = MagicMock()
        mock_create_skill.return_value = mock_skill

        # Running the game
        with patch('builtins.print') as mocked_print:
            game.start()

        # Ensuring that the game ends with villain's win
        mocked_print.assert_called_with("The villain wins!")

    @patch('game.Villain')
    @patch('game.Hero')
    def test_game_draw(self, MockHero, MockVillain):
        # Both characters have enough health to survive the maximum number of turns
        mock_hero = MockHero()
        mock_hero.health = 200
        mock_hero.speed = 50  # Define a return value for speed
        mock_hero.luck = 20  # Define a return value for luck
        mock_hero.hero = True  # Define a return value for hero
        mock_villain = MockVillain()
        mock_villain.health = 200
        mock_villain.speed = 50  # Define a return value for speed
        mock_villain.luck = 20  # Define a return value for luck
        mock_villain.hero = False  # Define a return value for hero

        # They inflict some damage but not enough to defeat the other
        mock_hero.calculate_damage.return_value = 5
        mock_hero.attack.return_value = 5
        mock_villain.calculate_damage.return_value = 5
        mock_villain.attack.return_value = 5

        game = Game(mock_hero, mock_villain, max_turns=20)

        with patch('game.print') as mocked_print:
            game.start()
            # The last print statement should announce a draw
            mocked_print.assert_any_call("It's a draw!")

        # Both characters should still have some health left
        self.assertTrue(mock_hero.health > 0)
        self.assertTrue(mock_villain.health > 0)


if __name__ == '__main__':
    unittest.main()
