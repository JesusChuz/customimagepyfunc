import logging

import azure.functions as func
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
    
    datastore = Datastore.get(ws, "workspaceblobstore")
    logging.info("got datastore")
    logging.info(datastore)

    logging.info("compute target set")

    all_ds = Dataset.get_all(ws)
    logging.info("got all datasets")
    logging.info(all_ds)

    dstwo = Dataset.get_by_name(ws, name='jesumeWS')
    dstwo.download(target_path='.', overwrite=False)
    logging.info("got dataset")
