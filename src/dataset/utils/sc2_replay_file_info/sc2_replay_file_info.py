from msilib.schema import Error
import os


class SC2ReplayFileInfo:

    """
    Is a custom data type that holds information about SC2 replay.

    :param directory: The directory that contains parsed .json files with data from SC2 replays.
    :type directory: str
    :param filename: Specifies the filename of a specific .json file which was previously parsed.
    :type filename: str
    """

    def __init__(
        self,
        directory: str,
        filename: str,
    ) -> None:

        if not os.path.isdir(directory):
            raise Error

        if not os.path.isfile(filename):
            raise Error

        self.directory = directory
        self.filename = filename

    def get_full_path(self) -> str:
        """
        Exposes the logic to access full path of a specific parsed replay .json file.

        :return: Returns a string that resembles the full path of a specific .json file containing data from a parsed replay.
        :rtype: str
        """
        return os.path.join(self.directory, self.filename)
