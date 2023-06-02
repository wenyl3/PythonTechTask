from character.character_type_enum import CharacterTypeEnum
from character_factory import CharacterFactory
from game import Game

if __name__ == '__main__':
    character_factory = CharacterFactory()
    hero = character_factory.create_character(CharacterTypeEnum.HERO, "Ghost Rider")
    print(str(hero))
    villain = character_factory.create_character(CharacterTypeEnum.VILLAIN, "Joker")
    print(str(villain))

    print("____________________________")
    game = Game(hero, villain, 20)
    game.start()
