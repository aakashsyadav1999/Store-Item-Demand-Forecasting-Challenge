from dataclasses import dataclass
import os
from pathlib import Path
import sys
from src.store_demand_forecasting.constants import *
from src.store_demand_forecasting.entity.artifact_entity import *
from src.store_demand_forecasting.entity.config_entity import *
#Data Ingestion
@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.data_ingestion_artifacts_dir:str = os.path.join(
            ARTIFACTS_DIR,ROOT_DIR
        )
        self.source_url:str = SOURCE_URL
        self.local_data_file:str = os.path.join(
            self.data_ingestion_artifacts_dir,LOCAL_FILE_PATH
        )
        self.unzip_dir:str = os.path.join(
            self.data_ingestion_artifacts_dir
        )