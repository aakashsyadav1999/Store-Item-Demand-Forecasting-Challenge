from dataclasses import dataclass
import os
from zipfile import ZipFile
from pathlib import Path
import urllib.request as request
import requests
import zipfile

from src.store_demand_forecasting.constants import *
from src.store_demand_forecasting.entity.artifact_entity import DataIngestionArtifacts
from src.store_demand_forecasting.entity.config_entity import DataIngestionConfig

from src.store_demand_forecasting.logger import logging
from src.store_demand_forecasting.exception import NerException
from src.store_demand_forecasting.utils.common import MainUtils

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig) -> None:

        self.data_ingestion_config = data_ingestion_config


    def download_file(self):
        if not os.path.exists(self.data_ingestion_config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.data_ingestion_config.source_url,
                filename = self.data_ingestion_config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"File already exists of size: {MainUtils.get_size(Path(self.data_ingestion_config.local_data_file))}")  


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.data_ingestion_config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            with zipfile.ZipFile(self.data_ingestion_config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except zipfile.BadZipFile as e:
            print(f"BadZipFile Error:{e}")
        

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of the data ingestion class")
        try:
            os.makedirs(
                self.data_ingestion_config.data_ingestion_artifacts_dir,exist_ok=True
            )
            logging.info(f"Creating {(self.data_ingestion_config.data_ingestion_artifacts_dir)} directory")

            #Downloading data from given URL
            self.download_file()
            logging.info(f"Downloading data from given url {self.data_ingestion_config.source_url}")

            #extract file
            self.extract_zip_file()
            logging.info(f"Extracting file in directory {self.data_ingestion_config.local_data_file}")

        except Exception as e:
            raise e