FROM nvidia/cuda:12.1.0-runtime-ubuntu20.04


RUN pip install poetry
RUN pip install torch --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app

COPY . .

RUN poetry install