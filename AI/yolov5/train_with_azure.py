import os
import shutil
import json

from azureml.core.workspace import Workspace
from azureml.core import Experiment
from azureml.core import Environment

from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException
from azureml.core.authentication import InteractiveLoginAuthentication

from azureml.core import ScriptRunConfig
from azureml.core.runconfig import DockerConfiguration

with open('./azure_config.json') as json_file:
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

project_folder = './clone_code'

try:
    compute_target = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing compute target')
except ComputeTargetException:
    print('Not Found Exsiting Target Cluster')

# Specify a GPU base image
DEPLOY_CONTAINER_FOLDER_PATH = 'clone_code'
SCRIPT_FILE_TO_EXECUTE = 'train.py'
PATH_TO_YAML_FILE='./conda_dependencies.yml'

pytorch_env = Environment.from_conda_specification(name='pytorch_env', file_path=PATH_TO_YAML_FILE)
#pytorch_env.docker.enabled = True

pytorch_env.docker.base_image = None
pytorch_env.docker.base_dockerfile = "./Dockerfile"

# Finally, use the environment in the ScriptRunConfig:
src = ScriptRunConfig(source_directory=DEPLOY_CONTAINER_FOLDER_PATH,
                      script=SCRIPT_FILE_TO_EXECUTE,
                      arguments=['--img', 640, '--batch', 16, '--epochs', 300, '--data', 'data/dataset.yaml', '--weights', 'yolov5l6.pt'],
                      compute_target=compute_target,
                      environment=pytorch_env)

run = Experiment(ws, name='canary_yolov5').submit(src)
run.wait_for_completion(show_output=True)

os.makedirs('./model', exist_ok=True)

# Download the model from run history