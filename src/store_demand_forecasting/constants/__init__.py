import os
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join("artifacts")
LOGS_DIR = "logs"
LOGS_FILE_NAME = "SIDFC.log"
MODELS_DIR = "models"
BEST_MODEL_DIR = "best_model"

# Data Ingestion 
ROOT_DIR= "DataIngestionArtifacts"
SOURCE_URL= "https://github.com/aakashsyadav1999/Store-Item-Demand-Forecasting-Challenge/blob/main/research/demand-forecasting-kernels-only.zip"
UNZIP_DIR = ROOT_DIR
LOCAL_FILE_PATH = "demand-forecasting-kernels-only.csv"

#Data Transformation
DATA_TRANSFORMATION_DIR = "DataTransformationArtifacts"
TRANSFORMED_FILE_NAME = 'final.csv'
CSV_FILE_NAME = r'D:\VS code files\store_item_demand_forecasting_challenge\artifacts\DataIngestionArtifacts\train.csv'