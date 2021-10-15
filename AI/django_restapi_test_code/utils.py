import getpass
import requests


def login(args):
    username = input('username: ')
    password = getpass.getpass('password: ')
    
    json = {'username': username, 'password': password}
    r = eval(requests.post(args.login_url, json=json).text)
    
    return r['token']