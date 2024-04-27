import os
import sys
from src.store_demand_forecasting.exception import NerException
from src.store_demand_forecasting.pipeline.training_pipeline import TrainPipeline
from src.store_demand_forecasting.constants import *


def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise NerException(e, sys) from e


if __name__ == "__main__":
    training()



