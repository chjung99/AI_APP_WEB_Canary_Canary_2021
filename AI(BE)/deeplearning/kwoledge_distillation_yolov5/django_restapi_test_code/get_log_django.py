import requests
import argparse
from multiprocessing import Process

from utils import login
    


SERVER_IP = 'http://3.143.240.128:8080'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--login_url', '-l', default=f'{SERVER_IP}/account/login')
parser.add_argument('--log_url', '-u', default=f'{SERVER_IP}/deeplearning/log')

args = parser.parse_args()

def main(args):
    token = login(args)
    
    r = requests.get(args.log_url, headers={'Authorization': f'Bearer {token}'}).text
    r = eval(r.replace('null', 'None'))
    print(r['results'])
    
    for d in r['results']:
        print(f"[{d['create_at']}] {d['username']}: {d['log']}")

main(args)