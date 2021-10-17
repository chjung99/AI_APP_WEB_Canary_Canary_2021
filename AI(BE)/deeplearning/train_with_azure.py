import os
import shutil
import json
import time
import csv
import numpy as np
from numpy import genfromtxt

from azureml.core import Experiment, ScriptRunConfig, Environment
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.runconfig import DockerConfiguration
from azureml.core.workspace import Workspace
from azureml.core.compute_target import ComputeTargetException
from azureml.core.authentication import InteractiveLoginAuthentication


from .models import TrainedModel

def fitness(x):
    # Model fitness as a weighted combination of metrics
    w = [0.0, 0.0, 0.1, 0.9]  # weights for [P, R, mAP@0.5, mAP@0.5:0.95]
    
    if x.ndim == 1:
        return (x[:4] * w).sum()
    else:
        return (x[:, :4] * w).sum(1)
        

def train(download_url, epoch=1):
    with open('./deeplearning/kwoledge_distillation_yolov5/azure_config.json') as json_file:
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
    
    project_folder = './deeplearning/kwoledge_distillation_yolov5/yolov5'
    
    try:
        compute_target = ComputeTarget(workspace=ws, name=cluster_name)
        print('Found existing compute target')
    except ComputeTargetException:
        print('Not Found Exsiting Target Cluster')
    
    # Specify a GPU base image
    DEPLOY_CONTAINER_FOLDER_PATH = 'deeplearning/kwoledge_distillation_yolov5/yolov5'
    SCRIPT_FILE_TO_EXECUTE = 'train.py'
    PATH_TO_YAML_FILE='./deeplearning/kwoledge_distillation_yolov5/conda_dependencies.yml'
    
    pytorch_env = Environment.from_conda_specification(name='pytorch_env', file_path=PATH_TO_YAML_FILE)
    #pytorch_env.docker.enabled = True
    
    pytorch_env.docker.base_image = None
    pytorch_env.docker.base_dockerfile = "./deeplearning/kwoledge_distillation_yolov5/Dockerfile"
    
    
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
    
    print(os.getcwd())
    
    
    results = genfromtxt(results_path, delimiter=',', skip_header = 1)
    
    if results.ndim == 1:
        results = results[4:8]
    else:
        results = results[:, 4:8]
        
    
    best = 0
    
    best = max(fitness(results), best)
    
    train_model = TrainedModel()
    train_model.file.name = model_path.split('/')[-1]
    train_model.result.name = results_path.split('/')[-1]
    train_model.matrix = best
    
    train_model.save()
    
# Download the model from run history