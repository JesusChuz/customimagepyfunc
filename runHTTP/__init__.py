import logging

import azure.functions as func
import pandas as pd
from io import BytesIO, StringIO
import csv
from azureml.core import Workspace
from azureml.core import Datastore
from azureml.core import Experiment
from azureml.core import Dataset
from azureml.core.authentication import MsiAuthentication

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
      
    msi_auth = MsiAuthentication()
    ws = Workspace.get(name="jesume-ml-functionapp",
                    subscription_id='bddf3c59-769c-49a7-a515-6310ce264e6a', 
                    resource_group='jesume-ML-PythonFunc',
                    auth = msi_auth
                    )

    logging.info("got workspace")
    
    # get the datastore to upload prepared data
    datastore = Datastore.get(ws, "workspaceblobstore")
    logging.info("got datastore")
    logging.info(datastore)

    #exp = Experiment(workspace=ws, name="auto-2-2-21")
    #compute_target = ws.compute_targets["test-2-2-21"]

    logging.info("compute target set")

    #ds = Dataset.get_by_name(ws, 'test')
    #logging.info("dataset retrieved")
    #ds = Dataset.Tabular.from_delimited_files(path = [(datastore, ('auto-uplift-output/original_03-29-2021.csv'))],validate=False)
    all_ds = Dataset.get_all(ws)
    logging.info("got all datasets")
    logging.info(all_ds)

    dstwo = Dataset.get_by_name(ws, name='jesumeWS')
    dstwo.download(target_path='.', overwrite=False)
    logging.info("got dataset")





