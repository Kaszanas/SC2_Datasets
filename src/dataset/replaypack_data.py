import os

from torch.utils.data import Dataset
from dataset.replay_data import SC2ReplayData
from dataset.utils.download_utils import download_and_unpack_replaypack


# TODO: This should hold the extraction logs.
# And other information that comes out of the processing pipeline:
class SC2ReplaypackData(Dataset):
    """
    Holds IterableDatasets for the data that
    is within a single StarCraft .json representation of a replay file.
    """

    def __init__(
        self,
        replaypack_name: str,
        replaypack_download_dir: str,
        replaypack_unpack_dir: str,
        url: str = "",
        download: bool = False,
    ):
        self.replaypack_download_dir = replaypack_download_dir
        self.replaypack_unpack_dir = replaypack_unpack_dir
        self.replaypack_name = replaypack_name
        self.url = url

        if download:
            (
                data_path,
                summary_content,
                mapping_content,
                processed_info,
            ) = download_and_unpack_replaypack(
                replaypack_download_dir=self.replaypack_download_dir,
                replaypack_unpack_dir=self.replaypack_unpack_dir,
                replaypack_name=self.replaypack_name,
                url=self.url,
            )

        self.replaypack_summary = summary_content
        self.replaypack_dir_mapping = mapping_content
        self.replaypack_processed_info = processed_info

        # Load all of the files
        self.list_of_files = os.listdir(data_path)
        self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int) -> SC2ReplayData:
        return SC2ReplayData(replay_filepath=self.list_of_files[index])
