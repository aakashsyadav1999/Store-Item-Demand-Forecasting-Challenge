import pandas as pd
import numpy as np
from dataclasses import dataclass
import os
from zipfile import ZipFile
from pathlib import Path
import urllib.request as request
import requests
import zipfile

from src.store_demand_forecasting.constants import *
from src.store_demand_forecasting.entity.artifact_entity import DataIngestionArtifacts,DataTransformationArtifacts
from src.store_demand_forecasting.entity.config_entity import DataIngestionConfig,DataTransformationConfig

from src.store_demand_forecasting.logger import logging
from src.store_demand_forecasting.exception import NerException
from src.store_demand_forecasting.utils.common import MainUtils


class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig,data_ingestion_artifacts = DataIngestionArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts


    def clean_raw_data(self):
        
        logging.info(f'Entered into cleaning module of {self.data_transformation_config.read_csv}')
        try:
            df = pd.read_csv(self.data_transformation_config.read_csv)
            print(df.info())
            print(df.describe())
            return df
        except Exception as e:
            print(e)

    def save_data(self):

        try:
            logging.info("Saving file to target location")
            
        except Exception as e:
            print(e)

    