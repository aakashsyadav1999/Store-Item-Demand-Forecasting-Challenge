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

    def __init__ (self):
        self.data_ingestion_artifacts_dir:str = os.path.join(
            ARTIFACTS_DIR,ROOT_DIR
        )

        self.source_url:str = SOURCE_URL

        self.local_data_file:str = os.path.join(
            self.data_ingestion_artifacts_dir,LOCAL_FILE_PATH
        )

        self.unzip_dir:str = UNZIP_DIR


#Data Transformation
@dataclass
class DataTransformationConfig:

    def __init__ (self):
        self.data_transformation_dir:str = os.path.join(
            ARTIFACTS_DIR,DATA_TRANSFORMATION_DIR
        )
        self.final_file_name: str = os.path.join(
            self.data_transformation_dir,TRANSFORMED_FILE_NAME
        )
        self.read_csv:str = CSV_FILE_NAME


#Model Trainer 
@dataclass
class ModelTrainerConfig:

    def __init__(self):
        self.model_trainer_dir:str = os.path.join(
            ARTIFACTS_DIR,MODEL_TRAINING_ARTIFACTS_DIR
        )
        
        self.params = LGB_PARAMS
        
        self.master_data:Path = MASTER_DATA

        self.train_data:Path = TRAIN_DATA
        
        self.test_data:Path = TEST_DATA

        self.model_name:str = MODEL_NAME
