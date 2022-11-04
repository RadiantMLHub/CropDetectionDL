"""
Download training dataset from MLHub to local machine.
"""
from radiant_mlhub import Dataset
from pathlib import Path


ref_african_crops_kenya_02 = Dataset.fetch('ref_african_crops_kenya_02')
ref_african_crops_kenya_02.download(
    output_dir=Path.home() / 'data'
)
