from pathlib import Path
from typing import Callable

from torch.utils.data import Dataset

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData


class SC2DatasetDirectory(Dataset):
    def __init__(
        self,
        directory: Path,
        transform: None | Callable = None,
        validator: None | Callable = None,
    ):
        self.directory = directory
        self.transform = transform
        self.validator = validator

        all_files = list(self.directory.rglob("*.SC2Replay.json"))
        if not all_files:
            raise ValueError(
                f"No .SC2Replay.json files found in directory {self.directory}"
            )

        # Validating files:
        self.skip_files: set[Path] = set()
        for file_path in all_files:
            if self.validator:
                is_valid = self.validator(file_path)
                if not is_valid:
                    self.skip_files.add(file_path)

        self.list_of_files: list[Path] = []
        for file_path in all_files:
            if file_path in self.skip_files:
                continue
            self.list_of_files.append(file_path)

        self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int):
        file_to_load = self.list_of_files[index]
        replay_data = SC2ReplayData.from_file(replay_filepath=file_to_load)
        if self.transform:
            return self.transform(replay_data)
        return replay_data
