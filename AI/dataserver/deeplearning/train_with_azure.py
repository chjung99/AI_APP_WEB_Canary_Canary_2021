import os
import shutil
import json
import time

from azureml.core.workspace import Workspace
from azureml.core import Experiment
from azureml.core import Environment

from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException
from azureml.core.authentication import InteractiveLoginAuthentication

from azureml.core import ScriptRunConfig
from azureml.core.runconfig import DockerConfiguration

from .models import TrainedModel

def train(download_url, epoch=300):
    with open('./deeplearning/kwoledge_distillation/azure_config.json') as json_file:
        azure_config = json.load(json_file)
    
    interactive_auth = InteractiveLoginAuthentication(tenant_id=azure_config['interactive_auth'])
    subscription_id = azure_config['subscription_id']
    resource_group  = azure_config['resource_group']
    workspace_name  = azure_config['workspace_name']
    cluster_name = azure_config['cluster_name']
    
    try:
        ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
        ws.write_config()
        print('Library configuration succeeded')
    except:
        print('Workspace not found')
    
    project_folder = './deeplearning/kwoledge_distillation/clone_code'
    
    try:
        compute_target = ComputeTarget(workspace=ws, name=cluster_name)
        print('Found existing compute target')
    except ComputeTargetException:
        print('Not Found Exsiting Target Cluster')
    
    # Specify a GPU base image
    DEPLOY_CONTAINER_FOLDER_PATH = 'deeplearning/kwoledge_distillation/clone_code'
    SCRIPT_FILE_TO_EXECUTE = 'train.py'
    PATH_TO_YAML_FILE='./deeplearning/kwoledge_distillation/conda_dependencies.yml'
    
    pytorch_env = Environment.from_conda_specification(name='pytorch_env', file_path=PATH_TO_YAML_FILE)
    #pytorch_env.docker.enabled = True
    
    pytorch_env.docker.base_image = None
    pytorch_env.docker.base_dockerfile = "./deeplearning/kwoledge_distillation/Dockerfile"
    
    
    # Finally, use the environment in the ScriptRunConfig:
    src = ScriptRunConfig(source_directory=DEPLOY_CONTAINER_FOLDER_PATH,
                          script=SCRIPT_FILE_TO_EXECUTE,
                          arguments=['--img', 640, '--batch', 32, '--epochs', epoch, '--data', 'data/dataset.yaml', '--weights', 'yolov5m6.pt', '--data_url', download_url],
                          compute_target=compute_target,
                          environment=pytorch_env)
    
    run = Experiment(ws, name='canary_yolov5_knowledge_distillation').submit(src)
    run.wait_for_completion()
    
    cur_time = time.time()
    model_path = f'./media/model_{cur_time}.pt'
    results_path = f'./media/results_{cur_time}.csv'
    
    if not os.path.exists('./media'):
        os.makedirs('./media')
    
    print("download_files")
    run.download_file(name='outputs/best.pt', output_file_path=model_path)
    run.download_file(name='outputs/results.csv', output_file_path=results_path)
    
    train_model = TrainedModel()
    train_model.file.name = model_path
    train_model.result.name = results_path
    
    train_model.save()
    
# Download the model from run history