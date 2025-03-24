# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

### Development with Docker

If you wish to develop using Docker, there is a `Dockerfile.dev` defined. Please use the following commands:

Build the Dockerfile (CPU):
```
docker build --tag=sc2_datasets:dev -f .\docker\Dockerfile.dev .
```

Build the Dockerfile (GPU):
```
docker build --tag=sc2_datasets:dev -f .\docker\Dockerfile.dev.gpu .
```

Run the Dockerfile:
```
docker run --gpus all -it -v .:/app sc2_datasets:dev
```

### Local Development

Ready to contribute? Here's how to set up `sc2_datasets` for local development.

1. Download a copy of `sc2_datasets` locally.
2. Install `sc2_datasets` using `poetry`:

    ```console
    $ poetry install
    ```

3. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

4. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

5. Before running tests make sure to setup environment variable name: `TEST_WORKSPACE` value: `YOUR_PATH_TO_APP`

6. Commit your changes and open a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `sc2_datasets` project is released
with a Contributor License Agreement (CLA)
Code of Conduct. By contributing to this project you agree to abide by its terms.
