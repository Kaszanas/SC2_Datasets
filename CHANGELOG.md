# Changelog



## 1.1.0 (2025-03-24)

### Feat

- multithreading zip unpacking with progressbars
- separated download\unpack responsibility
- multithreading initialization of replaypacks
- staticmethod for multithread initialization

### Fix

- dataset 2.1.3 hotfix in available_replaypacks
- **camera_update**: camera update can have null target
- matching names and urls

### Refactor

- organizing imports
- removed unused arguments
- **download_utils**: Drafting download progress
- **ruff**: sorting imports with ruff
- **pre-commit**: ran ruff pre-commit on entire repository

## v1.0.2 (2022/08/28)

- Verified the examples.
- Implemented a bugfix for EXAMPLE_SYNTHETIC_REPLAYPACKS, the replaypack was set to be downloaded from URL of a branch that no longer exists.

## v1.0.1 (2022/08/28)

- Implemented a bugfix for EXAMPLE_SYNTHETIC_REPLAYPACKS, the replaypack was set to be downloaded from URL of a branch that no longer exists.

## v1.0.0 (2022/07/28)

- Changed repository name to "SC2_Datasets"
- Changed package name to ```sc2_datasets```
- Inroduced poetry to the project.
- Added Contributor License Agreement (CLA)
- Added GitHub Actions for continuous integration (CI):
    - Linter execution
    - Testing
    - Documentation building
- Added GitHub Actions for continous deployment (CD):
    - Uploading to test.pypi
    - Uploading to pypi

## v0.9.0 (2022/06/09)

- First release of `sc2_datasets`!
