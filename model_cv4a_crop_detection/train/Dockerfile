FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime

RUN apt-get update && apt-get install -y \
        software-properties-common
RUN apt-get update && apt-get install -y && \
    pip install --upgrade pip
    
COPY requirements-docker.txt /tmp/requirements-docker.txt

ENV INPUT_DATA_VOLUME="/var/data/input"
ENV OUTPUT_DATA_VOLUME="/var/data/output"

RUN pip install -r /tmp/requirements-docker.txt && \
    rm /tmp/requirements-docker.txt

RUN mkdir -p /app
COPY main.py /app/main.py
COPY model.py /app/model.py
COPY prepare_data.py /app/prepare_data.py
COPY run-model.sh /app/run-model.sh

WORKDIR /app

ENTRYPOINT [ "bash", "run-model.sh" ]
