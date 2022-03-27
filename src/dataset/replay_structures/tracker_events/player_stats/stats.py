class Stats:

    """_summary_

    :param foodMade: _description_
    :type foodMade: int
    :param foodUsed: _description_
    :type foodUsed: int
    :param mineralsCollectionRate: _description_
    :type mineralsCollectionRate: int
    :param mineralsCurrent: _description_
    :type mineralsCurrent: int
    :param mineralsFriendlyFireArmy: _description_
    :type mineralsFriendlyFireArmy: int
    :param mineralsFriendlyFireEconomy: _description_
    :type mineralsFriendlyFireEconomy: int
    :param mineralsFriendlyFireTechnology: _description_
    :type mineralsFriendlyFireTechnology: int
    :param mineralsKilledArmy: _description_
    :type mineralsKilledArmy: int
    :param mineralsKilledEconomy: _description_
    :type mineralsKilledEconomy: int
    :param mineralsKilledTechnology: _description_
    :type mineralsKilledTechnology: int
    :param mineralsLostArmy: _description_
    :type mineralsLostArmy: int
    :param mineralsLostEconomy: _description_
    :type mineralsLostEconomy: int
    :param mineralsLostTechnology: _description_
    :type mineralsLostTechnology: int
    :param mineralsUsedActiveForces: _description_
    :type mineralsUsedActiveForces: int
    :param mineralsUsedCurrentArmy: _description_
    :type mineralsUsedCurrentArmy: int
    :param mineralsUsedCurrentEconomy: _description_
    :type mineralsUsedCurrentEconomy: int
    :param mineralsUsedCurrentTechnology: _description_
    :type mineralsUsedCurrentTechnology: int
    :param mineralsUsedInProgressArmy: _description_
    :type mineralsUsedInProgressArmy: int
    :param mineralsUsedInProgressEconomy: _description_
    :type mineralsUsedInProgressEconomy: int
    :param mineralsUsedInProgressTechnology: _description_
    :type mineralsUsedInProgressTechnology: int
    :param vespeneCollectionRate: _description_
    :type vespeneCollectionRate: int
    :param vespeneCurrent: _description_
    :type vespeneCurrent: int
    :param vespeneFriendlyFireArmy: _description_
    :type vespeneFriendlyFireArmy: int
    :param vespeneFriendlyFireEconomy: _description_
    :type vespeneFriendlyFireEconomy: int
    :param vespeneFriendlyFireTechnology: _description_
    :type vespeneFriendlyFireTechnology: int
    :param vespeneKilledArmy: _description_
    :type vespeneKilledArmy: int
    :param vespeneKilledEconomy: _description_
    :type vespeneKilledEconomy: int
    :param vespeneKilledTechnology: _description_
    :type vespeneKilledTechnology: int
    :param vespeneLostArmy: _description_
    :type vespeneLostArmy: int
    :param vespeneLostEconomy: _description_
    :type vespeneLostEconomy: int
    :param vespeneLostTechnology: _description_
    :type vespeneLostTechnology: int
    :param vespeneUsedActiveForces: _description_
    :type vespeneUsedActiveForces: int
    :param vespeneUsedCurrentArmy: _description_
    :type vespeneUsedCurrentArmy: int
    :param vespeneUsedCurrentEconomy: _description_
    :type vespeneUsedCurrentEconomy: int
    :param vespeneUsedCurrentTechnology: _description_
    :type vespeneUsedCurrentTechnology: int
    :param vespeneUsedInProgressArmy: _description_
    :type vespeneUsedInProgressArmy: int
    :param vespeneUsedInProgressEconomy: _description_
    :type vespeneUsedInProgressEconomy: int
    :param vespeneUsedInProgressTechnology: _description_
    :type vespeneUsedInProgressTechnology: int
    :param workersActiveCount: _description_
    :type workersActiveCount: int
    """

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
