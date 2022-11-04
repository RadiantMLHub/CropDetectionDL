#!/bin/bash
python prepare_data.py --data_path $INPUT_DATA_VOLUME;
python main.py --data_path $OUTPUT_DATA_VOLUME;
