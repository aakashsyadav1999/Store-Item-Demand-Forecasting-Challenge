import pandas as pd
import numpy as np
from dataclasses import dataclass
import os
import stat

from src.store_demand_forecasting.constants import *
from src.store_demand_forecasting.entity.config_entity import ModelTrainerConfig
from src.store_demand_forecasting.logger import logging


import lightgbm as lgb
from sklearn.metrics import mean_absolute_error
import joblib

#class for initiating all methods
class ModelTrainer:

    def __init__(self,model_trainer_config:ModelTrainerConfig):
    
        self.model_trainer_config = model_trainer_config

    def train(self):

        train_data = pd.read_csv(self.model_trainer_config.train_data)
        test_date = pd.read_csv(self.model_trainer_config.test_data)

        df = pd.read_csv(self.model_trainer_config.master_data)

        # Train set until the beginning of 2017 (until the end of 2016).
        train = df.loc[(df["date"] < "2017-01-01"), :]

        # First three months of 2017 validation set.
        val = df.loc[(df["date"] >= "2017-01-01") & (df["date"] < "2017-04-01"), :]

        cols = [col for col in train.columns if col not in ['date', 'id', "sales", "year"]]

        # Selecting the dependent and independent variable for the train set
        Y_train = train['sales']
        X_train = train[cols]

        # Choosing the dependent and independent variable for the validation set
        Y_val = val['sales']
        X_val = val[cols]

        cols = [col for col in train.columns if col not in ['date', 'id', "sales", "year"]]

        # Train set: rows where sales is not NaN
        train = df.loc[~df.sales.isna()]
        Y_train = train['sales']
        X_train = train[cols]

        # Test set: rows where sales is NaN
        test = df.loc[~df.sales.isna()]
        X_test = test[cols]

        # Ensure X_test is not empty and is 2D
        if X_test.empty:
            raise ValueError("X_test is empty. Check your dataframe and feature columns.")
        if len(X_test.shape) != 2:
            raise ValueError("X_test must be a 2-dimensional array.")

        # LightGBM parameters
        lgb_params = self.model_trainer_config.params

        # LightGBM dataset
        lgbtrain_all = lgb.Dataset(data=X_train, label=Y_train, feature_name=cols)

        # Train the model
        model = lgb.train(lgb_params, lgbtrain_all, num_boost_round=100)

        # Predict using the model
        test_preds = model.predict(X_test)

        # Print predictions
        print(test_preds)

        # Assuming you have a validation set to check the accuracy
        # Create a validation set (e.g., the first three months of 2017)
        val = df.loc[(df["date"] >= "2017-01-01") & (df["date"] < "2017-04-01"), :]

        val = test.loc[(df["date"] >= "2017-01-01") & (df["date"] < "2017-04-01") & ~df.sales.isna()]
        Y_val = val['sales']
        X_val = val[cols]

        # Predict on validation set
        val_preds = model.predict(X_val)

        # Calculate and print MAE on validation set
        mae_val = mean_absolute_error(Y_val, val_preds)
        print(f'Mean Absolute Error on validation set: {mae_val}')

        joblib.dump(model, os.path.join(self.model_trainer_config.model_trainer_dir, self.model_trainer_config.model_name))

    def initiate_model_trainer(self):

        logging.info("Entered the initiate_data_transformation method of the data ingestion class")
        try:
            os.makedirs(
                self.model_trainer_config.model_trainer_dir,exist_ok=True
            )

            self.train()
            
        except Exception as e:
            raise e


