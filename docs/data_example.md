# Data example

Below we post a direct ilustration of the data format.
Every single StarCraft II replay has these json objects.
We parse these data with our tools to get specific information.

---

## Header
Header represents the replay header parameters representation. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/header/header/index.html?highlight=header%20#sc2_datasets.replay_parser.header.header.Header)

```
"header": {
    "elapsedGameLoops": 7855,
    "version": "3.4.0.44401"
  }
```

---

## InitData
Data type containing some "init data" information about StarCraft II game. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/init_data/init_data/index.html?highlight=initData#sc2_datasets.replay_parser.init_data.init_data.InitData)
```
"initData": {
    "gameDescription": {
      "gameOptions": {z
        "advancedSharedControl": false,
        "amm": false,
        "battleNet": true,
        "clientDebugFlags": 265,
        "competitive": false,
        "cooperative": false,
        "fog": 0,
        "heroDuplicatesAllowed": true,
        "lockTeams": true,
        "noVictoryOrDefeat": false,
        "observers": 0,
        "practice": false,
        "randomRaces": false,
        "teamsTogether": false,
        "userDifficulty": 0
      },
      "gameSpeed": "Faster",
      "isBlizzardMap": true,
      "mapAuthorName": "5-S2-1-1",
      "mapFileSyncChecksum": 360400735,
      "mapSizeX": 152,
      "mapSizeY": 152,
      "maxPlayers": 2
    }
  }
```

---

## Details
Data type containing some "details" information about an StarCraft II game. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/details/details/index.html?highlight=details#sc2_datasets.replay_parser.details.details.Details)
```
"details": {
    "gameSpeed": "Faster",
    "isBlizzardMap": true,
    "timeUTC": "2016-07-29T04:50:12.5655603Z"
  }
```

---

## Metadata
Specifies a class which includes parameters about the game. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/metadata/metadata/index.html?highlight=Metadata#sc2_datasets.replay_parser.metadata.metadata.Metadata)
```
"metadata": {
    "baseBuild": "",
    "dataBuild": "",
    "gameVersion": "",
    "mapName": "Galactic Process LE"
  }
```

---

## MessageEvents
Contains the information about in game chat between the players. We don't use this information at all.
```
"messageEvents": [
    {
      "evtTypeName": "Chat",
      "id": 0,
      "loop": 219,
      "recipient": 0,
      "string": "(glhf)",
      "userid": {
        "userId": 1
      }
    }, ...
  ]
```

---

## GameEvents
Contains the list of objects with informationsabout the events happened in the game. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/game_events/game_events_parser/index.html?highlight=GameEventsParser#sc2_datasets.replay_parser.game_events.game_events_parser.GameEventsParser)

```
"gameEvents": [...]
```


Unique events available are listed in the following sections.

### UserOptions


```
  {
    "baseBuildNum": 44401,
    "buildNum": 44401,
    "cameraFollow": false,
    "debugPauseEnabled": false,
    "developmentCheatsEnabled": false,
    "evtTypeName": "UserOptions",
    "gameFullyDownloaded": true,
    "hotkeyProfile": "\u003ccustom\u003e",
    "id": 7,
    "isMapToMapTransition": false,
    "loop": 0,
    "multiplayerCheatsEnabled": false,
    "platformMac": false,
    "syncChecksummingEnabled": false,
    "testCheatsEnabled": false,
    "useGalaxyAsserts": false,
    "userid": {
      "userId": 0
    },
    "versionFlags": 0
  },
```


