"""Kaggle API client for downloading/uploading datasets."""

import kaggle

class KaggleClient:
    """Kaggle API client"""

    def __init__(self):
        kaggle.api.authenticate()

    def download_dataset(self, dataset_name: str, path: str):
        """Download dataset"""
        kaggle.api.dataset_download_files(dataset_name, path, unzip=True)

    def upload_dataset(self, path: str):
        """Upload dataset"""
        kaggle.api.dataset_create_version(path)
