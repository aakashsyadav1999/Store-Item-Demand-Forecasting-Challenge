import sys
from src.store_demand_forecasting.constants import *

from src.store_demand_forecasting.entity.artifact_entity import (
    DataIngestionArtifacts
    )

from src.store_demand_forecasting.components.data_ingestion import DataIngestion
from src.store_demand_forecasting.entity.config_entity import (
    DataIngestionConfig,
    
)


from src.store_demand_forecasting.exception import NerException
from src.store_demand_forecasting.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    
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
       # This method is used to start the training pipeline
    def run_pipeline(self) -> None:
        try:
            logging.info("Started Model training >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise e