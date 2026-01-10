import json
import unittest
from pathlib import Path

import pytest

from sc2_datasets.available_replaypacks import DatasetProperties
from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset
from sc2_datasets.utils.json_utils import (
    dataset_to_single_json,
    get_json_offsets,
    get_object_at_index,
)
from sc2_datasets.utils.zip_utils import unpack_zipfile
from tests.test_utils.test_utils import get_setup_paths, get_test_output_dir


@pytest.mark.minor
class DatasetUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Get an example dataset:

        (
            cls.test_replaypack_name,
            cls.replaypack_zip_path,
            cls.unpack_dir_path,
            cls.download_dir_path,
            cls.unpacked,
            cls.download,
        ) = get_setup_paths()

        cls.output_dir = get_test_output_dir()
        cls.output_json_path = cls.output_dir / "single_dataset.json"

        # If it doesn't exist, unpack the test .zip archive:
        if not cls.unpacked.exists():
            # Unpacks the replaypack that will be used for testing:
            cls.unpacked = Path(
                unpack_zipfile(
                    destination_dir=cls.unpack_dir_path,
                    subdir=cls.test_replaypack_name,
                    zip_path=cls.replaypack_zip_path,
                    n_workers=1,
                )
            )

    # TODO: Check the JSON contents as well:
    def test_dataset_to_single_json_correct(self):
        test_dataset = SC2Dataset(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=False,
            names_urls=[DatasetProperties(name=self.test_replaypack_name, url="")],
        )

        output_path = dataset_to_single_json(
            dataset=test_dataset,
            output_filepath=self.output_json_path,
        )

        self.assertTrue(output_path.exists())
        self.assertEqual(output_path, self.output_json_path)

        # Test the contents of the file when its entirety is loaded:
        with output_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        # Check if it is a list
        self.assertIsInstance(data, list)

        # Check if the number of items matches the dataset
        self.assertEqual(len(data), len(test_dataset))

        # Check if the first item has the additional info
        if len(data) > 0:
            first_item = data[0]
            self.assertIn("additional_information", first_item)
            self.assertEqual(
                first_item["additional_information"]["replaypack_name"],
                self.test_replaypack_name,
            )

        json_offsets = get_json_offsets(
            json_filepath=output_path,
            offsets_filepath=None,
        )

        with output_path.open("rb") as f:
            for offset_index in range(len(json_offsets)):
                read_json = get_object_at_index(
                    file_handle=f,
                    offsets=json_offsets,
                    index=offset_index,
                )

                self.assertIsInstance(read_json, dict)
