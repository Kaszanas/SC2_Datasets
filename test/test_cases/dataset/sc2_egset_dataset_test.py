import unittest

from src.dataset.sc2_egset_dataset import SC2EGSetDataset


class SC2EGSetDatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_loading_replaypacks(self):

        sc2egset_dataset = SC2EGSetDataset(
            names_urls=[
                ("2020_IEM_Katowice", ""),
            ],
            download=False,
        )

        self.assertIsInstance(sc2egset_dataset, SC2EGSetDataset)

    def test_parsing_all_files(self):

        # TODO: Iterate over the whole dataset and test replay json parsing

        pass

    def test_get_item(self):
        pass

    def test_get_len(self):
        pass
