from skill.offensive.critical_strike import CriticalStrike
from skill.defensive.resilience import Resilience
from skill.skill_type_enum import SkillTypeEnum


class SkillFactory:

    def create_skill(self, type):
        if type == SkillTypeEnum.CRITICAL_STRIKE:
            return CriticalStrike("Critical Strike")
        elif type == SkillTypeEnum.RESILIENCE:
            return Resilience("Resilience")
        else:
            raise ValueError("Invalid type of skill provided")
