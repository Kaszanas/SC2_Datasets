# TODO: This should hold the extraction logs.
# And other information that comes out of the processing pipeline:
class SC2ReplaypackData:
    """
    Holds IterableDatasets for the data that
    is within a single StarCraft .json representation of a replay file.
    """

    def __init__(self, files, processing_log) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __getitem__(self) -> "SC2ReplayData":
        pass
