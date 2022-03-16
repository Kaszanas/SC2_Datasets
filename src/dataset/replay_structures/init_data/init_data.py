from dataset.replay_structures.init_data.game_description import GameDescription


class InitData:
    def __init__(self, game_description: GameDescription) -> None:
        self.game_description = game_description
