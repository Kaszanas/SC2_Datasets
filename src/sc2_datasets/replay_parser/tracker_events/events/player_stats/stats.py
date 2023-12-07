from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class Stats(TrackerEvent):
    """
    Stats holds specific fields on the economy of a player and is used in PlayerStats event.

    Parameters
    ----------
    foodMade : int
        Specifies the amount of supply that a player created.\
        This is a limit of units that can be made.
    foodUsed : int
        Specifies how much of the supply is used for units.
    mineralsCollectionRate : int
        Specifies the collection rate of minerals. Most likely per minute.
    mineralsCurrent : int
        Specifies how much minerals the player has in his "bank".
    mineralsFriendlyFireArmy : int
        Specifies how much minerals were lost in friendly fire on army units.
    mineralsFriendlyFireEconomy : int
        Specifies how much minerals were lost in friendly fire on economy.
    mineralsFriendlyFireTechnology : int
        Specifies how much minerals were lost in friendly fire on technology.
    mineralsKilledArmy : int
        Specifies how much minerals a player killed in his opponent's army.
    mineralsKilledEconomy : int
        Specifies how much minerals player killed in his opponent's economy.
    mineralsKilledTechnology : int
        Specifies how much minerals player killed in his opponent's technology.
    mineralsLostArmy : int
        Specifies how much minerals player lost in his army.
    mineralsLostEconomy : int
        Specifies how much minerals player lost in his economy.
    mineralsLostTechnology : int
        Specifies how much minerals player lost in his technology.
    mineralsUsedActiveForces : int
        Specifies how much minerals does the player have in his active forces.
    mineralsUsedCurrentArmy : int
        Specifies how much minerals does the player have in his army.
    mineralsUsedCurrentEconomy : int
        Specifies how much minerals does the player have in his\
        economical units and structures.
    mineralsUsedCurrentTechnology : int
        Specifies how much minerals does the player have in his technological\
        units, upgrades, and structures.
    mineralsUsedInProgressArmy : int
        Specifies how much minerals does the player have in army that\
        is currently being built.
    mineralsUsedInProgressEconomy : int
        Specifies how much minerals does the player have in economy that\
        is currently being built.
    mineralsUsedInProgressTechnology : int
        Specifies how much minerals does the player have in technology that is\
        currently being built.
    vespeneCollectionRate : int
        Specifies what is the vespene collection rate. Most likely per minute.
    vespeneCurrent : int
        Specifies the amount of vespene gas that the user has in his "bank".
    vespeneFriendlyFireArmy : int
        Specifies how much vespene was lost in friendly fire on army units.
    vespeneFriendlyFireEconomy : int
        Specifies how much vespene was lost in friendly fire on economy.
    vespeneFriendlyFireTechnology : int
        Specifies how much vespene was lost in friendly fire on technology.
    vespeneKilledArmy : int
        Specifies how much vespene player killed in his opponent's army.
    vespeneKilledEconomy : int
        Specifies how much vespene player killed in his opponent's economy.
    vespeneKilledTechnology : int
        Specifies how much vespene player killed in his opponent's technology.
    vespeneLostArmy : int
        Specifies how much vespene player lost in his army.
    vespeneLostEconomy : int
        Specifies how much vespene player lost in his economy.
    vespeneLostTechnology : int
        Specifies how much vespene player lost in his technology.
    vespeneUsedActiveForces : int
        Specifies how much vespene does the player have in his active forces.
    vespeneUsedCurrentArmy : int
        Specifies how much vespene does the player have in his army.
    vespeneUsedCurrentEconomy : int
        Specifies how much vespene does the player have in his economical\
        units and structures.
    vespeneUsedCurrentTechnology : int
        Specifies how much vespene does the player have in his technological\
        units, upgrades, and structures.
    vespeneUsedInProgressArmy : int
        Specifies how much vespene does the player have in army that\
        is currently being built.
    vespeneUsedInProgressEconomy : int
        Specifies how much minerals does the player have in economy that\
        is currently being built.
    vespeneUsedInProgressTechnology : int
        Specifies how much minerals does the player have in technology that\
        is currently being built.
    workersActiveCount : int
        Specifies the number of workers that the player has.
    """

    @staticmethod
    def from_dict(d: Dict) -> "Stats":
        """
        Static method returning initialized Stats class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file
            that is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        Stats
            Returns an initialized Stats class.
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
