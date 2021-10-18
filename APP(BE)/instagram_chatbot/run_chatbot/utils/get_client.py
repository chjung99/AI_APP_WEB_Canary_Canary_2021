from instagrapi import *
import json

def get_logined_client(cl):
    try:
        cl.account_info()
    except:
        with open('/workspaces/AI_APP_WEB_Canary_Canary/APP(BE)/instagrapi/async_utils_connect_test/utils/instagram_config.json') as json_file:
            instagram_config = json.load(json_file)
        id = instagram_config['id']
        password = instagram_config['password']
        cl.login(id, password)