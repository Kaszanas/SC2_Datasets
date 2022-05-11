from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset

# from src.dataset.validators.validate_chunk import validate_integrity_singleprocess

dataset = SC2EGSetDataset(
    unpack_dir="",
    download=False,
    validator=validate_integrity_singleprocess,
)

for i in len(dataset):
    replay = dataset[i]
