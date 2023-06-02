from abc import abstractmethod

from skill.skill import Skill


class DefensiveSkill(Skill):

    @abstractmethod
    def execute(self, defender, attack_damage):
        pass