```
"gameEvents": [
    {
      "distance": null,
      "evtTypeName": "CameraUpdate",
      "follow": false,
      "id": 49,
      "loop": 2,
      "pitch": null,
      "reason": null,
      "target": {
        "x": 0.7109375,
        "y": 0.5469970703125
      },
      "userid": {
        "userId": 6
      },
      "yaw": null
    },
    {
      "controlGroupId": 10,
      "delta": {
        "addSubgroups": [
          {
            "count": 1,
            "intraSubgroupPriority": 1,
            "subgroupPriority": 32,
            "unitLink": 108
          }
        ],
        "addUnitTags": [
          56885249
        ],
        "removeMask": {
          "None": null
        },
        "subgroupIndex": 0
      },
      "evtTypeName": "SelectionDelta",
      "id": 28,
      "loop": 12,
      "userid": {
        "userId": 5
      }
    },
    {
      "abil": {
        "abilCmdData": null,
        "abilCmdIndex": 0,
        "abilLink": 188
      },
      "cmdFlags": 256,
      "data": {
        "None": null
      },
      "evtTypeName": "Cmd",
      "id": 27,
      "loop": 15,
      "otherUnit": null,
      "sequence": 1,
      "unitGroup": null,
      "userid": {
        "userId": 5
      }
    },
    {
      "abil": null,
      "cmdFlags": 264,
      "data": {
        "TargetUnit": {
          "snapshotControlPlayerId": 0,
          "snapshotPoint": {
            "x": 548864,
            "y": 538624,
            "z": 49104
          },
          "snapshotUnitLink": 369,
          "snapshotUpkeepPlayerId": 0,
          "tag": 1310721,
          "targetUnitFlags": 111,
          "timer": 0
        }
      },
      "evtTypeName": "Cmd",
      "id": 27,
      "loop": 24,
      "otherUnit": null,
      "sequence": 2,
      "unitGroup": null,
      "userid": {
        "userId": 5
      },
    {
      "abil": null,
      "cmdFlags": 264,
      "data": {
        "TargetPoint": {
          "x": 123854,
          "y": 90417,
          "z": 49111
        }
      },
      "evtTypeName": "Cmd",
      "id": 27,
      "loop": 23,
      "otherUnit": null,
      "sequence": 2,
      "unitGroup": null,
      "userid": {
        "userId": 1
      }
    },
    {
      "controlGroupId": 10,
      "delta": {
        "addSubgroups": [
          {
            "count": 1,
            "intraSubgroupPriority": 1,
            "subgroupPriority": 60,
            "unitLink": 126
          }
        ],
        "addUnitTags": [
          60555265
        ],
        "removeMask": {
          "ZeroIndices": []
        },
        "subgroupIndex": 0
      },
      "evtTypeName": "SelectionDelta",
      "id": 28,
      "loop": 35,
      "userid": {
        "userId": 5
      }
    },
    {
      "evtTypeName": "CmdUpdateTargetUnit",
      "id": 105,
      "loop": 37,
      "target": {
        "snapshotControlPlayerId": 0,
        "snapshotPoint": {
          "x": 64.5,
          "y": 68.75,
          "z": 5.994140625
        },
        "snapshotUnitLink": 369,
        "snapshotUpkeepPlayerId": 0,
        "tag": 2883585,
        "targetUnitFlags": 111,
        "timer": 0
      },
      "userid": {
        "userId": 5
      }
    },
    {
      "evtTypeName": "CommandManagerState",
      "id": 103,
      "loop": 37,
      "sequence": 3,
      "state": 1,
      "userid": {
        "userId": 5
      }
    },
    {
      "controlGroupIndex": 1,
      "controlGroupUpdate": 2,
      "evtTypeName": "ControlGroupUpdate",
      "id": 29,
      "loop": 1639,
      "mask": {
        "None": null
      },
      "userid": {
        "userId": 1
      }
    },
    {
      "evtTypeName": "CmdUpdateTargetPoint",
      "id": 104,
      "loop": 2965,
      "target": {
        "x": 19.133056640625,
        "y": 26.369140625,
        "z": 5.73388671875
      },
      "userid": {
        "userId": 5
      }
    },
    {
      "evtTypeName": "GameUserLeave",
      "id": 101,
      "leaveReason": 0,
      "loop": 7845,
      "userid": {
        "userId": 5
      }
    },...
]
```
## TrackerEvents
Exposes a logic of converting a single list of objects to a dictionary representation of the data.Can be used to initialize a pandas DataFrame. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/tracker_events/tracker_events_parser/index.html?highlight=TrackerEventsparser#sc2_datasets.replay_parser.tracker_events.tracker_events_parser.TrackerEventsParser)

