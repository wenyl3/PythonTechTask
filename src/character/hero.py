from character.character import Character


class Hero(Character):

    def __init__(self, name, health, strength, defence, speed, luck):
        super().__init__(name, health, strength, defence, speed, luck)
        self.hero = True
