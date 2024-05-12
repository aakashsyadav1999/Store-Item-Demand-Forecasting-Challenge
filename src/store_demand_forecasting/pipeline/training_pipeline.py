import sys
import stat
from src.store_demand_forecasting.constants import *

from src.store_demand_forecasting.entity.artifact_entity import (
    DataIngestionArtifacts
    )

from src.store_demand_forecasting.components.data_ingestion import DataIngestion
from src.store_demand_forecasting.components.data_transformation import DataTransformation
from src.store_demand_forecasting.entity.config_entity import (
    DataIngestionConfig,DataTransformationConfig
    
)


from src.store_demand_forecasting.exception import NerException
from src.store_demand_forecasting.logger import logging

#Class create to start all the process which is in components.
class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()

    #Permission for directory to read, write, delete    
    def create_directory_with_permissions(self, directory_path):
        try:
            os.makedirs(directory_path, exist_ok=True)
            os.chmod(directory_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # Set permissions for owner, group, and others
            logging.info(f"Directory '{directory_path}' created successfully.")
        except Exception as e:
            raise NerException(e, sys) from e


     # This method is used to start the data ingestion
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from Google cloud storage")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from Google cloud storage")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact

        except Exception as e:
            raise NerException(e, sys) from e

    #This method is starting data transformation
    def start_data_transformation(self) -> DataTransformationConfig:
        logging.info("Entered Data Transformation method in training pipeline")
        try:
            directory_path = self.data_transformation_config.data_transformation_dir
            self.create_directory_with_permissions(directory_path)
            logging.info(f"Creating {directory_path}")

            logging.info("Starting Data Transformation")
            #Make object of data transformation config and all the initate data transformation function.
            data_transformation = DataTransformation(
                data_transformation_config=self.data_transformation_config
            )
            #call function
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info("Cleaned Data")
            logging.info("Exited the data_transformation method of TrainPipeline class")
            return data_transformation_artifact
        except Exception as e:
            raise NerException(e, sys) from e


    # This method is used to start the training pipeline
    def run_pipeline(self) -> None:
        try:
            logging.info("Started Model training >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            #data_ingestion_artifact = self.start_data_ingestion()
            data_transformation_artifact = self.start_data_transformation()
        except Exception as e:
            raise e