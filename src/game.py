from character.hero import Hero
from character.villain import Villain
from skill.skill_type_enum import SkillTypeEnum
from skill_factory import SkillFactory


class Game:
    def __init__(self, hero: Hero, villain: Villain, max_turns=20):
        self.hero = hero
        self.villain = villain
        self.max_turns = max_turns

    def start(self):
        turn_count = 0
        skill_factory = SkillFactory()
        offensive_skill = skill_factory.create_skill(SkillTypeEnum.CRITICAL_STRIKE)
        defensive_skill = skill_factory.create_skill(SkillTypeEnum.RESILIENCE)

        # Determine the first attacker based on the speed and luck
        if self.check_if_hero_goes_first():
            attacker, defender = self.hero, self.villain
        else:
            attacker, defender = self.villain, self.hero

        while self.check_if_game_can_continue(turn_count):

            # Stop the game as soon as the health of one of them reaches 0
            if self.should_stop_the_game():
                break

            # Set the attack or defence skill for this round (the current 'strategy')
            # In the future this logic could be separated as it becomes more complex
            # For example if villains will be able to use skills as well
            # or if the hero will have multiple skills with different cool downs
            if attacker.hero:
                attacker.set_skill(offensive_skill)
            if defender.hero:
                defender.set_skill(defensive_skill)

            # The attacker attacks and the defender defends
            expected_damage = attacker.attack(defender)
            defender.defend(expected_damage)

            # Swap roles
            attacker, defender = defender, attacker

            turn_count += 1

        # Determine the winner
        self.determine_the_winner()

    def check_if_hero_goes_first(self):
        return self.hero.speed > self.villain.speed \
            or (self.hero.speed == self.villain.speed and self.hero.luck > self.villain.luck)

    def check_if_game_can_continue(self, turn_count):
        return turn_count < self.max_turns \
            and self.hero.health > 0 \
            and self.villain.health > 0

    def should_stop_the_game(self):
        return self.hero.health <= 0 or self.villain.health <= 0

    def determine_the_winner(self):
        if self.hero.health > self.villain.health:
            print("The hero wins!")
        elif self.villain.health > self.hero.health:
            print("The villain wins!")
        else:
            print("It's a draw!")
