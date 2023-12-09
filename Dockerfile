FROM nvidia/cuda:12.1.0-runtime-ubuntu20.04

ENV PYTHON_VERSION 3.11.4

# No questions from dependency installation:
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    make build-essential \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    wget ca-certificates curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 \
    git

# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Pyenv to handle specific Python installation
# Install pyenv:
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

# Install pytorch with CUDA GPU support:
RUN pip install torch --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app

# Copy entire repository contents
# This is needed because package needs the ability to install itself:
COPY . .

# Install only "production" dependencies
RUN poetry install --without dev