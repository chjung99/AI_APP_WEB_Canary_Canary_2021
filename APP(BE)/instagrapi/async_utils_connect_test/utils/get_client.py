from instagrapi import *
import json

def get_logined_client(cl, instagramID, instagramPW):
    try:
        cl.account_info()
    except:
        cl.login(instagramID,instagramPW)
with open('/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/utils/instagram_config.json') as json_file:
    instagram_config = json.load(json_file)
id = instagram_config['id']
password = instagram_config['password']