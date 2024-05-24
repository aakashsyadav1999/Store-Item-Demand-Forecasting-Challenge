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
SOURCE_URL= "https://drive.google.com/file/d/12TOieo_IuboUIG25GmKjKh0G2q3UfBXA/view?usp=sharing"
UNZIP_DIR= ROOT_DIR
LOCAL_FILE_PATH = "sample_submission.zip"

#Data Transformation
DATA_TRANSFORMATION_DIR = "DataTransformationArtifacts"
TRANSFORMED_FILE_NAME = 'final.csv'
CSV_FILE_NAME = r'artifacts\DataTransformationArtifacts\train.csv'

#Model Trainer
LGB_PARAMS = {
    'metric': 'mae',
    'num_leaves': 10,
    'learning_rate': 0.02,
    'feature_fraction': 0.8,
    'max_depth': 5,
    'verbose': 0,
    'nthread': -1
}
MODEL_TRAINING_ARTIFACTS_DIR = "ModelTrainingArtifacts"
TRAIN_DATA = r'D:\VS code files\store_item_demand_forecasting_challenge\artifacts\DataTransformationArtifacts\train.csv'
TEST_DATA = r'D:\VS code files\store_item_demand_forecasting_challenge\artifacts\DataTransformationArtifacts\test.csv'
MASTER_DATA = r'D:\VS code files\store_item_demand_forecasting_challenge\artifacts\DataTransformationArtifacts\final.csv'
MODEL_NAME = 'model.joblib'


APP_HOST = "0.0.0.0"
APP_PORT = 8080
