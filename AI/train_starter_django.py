import requests
import argparse
import getpass
from multiprocessing import Process

def login(args):
    username = input('username: ')
    password = getpass.getpass('password: ')
    
    json = {'username': username, 'password': password}
    r = eval(requests.post(args.login_url, json=json).text)
    
    return r['token']
    

def train(args, token):
    # url = 'http://52.14.108.141:8080/deeplearning/train'
    # file_id
    
    file = {'file': open(args.file_path, 'rb')}
    r = requests.post(args.upload_url, files=file, headers={'Authorization': f'Bearer {token}'})
    
    
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--upload_url', '-u', default='http://52.14.108.141:8080/deeplearning/upload')
parser.add_argument('--train_url', '-t', default='http://52.14.108.141:8080/deeplearning/train')
parser.add_argument('--login_url', '-l', default='http://52.14.108.141:8080/account/login')
parser.add_argument('--file_path', '-f')

args = parser.parse_args()

def main(args):
    if args.file_path.split('.')[-1] != 'zip':
        print('unsupported file type')
        return
    
    token = login(args)
    
    p = Process(target=train, args=(args, token, ))
    p.start()
    print(f'upload {args.file_path}...')
    p.join()
    
    r = eval(requests.post(args.train_url, headers={'Authorization': f'Bearer {token}'}).text)
    print(f'train model with {r["file"]}')

main(args)