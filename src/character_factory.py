from character.hero import Hero
from character.villain import Villain
from character.character_type_enum import CharacterTypeEnum
from random import randrange


class CharacterFactory:

    def create_character(self, type, name):
        if type == CharacterTypeEnum.HERO:
            return Hero(
                name=name,
                health=randrange(70, 100),
                strength=randrange(70, 80),
                defence=randrange(45, 55),
                speed=randrange(40, 50),
                luck=randrange(10, 30))
        elif type == CharacterTypeEnum.VILLAIN:
            return Villain(
                name=name,
                health=randrange(60, 90),
                strength=randrange(60, 90),
                defence=randrange(40, 60),
                speed=randrange(40, 60),
                luck=randrange(25, 40))
        else:
            raise ValueError("Invalid type of character provided")
