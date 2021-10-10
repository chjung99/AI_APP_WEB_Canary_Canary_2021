import requests
import argparse
from multiprocessing import Process

def train(args):
    # url = 'http://52.14.108.141:8080/deeplearning/train'
    # file_id
    
    file = {'file': open(args.file_path, 'rb')}
    r = requests.post(args.upload_url, files=file)
    
    print(r.text)
    
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--upload_url', '-u', default='http://52.14.108.141:8080/deeplearning/upload')
parser.add_argument('--train_url', '-t', default='http://52.14.108.141:8080/deeplearning/train')
parser.add_argument('--file_path', '-f')

args = parser.parse_args()

def main(args):
    if args.file_path.split('.')[-1] != 'zip':
        print('unsupported file type')
        return
    p = Process(target=train, args=(args,))
    p.start()
    print('upload dataset...')
    p.join()
    
    r = requests.post(args.train_url)
    print(r.text)

main(args)