```
"trackerEvents": [
    {
      "evtTypeName": "PlayerSetup",
      "id": 9,
      "loop": 0,
      "playerId": 1,
      "slotId": 0,
      "type": 1,
      "userId": 1
    },
    {
      "evtTypeName": "PlayerStats",
      "id": 0,
      "loop": 1,
      "playerId": 1,
      "stats": {
        "scoreValueFoodMade": 57344,
        "scoreValueFoodUsed": 49152,
        "scoreValueMineralsCollectionRate": 0,
        "scoreValueMineralsCurrent": 50,
        "scoreValueMineralsFriendlyFireArmy": 0,
        "scoreValueMineralsFriendlyFireEconomy": 0,
        "scoreValueMineralsFriendlyFireTechnology": 0,
        "scoreValueMineralsKilledArmy": 0,
        "scoreValueMineralsKilledEconomy": 0,
        "scoreValueMineralsKilledTechnology": 0,
        "scoreValueMineralsLostArmy": 0,
        "scoreValueMineralsLostEconomy": 0,
        "scoreValueMineralsLostTechnology": 0,
        "scoreValueMineralsUsedActiveForces": 0,
        "scoreValueMineralsUsedCurrentArmy": 0,
        "scoreValueMineralsUsedCurrentEconomy": 1050,
        "scoreValueMineralsUsedCurrentTechnology": 0,
        "scoreValueMineralsUsedInProgressArmy": 0,
        "scoreValueMineralsUsedInProgressEconomy": 0,
        "scoreValueMineralsUsedInProgressTechnology": 0,
        "scoreValueVespeneCollectionRate": 0,
        "scoreValueVespeneCurrent": 0,
        "scoreValueVespeneFriendlyFireArmy": 0,
        "scoreValueVespeneFriendlyFireEconomy": 0,
        "scoreValueVespeneFriendlyFireTechnology": 0,
        "scoreValueVespeneKilledArmy": 0,
        "scoreValueVespeneKilledEconomy": 0,
        "scoreValueVespeneKilledTechnology": 0,
        "scoreValueVespeneLostArmy": 0,
        "scoreValueVespeneLostEconomy": 0,
        "scoreValueVespeneLostTechnology": 0,
        "scoreValueVespeneUsedActiveForces": 0,
        "scoreValueVespeneUsedCurrentArmy": 0,
        "scoreValueVespeneUsedCurrentEconomy": 0,
        "scoreValueVespeneUsedCurrentTechnology": 0,
        "scoreValueVespeneUsedInProgressArmy": 0,
        "scoreValueVespeneUsedInProgressEconomy": 0,
        "scoreValueVespeneUsedInProgressTechnology": 0,
        "scoreValueWorkersActiveCount": 12
      }
    },
    {
      "evtTypeName": "UnitTypeChange",
      "id": 4,
      "loop": 15,
      "unitTagIndex": 218,
      "unitTagRecycle": 1,
      "unitTypeName": "Egg"
    },
    {
      "controlPlayerId": 1,
      "evtTypeName": "UnitBorn",
      "id": 1,
      "loop": 652,
      "unitTagIndex": 238,
      "unitTagRecycle": 1,
      "unitTypeName": "Drone",
      "upkeepPlayerId": 1,
      "x": 23,
      "y": 17
    },
    {
      "evtTypeName": "UnitTypeChange",
      "id": 4,
      "loop": 652,
      "unitTagIndex": 203,
      "unitTagRecycle": 1,
      "unitTypeName": "Larva"
    },
    {
      "evtTypeName": "UnitDied",
      "id": 2,
      "killerPlayerId": null,
      "killerUnitTagIndex": null,
      "killerUnitTagRecycle": null,
      "loop": 652,
      "unitTagIndex": 203,
      "unitTagRecycle": 1,
      "x": 23,
      "y": 17
    },
    {
      "evtTypeName": "UnitPositions",
      "firstUnitIndex": 265,
      "id": 8,
      "items": [
        0,
        50,
        27,
        14,
        49,
        26,
        3,
        49,
        28,
        9,
        48,
        28,
        18,
        50,
        26,
        11,
        50,
        27,
        21,
        55,
        23
      ],
      "loop": 6000
    }
]
```

---

## ToonPlayerDescMap
We parse this object into separate objects with informations about the in game player status. More information here: [documentation](https://sc2-datasets.readthedocs.io/en/latest/autoapi/sc2_datasets/replay_parser/toon_player_desc_map/toon_player_desc/index.html?highlight=ToonPlayerDesc#sc2_datasets.replay_parser.toon_player_desc_map.toon_player_desc.ToonPlayerDesc)
```
"ToonPlayerDescMap": {
    "5-S2-1-7361539": {
      "nickname": "viOLet",
      "playerID": 2,
      "userID": 5,
      "SQ": 105,
      "supplyCappedPercent": 4,
      "startDir": 1,
      "startLocX": 127,
      "startLocY": 131,
      "race": "Zerg",
      "selectedRace": "",
      "APM": 0,
      "MMR": 0,
      "result": "Win",
      "region": "China",
      "realm": "China",
      "highestLeague": "Unknown",
      "isInClan": false,
      "clanTag": "",
      "handicap": 100,
      "color": {
        "a": 255,
        "b": 0,
        "g": 66,
        "r": 255
      }
    },
    "5-S2-1-7361634": {
      "nickname": "Nerchio",
      "playerID": 1,
      "userID": 1,
      "SQ": 115,
      "supplyCappedPercent": 7,
      "startDir": 7,
      "startLocX": 24,
      "startLocY": 20,
      "race": "Zerg",
      "selectedRace": "",
      "APM": 0,
      "MMR": 0,
      "result": "Loss",
      "region": "China",
      "realm": "China",
      "highestLeague": "Unknown",
      "isInClan": false,
      "clanTag": "",
      "handicap": 100,
      "color": {
        "a": 255,
        "b": 180,
        "g": 20,
        "r": 30
      }
    }
  }
```

---

## GameEventsErr
A boolean value representating the information if in game event error occured.
```
"gameEventsErr": false
```

---

## MessageEventsErr
A boolean value representating the information if in game message event error occured.
```
"messageEventsErr": false
```

---

## TrackerEvtsErr
A boolean value representating the information if in game tracker error occured.
```
"trackerEvtsErr": false
```
