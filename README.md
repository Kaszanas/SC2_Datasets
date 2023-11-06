[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6629005.svg)](https://doi.org/10.5281/zenodo.6629005)
[![PyPI](https://img.shields.io/pypi/v/sc2-datasets?style=flat-square)](https://pypi.org/project/sc2-datasets/)
[![Python](https://img.shields.io/badge/python-3.10%5E-blue)](https://www.python.org/)

# StarCraft II Datasets

Library can be used to interface with datasets that were pre-processed with our pipeline
as described in:
- [SC2DatasetPreparator](https://github.com/Kaszanas/SC2DatasetPreparator)

Currently we have exposed PyTorch and PyTorch Lightning API. Our goal is to provide
infrastructure used for StarCraft&nbsp;II analytics.

Please refer to the [**official documentation**](https://sc2-datasets.readthedocs.io/), or contact contributors directly for all of the details.

## Supported Datasets

### SC2EGSet: StarCraft II Esport Game State Dataset

This project contains official API implementation for the [SC2EGSet: StarCraft II Esport Game State Dataset](https://doi.org/10.5281/zenodo.5503997), which is built based on [SC2ReSet: StarCraft II Esport Replaypack Set](https://doi.org/10.5281/zenodo.5575796).
Contents of this library provide PyTorch and PyTorch Lightning API for pre-processed StarCraft II dataset.

## Installation

1. Manually install PyTorch with minimal version of ```^1.11.0+cu116```.
2. Perform the following command:

```bash
$ pip install sc2_datasets
```

## Usage

Basic example usage can be seen below. For advanced interactions with the datasets
please refer to the documentation.

Use [SC2EGSet](https://doi.org/10.5281/zenodo.5503997) with PyTorch:
```python
from sc2_datasets.torch.sc2_egset_dataset import SC2EGSetDataset
from sc2_datasets.available_replaypacks import EXAMPLE_SYNTHETIC_REPLAYPACKS

if __name__ == "__main__":
    # Initialize the dataset:
    sc2_egset_dataset = SC2EGSetDataset(
        unpack_dir="./unpack_dir_path",           # Specify existing directory path, where the data will be unpacked.
        download_dir="./download_dir_path",       # Specify existing directory path, where the data will be downloaded.
        download=True,
        names_urls=EXAMPLE_SYNTHETIC_REPLAYPACKS, # Use a synthetic replaypack containing 1 replay.
    )

    # Iterate over instances:
    for i in range(len(sc2_egset_dataset)):
        sc2_egset_dataset[i]
```

Use [SC2EGSet](https://doi.org/10.5281/zenodo.5503997) with PyTorch Lightning:
```python
from sc2_datasets.lightning.sc2_egset_datamodule import SC2EGSetDataModule
from sc2_datasets.available_replaypacks import EXAMPLE_SYNTHETIC_REPLAYPACKS

if __name__ == "__main__":
    sc2_egset_datamodule = SC2EGSetDataModule(
                unpack_dir="./unpack_dir_path",            # Specify existing directory path, where the data will be unpacked.
                download_dir="./download_dir_path",        # Specify existing directory path, where the data will be downloaded.
                download=True,
                replaypacks=EXAMPLE_SYNTHETIC_REPLAYPACKS, # Use a synthetic replaypack containing 1 replay.
            )
    sc2_egset_datamodule.prepare_data()
    sc2_egset_datamodule.setup()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Contributor License Agreement (CLA) and a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`sc2egset_dataset` was created by Andrzej Białecki. It is licensed under the terms of the GNU General Public License v3.0 license.

## Cite

### [Dataset Description Article](https://www.researchgate.net/publication/373767449_SC2EGSet_StarCraft_II_Esport_Replay_and_Game-state_Dataset)

To cite the article that introduces [SC2ReSet](https://doi.org/10.5281/zenodo.5575796) and [SC2EGSet](https://doi.org/10.5281/zenodo.5503997) use this:

```bibtex
@article{Białecki2023,
  author   = {Bia{\l}ecki, Andrzej
              and Jakubowska, Natalia
              and Dobrowolski, Pawe{\l}
              and Bia{\l}ecki, Piotr
              and Krupi{\'{n}}ski, Leszek
              and Szczap, Andrzej
              and Bia{\l}ecki, Robert
              and Gajewski, Jan},
  title    = {SC2EGSet: StarCraft II Esport Replay and Game-state Dataset},
  journal  = {Scientific Data},
  year     = {2023},
  month    = {Sep},
  day      = {08},
  volume   = {10},
  number   = {1},
  pages    = {600},
  issn     = {2052-4463},
  doi      = {10.1038/s41597-023-02510-7},
  url      = {https://doi.org/10.1038/s41597-023-02510-7}
}
```
