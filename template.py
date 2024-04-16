import sys
import os
import logging
import pathlib
from pathlib import Path

#Name of the project
project_name = 'store_demand_forecasting'

#list of files to be created for project
list_of_files = [
    
                f'src/{project_name}/__init__.py',
                f'src/{project_name}/components/data_ingestion.py',
                f'src/{project_name}/components/data_transformation.py',
                f'src/{project_name}/components/data_validation.py',
                f'src/{project_name}/components/data_evaluation.py',
                f'src/{project_name}/components/model_pusher.py',
                f'src/{project_name}/components/model_trainer.py',
                f'src/{project_name}/utils/__init__.py',
                f'src/{project_name}/utils/common.py',
                f'src/{project_name}/logger/__init__.py',
                f'src/{project_name}/pipeline/__init__.py',
                f'src/{project_name}/pipeline/training_pipeline.py',
                f'src/{project_name}/pipeline/prediction_pipeline.py',
                f'src/{project_name}/entity/__init__.py',
                f'src/{project_name}/constants/__init__.py',
                f'config/config.yaml', 
                f'params.yaml', 
                f'app.py', 
                f'Dockerfile', 
                f'requirements.txt', 
                f'setup.py', 
                f'research/data_ingestion.ipynb', 
                f'research/data_transformation.ipynb', 
                f'research/model_evaluation.ipynb', 
                f'research/model_trainer.ipynb', 
                f'research/trail.ipynb', 
                
                ]



for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filepath} for the file {filename}")


    if (not os.path.exists(filepath)) or  (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")