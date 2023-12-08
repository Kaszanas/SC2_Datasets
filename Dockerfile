FROM nvidia/cuda:12.1.0-runtime-ubuntu20.04


RUN pip install poetry

# Install pytorch with CUDA GPU support:
RUN pip install torch --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app

# Copy entire repository contents
# This is needed because package needs the ability to install itself:
COPY . .

# Install only "production" dependencies
RUN poetry install --without dev