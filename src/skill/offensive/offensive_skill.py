from abc import abstractmethod

from skill.skill import Skill


class OffensiveSkill(Skill):

    @abstractmethod
    def execute(self, attacker, defender):
        pass
