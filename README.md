# {{ A Spatio-Temporal Deep Learning-Based Crop Classification Model for Satellite Imagery }}

First place solution for Crop Detection from Satellite Imagery competition
organized by CV4A workshop at ICLR 2020. The model architecture consists of
3-layer Conv-net, Masked Features Averaging layer, 3-layer Bi-directional
GRU-net and fully connected classification layer. Masked Features Averaging
layer is similar to global average pooling but only averages pixels belong to
crop field.

![model-cv4a-crop-detection-v1](https://radiantmlhub.blob.core.windows.net/frontend-ml-model-images/model-cv4a-crop-detection-v1.png)

MLHub model id: `model-cv4a-crop-detection-v1`. Browse on [Radiant MLHub](https://mlhub.earth/model/model-cv4a-crop-detection-v1).

## ML Model Documentation

Please review the model architecture, license, applicable spatial and temporal extents
and other details in the [model documentation](/docs/index.md).

## System Requirements

* Git client
* [Docker](https://www.docker.com/) with
    [Compose](https://docs.docker.com/compose/) v1.28 or newer.

## Hardware Requirements

|Inferencing|Training|
|-----------|--------|
|{{int}}GB RAM | 20GB RAM|
|           | NVIDIA GPU |

## Get Started With Inferencing

First clone this Git repository.

```bash
git clone https://github.com/radiantearth/CropDetectionDL.git
cd CropDetectionDL/
```

After cloning the model repository, you can use the Docker Compose runtime
files as described below.

## Pull or Build the Docker Image

{{

:pushpin: Model developer: please build and publish your images to [Docker
Hub](https://hub.docker.com/). The images should be public, and should be
tagged as `model_id:version` and `model_id:version-gpu`.

For example model_id `model_unet_agri_western_cape_v1`
would have two docker image tags published on Docker Hub:

* `model_unet_agri_western_cape:1` for cpu inferencing
* `model_unet_agri_western_cape:1-gpu` for gpu inferencing

}}

Pull pre-built image from Docker Hub (recommended):

```bash
docker pull docker.io/radiantearth/crop-detection-dl:1
```

Or build image from source:

```bash
docker build -t radiantearth/crop-detection-dl:1}:1 -f Dockerfile .
```

## Run Model to Generate New Inferences

{{

:pushpin: Model developer: do not commit training data to the data folder on
this repo, this is only a placeholder to run the model locally for inferencing.

}}

1. Prepare your input and output data folders. The `data/` folder in this repository
    contains some placeholder files to guide you.

    * The `data/` folder must contain:
        * `input/chips` {{ Landsat, Maxar Open-Data 30cm, Sentinel-2, etc. }} imagery chips for inferencing:
            * File name: {{ `chip_id.tif` }} e.g. {{ `0fec2d30-882a-4d1d-a7af-89dac0198327.tif` }}
            * File Format: {{ GeoTIFF, 256x256 }}
            * Coordinate Reference System: {{ WGS84, EPSG:4326 }}
            * Bands: {{ 3 bands per file:
                * Band 1 Type=Byte, ColorInterp=Red
                * Band 2 Type=Byte, ColorInterp=Green
                * Band 3 Type=Byte, ColorInterp=Blue
                }}
        * `/input/checkpoint` the model checkpoint {{ file | folder }}, `{{ checkpoint file or folder name }}`.
            Please note: the model checkpoint is included in this repository.
    * The `output/` folder is where the model will write inferencing results.

2. Set `INPUT_DATA` and `OUTPUT_DATA` environment variables corresponding with
    your input and output folders. These commands will vary depending on operating
    system and command-line shell:

    ```bash
    # change paths to your actual input and output folders
    export INPUT_DATA="/home/my_user/{{repository_name}}/data/input/"
    export OUTPUT_DATA="/home/my_user/{{repository_name}}/data/output/"
    ```

3. Run the appropriate Docker Compose command for your system:

    ```bash
    # cpu
    docker compose up {{stac.id}}_cpu
    # NVIDIA gpu driver
    docker compose up {{stac.id}}_gpu
    ```

4. Wait for the `docker compose` to finish running, then inspect the
`OUTPUT_DATA` folder for results.

## Understanding Output Data

Please review the model output format and other technical details in the [model
documentation](/docs/index.md).
