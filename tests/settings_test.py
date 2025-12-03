from sc2_datasets.available_replaypacks import DatasetProperties

TEST_SYNTHETIC_REPLAYPACKS = [
    DatasetProperties(
        name="2022_TestReplaypack",
        url="https://github.com/Kaszanas/SC2EGSet_Dataset/raw/dev/tests/test_files/2022_TestReplaypack.zip",  # noqa
    )
]

TEST_SINGLE_JSON_REPLAYPACKS = [
    DatasetProperties(
        name="sc2egset_synthetic_merged",
        url="https://github.com/Kaszanas/SC2EGSet_Dataset/raw/dev/tests/test_files/sc2egset_synthetic_merged.zip",
    ),
]

TEST_REAL_REPLAYPACKS = [
    DatasetProperties(
        name="2016_IEM_10_Taipei",
        url="https://zenodo.org/record/6903505/files/2016_IEM_10_Taipei.zip?download=1",
    ),
    DatasetProperties(
        name="2016_IEM_11_Shanghai",
        url="https://zenodo.org/record/6903505/files/2016_IEM_11_Shanghai.zip?download=1",
    ),
]
