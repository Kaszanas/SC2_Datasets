from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class Stats(TrackerEvent):
    """
    Stats holds specific fields on the economy of a player and is used in PlayerStats event.

    :param foodMade: Specifies the amount of supply that a player created.\
    This is a limit of units that can be made.
    :type foodMade: int
    :param foodUsed: Specifies how much of the supply is used for units.
    :type foodUsed: int
    :param mineralsCollectionRate: Specifies the collection rate of minerals.\
    Most likely per minute.
    :type mineralsCollectionRate: int
    :param mineralsCurrent: Specifies how much minerals the player has in his "bank".
    :type mineralsCurrent: int
    :param mineralsFriendlyFireArmy: Specifies how much minerals were lost\
    in friendly fire on army units.
    :type mineralsFriendlyFireArmy: int
    :param mineralsFriendlyFireEconomy: Specifies how much minerals were lost\
    in friendly fire on economy.
    :type mineralsFriendlyFireEconomy: int
    :param mineralsFriendlyFireTechnology: Specifies how much minerals were lost\
    in friendly fire on technology.
    :type mineralsFriendlyFireTechnology: int
    :param mineralsKilledArmy: Specifies how much minerals a player killed\
    in his oponent's army.
    :type mineralsKilledArmy: int
    :param mineralsKilledEconomy: Specifies how much minerals player killed\
    in his oponents economy.
    :type mineralsKilledEconomy: int
    :param mineralsKilledTechnology: Specifies how much minerals player killed\
    in his oponents technology.
    :type mineralsKilledTechnology: int
    :param mineralsLostArmy: Specifies how much minerals player lost in his army.
    :type mineralsLostArmy: int
    :param mineralsLostEconomy: Specifies how much minerals player lost in his economy.
    :type mineralsLostEconomy: int
    :param mineralsLostTechnology: Specifies how much minerals player lost in his technology.
    :type mineralsLostTechnology: int
    :param mineralsUsedActiveForces: Specifies how much minerals does the player\
    have in his active forces.
    :type mineralsUsedActiveForces: int
    :param mineralsUsedCurrentArmy: Specifies how much minerals does the player\
    have in his army.
    :type mineralsUsedCurrentArmy: int
    :param mineralsUsedCurrentEconomy: Specifies how much minerals does the player\
    have in his economical units and structures.
    :type mineralsUsedCurrentEconomy: int
    :param mineralsUsedCurrentTechnology: Specifies how much minerals does the player\
    have in his technological units, upgrades, and structures.
    :type mineralsUsedCurrentTechnology: int
    :param mineralsUsedInProgressArmy: Specifies how much minerals does the player\
    have in army that is currently being built.
    :type mineralsUsedInProgressArmy: int
    :param mineralsUsedInProgressEconomy: Specifies how much minerals does the player\
    have in economy that is currently being built.
    :type mineralsUsedInProgressEconomy: int
    :param mineralsUsedInProgressTechnology: Specifies how much minerals does\
    the player have in technology that is currently being built.
    :type mineralsUsedInProgressTechnology: int
    :param vespeneCollectionRate: Specifies what is the vespene collection rate.\
    Most likely per minute.
    :type vespeneCollectionRate: int
    :param vespeneCurrent: Specifies the amount of vespene gas that the user has\
    in his "bank".
    :type vespeneCurrent: int
    :param vespeneFriendlyFireArmy: Specifies how much vespene was lost in friendly fire\
    on army units.
    :type vespeneFriendlyFireArmy: int
    :param vespeneFriendlyFireEconomy: Specifies how much vespene was lost\
    in friendly fire on economy.
    :type vespeneFriendlyFireEconomy: int
    :param vespeneFriendlyFireTechnology: Specifies how much vespene was lost\
    in friendly fire on technology.
    :type vespeneFriendlyFireTechnology: int
    :param vespeneKilledArmy: Specifies how much vespene player killed in his oponents army.
    :type vespeneKilledArmy: int
    :param vespeneKilledEconomy: Specifies how much vespene player killed\
    in his oponents economy.
    :type vespeneKilledEconomy: int
    :param vespeneKilledTechnology: Specifies how much vespene player killed\
    in his oponents technology.
    :type vespeneKilledTechnology: int
    :param vespeneLostArmy: Specifies how much vespene player lost in his army.
    :type vespeneLostArmy: int
    :param vespeneLostEconomy: Specifies how much vespene player lost in his economy.
    :type vespeneLostEconomy: int
    :param vespeneLostTechnology: Specifies how much vespene player lost in his technology.
    :type vespeneLostTechnology: int
    :param vespeneUsedActiveForces: Specifies how much vespene does the player\
    have in his active forces.
    :type vespeneUsedActiveForces: int
    :param vespeneUsedCurrentArmy: Specifies how much vespene does the player\
    have in his army.
    :type vespeneUsedCurrentArmy: int
    :param vespeneUsedCurrentEconomy: Specifies how much vespene does the player\
    have in his economical units and structures.
    :type vespeneUsedCurrentEconomy: int
    :param vespeneUsedCurrentTechnology: Specifies how much minerals does the player\
    have in his technological units, upgrades, and structures.
    :type vespeneUsedCurrentTechnology: int
    :param vespeneUsedInProgressArmy: Specifies how much vespene does the player\
    have in army that is currently being built.
    :type vespeneUsedInProgressArmy: int
    :param vespeneUsedInProgressEconomy: Specifies how much minerals does the player\
    have in economy that is currently being built.
    :type vespeneUsedInProgressEconomy: int
    :param vespeneUsedInProgressTechnology: Specifies how much minerals does the player\
    have in technology that is currently being built.
    :type vespeneUsedInProgressTechnology: int
    :param workersActiveCount: Specifies the number of workers that the player has.
    :type workersActiveCount: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "Stats":
        """
        Static method returning initialized Stats class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized Stats class.
        :rtype: Stats
        """
        return Stats(
            foodMade=d["scoreValueFoodMade"],
            foodUsed=d["scoreValueFoodUsed"],
            mineralsCollectionRate=d["scoreValueMineralsCollectionRate"],
            mineralsCurrent=d["scoreValueMineralsCurrent"],
            mineralsFriendlyFireArmy=d["scoreValueMineralsFriendlyFireArmy"],
            mineralsFriendlyFireEconomy=d["scoreValueMineralsFriendlyFireEconomy"],
            mineralsFriendlyFireTechnology=d[
                "scoreValueMineralsFriendlyFireTechnology"
            ],
            mineralsKilledArmy=d["scoreValueMineralsKilledArmy"],
            mineralsKilledEconomy=d["scoreValueMineralsKilledEconomy"],
            mineralsKilledTechnology=d["scoreValueMineralsKilledTechnology"],
            mineralsLostArmy=d["scoreValueMineralsLostArmy"],
            mineralsLostEconomy=d["scoreValueMineralsLostEconomy"],
            mineralsLostTechnology=d["scoreValueMineralsLostTechnology"],
            mineralsUsedActiveForces=d["scoreValueMineralsUsedActiveForces"],
            mineralsUsedCurrentArmy=d["scoreValueMineralsUsedCurrentArmy"],
            mineralsUsedCurrentEconomy=d["scoreValueMineralsUsedCurrentEconomy"],
            mineralsUsedCurrentTechnology=d["scoreValueMineralsUsedCurrentTechnology"],
            mineralsUsedInProgressArmy=d["scoreValueMineralsUsedInProgressArmy"],
            mineralsUsedInProgressEconomy=d["scoreValueMineralsUsedInProgressEconomy"],
            mineralsUsedInProgressTechnology=d[
                "scoreValueMineralsUsedInProgressTechnology"
            ],
            vespeneCollectionRate=d["scoreValueVespeneCollectionRate"],
            vespeneCurrent=d["scoreValueVespeneCurrent"],
            vespeneFriendlyFireArmy=d["scoreValueVespeneFriendlyFireArmy"],
            vespeneFriendlyFireEconomy=d["scoreValueVespeneFriendlyFireEconomy"],
            vespeneFriendlyFireTechnology=d["scoreValueVespeneFriendlyFireTechnology"],
            vespeneKilledArmy=d["scoreValueVespeneKilledArmy"],
            vespeneKilledEconomy=d["scoreValueVespeneKilledEconomy"],
            vespeneKilledTechnology=d["scoreValueVespeneKilledTechnology"],
            vespeneLostArmy=d["scoreValueVespeneLostArmy"],
            vespeneLostEconomy=d["scoreValueVespeneLostEconomy"],
            vespeneLostTechnology=d["scoreValueVespeneLostTechnology"],
            vespeneUsedActiveForces=d["scoreValueVespeneUsedActiveForces"],
            vespeneUsedCurrentArmy=d["scoreValueVespeneUsedCurrentArmy"],
            vespeneUsedCurrentEconomy=d["scoreValueVespeneUsedCurrentEconomy"],
            vespeneUsedCurrentTechnology=d["scoreValueVespeneUsedCurrentTechnology"],
            vespeneUsedInProgressArmy=d["scoreValueVespeneUsedInProgressArmy"],
            vespeneUsedInProgressEconomy=d["scoreValueVespeneUsedInProgressEconomy"],
            vespeneUsedInProgressTechnology=d[
                "scoreValueVespeneUsedInProgressTechnology"
            ],
            workersActiveCount=d["scoreValueWorkersActiveCount"],
        )

    def __init__(
        self,
        foodMade: int,
        foodUsed: int,
        mineralsCollectionRate: int,
        mineralsCurrent: int,
        mineralsFriendlyFireArmy: int,
        mineralsFriendlyFireEconomy: int,
        mineralsFriendlyFireTechnology: int,
        mineralsKilledArmy: int,
        mineralsKilledEconomy: int,
        mineralsKilledTechnology: int,
        mineralsLostArmy: int,
        mineralsLostEconomy: int,
        mineralsLostTechnology: int,
        mineralsUsedActiveForces: int,
        mineralsUsedCurrentArmy: int,
        mineralsUsedCurrentEconomy: int,
        mineralsUsedCurrentTechnology: int,
        mineralsUsedInProgressArmy: int,
        mineralsUsedInProgressEconomy: int,
        mineralsUsedInProgressTechnology: int,
        vespeneCollectionRate: int,
        vespeneCurrent: int,
        vespeneFriendlyFireArmy: int,
        vespeneFriendlyFireEconomy: int,
        vespeneFriendlyFireTechnology: int,
        vespeneKilledArmy: int,
        vespeneKilledEconomy: int,
        vespeneKilledTechnology: int,
        vespeneLostArmy: int,
        vespeneLostEconomy: int,
        vespeneLostTechnology: int,
        vespeneUsedActiveForces: int,
        vespeneUsedCurrentArmy: int,
        vespeneUsedCurrentEconomy: int,
        vespeneUsedCurrentTechnology: int,
        vespeneUsedInProgressArmy: int,
        vespeneUsedInProgressEconomy: int,
        vespeneUsedInProgressTechnology: int,
        workersActiveCount: int,
    ) -> None:
        # This calculation is required for raw data ingestion:
        self.foodMade = int(foodMade / 4096)
        self.foodUsed = int(foodUsed / 4096)
        self.mineralsCollectionRate = mineralsCollectionRate
        self.mineralsCurrent = mineralsCurrent
        self.mineralsFriendlyFireArmy = mineralsFriendlyFireArmy
        self.mineralsFriendlyFireEconomy = mineralsFriendlyFireEconomy
        self.mineralsFriendlyFireTechnology = mineralsFriendlyFireTechnology
        self.mineralsKilledArmy = mineralsKilledArmy
        self.mineralsKilledEconomy = mineralsKilledEconomy
        self.mineralsKilledTechnology = mineralsKilledTechnology
        self.mineralsLostArmy = mineralsLostArmy
        self.mineralsLostEconomy = mineralsLostEconomy
        self.mineralsLostTechnology = mineralsLostTechnology
        self.mineralsUsedActiveForces = mineralsUsedActiveForces
        self.mineralsUsedCurrentArmy = mineralsUsedCurrentArmy
        self.mineralsUsedCurrentEconomy = mineralsUsedCurrentEconomy
        self.mineralsUsedCurrentTechnology = mineralsUsedCurrentTechnology
        self.mineralsUsedInProgressArmy = mineralsUsedInProgressArmy
        self.mineralsUsedInProgressEconomy = mineralsUsedInProgressEconomy
        self.mineralsUsedInProgressTechnology = mineralsUsedInProgressTechnology
        self.vespeneCollectionRate = vespeneCollectionRate
        self.vespeneCurrent = vespeneCurrent
        self.vespeneFriendlyFireArmy = vespeneFriendlyFireArmy
        self.vespeneFriendlyFireEconomy = vespeneFriendlyFireEconomy
        self.vespeneFriendlyFireTechnology = vespeneFriendlyFireTechnology
        self.vespeneKilledArmy = vespeneKilledArmy
        self.vespeneKilledEconomy = vespeneKilledEconomy
        self.vespeneKilledTechnology = vespeneKilledTechnology
        self.vespeneLostArmy = vespeneLostArmy
        self.vespeneLostEconomy = vespeneLostEconomy
        self.vespeneLostTechnology = vespeneLostTechnology
        self.vespeneUsedActiveForces = vespeneUsedActiveForces
        self.vespeneUsedCurrentArmy = vespeneUsedCurrentArmy
        self.vespeneUsedCurrentEconomy = vespeneUsedCurrentEconomy
        self.vespeneUsedCurrentTechnology = vespeneUsedCurrentTechnology
        self.vespeneUsedInProgressArmy = vespeneUsedInProgressArmy
        self.vespeneUsedInProgressEconomy = vespeneUsedInProgressEconomy
        self.vespeneUsedInProgressTechnology = vespeneUsedInProgressTechnology
        self.workersActiveCount = workersActiveCount
