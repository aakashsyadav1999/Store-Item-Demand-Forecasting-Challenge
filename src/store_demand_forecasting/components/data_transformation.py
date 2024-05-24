import pandas as pd
import time
import numpy as np
from dataclasses import dataclass
import os
import stat

from src.store_demand_forecasting.constants import *
from src.store_demand_forecasting.entity.artifact_entity import DataTransformationArtifacts
from src.store_demand_forecasting.entity.config_entity import DataTransformationConfig
from src.store_demand_forecasting.logger import logging

from sklearn.model_selection import train_test_split


#class for initiating all methods
class DataTransformation:

    def __init__(self,data_transformation_config:DataTransformationConfig,data_transformation_artifacts = DataTransformationArtifacts):
        self.data_transformation_config = data_transformation_config
        self.data_transformation_artifacts = data_transformation_artifacts


    #funtion for cleaning unwanted parts from data
    def clean_raw_data(self):
        
        logging.info(f'Entered into cleaning module of {self.data_transformation_config.read_csv}')
        try:
            df = pd.read_csv(self.data_transformation_config.read_csv)
            print(df.info())
            print(df.describe())
            return df
        except Exception as e:
            print(e)


    def split_train_test_split(self,df):
        try:
            df = pd.read_csv(self.data_transformation_config.read_csv)
            train,test = train_test_split(df,test_size=0.2,random_state=42)

            train.to_csv(os.path.join(self.data_transformation_config.data_transformation_dir,'train.csv'),index=False)
            test.to_csv(os.path.join(self.data_transformation_config.data_transformation_dir,'test.csv'),index=False)
            
            logging.info("Data splitted into train and test data.")
            logging.info(f'Shape of train data is {train.shape}')
            logging.info(f'Shape of test data is {test.shape}')
        
            return train, test
        
        except Exception as e:
            logging.error(f"Error in split_train_test_data: {e}")
            raise


    #saving data into allowed path for model training and model prediction.
    def save_data(self, df):
        try:
            logging.info("Saving file to target location")
            save_path = self.data_transformation_config.final_file_name
            df.to_csv(save_path, index=False)
            logging.info(f"Data saved successfully at {save_path}")
            return save_path
        except Exception as e:
            print(e)

    #initiate all the methods which are mentioned above.
    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        logging.info("Entered the initiate_data_transformation method of the data ingestion class")
        try:
            os.makedirs(
                self.data_transformation_config.data_transformation_dir,exist_ok=True
            )
            os.chmod(self.data_transformation_config.data_transformation_dir,stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            logging.info(f"Creating {(self.data_transformation_config.data_transformation_dir)} directory")


            #Downloading data from given URL
            df = self.clean_raw_data()
            logging.info(f"Cleaning data")

            self.split_train_test_split(df)
            logging.info(f"Train-Test Split")

            #saving file
            final_data_file_path = self.save_data(df=df)
            logging.info(f"Saving data into the directory")

            # Return artifact
            data_transformation_artifact = DataTransformationArtifacts(final_data_file_path=final_data_file_path)
            logging.info(f"Saving data into the directory")
            return data_transformation_artifact

        except Exception as e:
            raise e