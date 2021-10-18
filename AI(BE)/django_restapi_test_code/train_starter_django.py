import requests
import argparse
import getpass
from multiprocessing import Process


from utils import login
    

def upload(args, token):
    # url = 'http://52.14.108.141:8080/deeplearning/train'
    # file_id
    if args.file_path:
        file = {'file': open(args.file_path, 'rb')}
        r = requests.post(args.upload_url, files=file, headers={'Authorization': f'Bearer {token}'})
    

SERVER_IP = 'http://3.143.240.128:8080'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--upload_url', '-u', default=f'{SERVER_IP}/deeplearning/files')
parser.add_argument('--train_url', '-t', default=f'{SERVER_IP}/deeplearning/train')
parser.add_argument('--login_url', '-l', default=f'{SERVER_IP}/account/login')
parser.add_argument('--file_path', '-f')

args = parser.parse_args()

def main(args):
    if args.file_path and args.file_path.split('.')[-1] != 'zip':
        print('unsupported file type')
        return
    
    token = login(args)
    
    p = Process(target=upload, args=(args, token, ))
    p.start()
    print(f'upload {args.file_path}...')
    p.join()
    
    r = eval(requests.post(args.train_url, headers={'Authorization': f'Bearer {token}'}).text)
    print(f'train model with {r["file"]}')

main(args)