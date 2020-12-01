import json
import requests
from instagram_data_api import business_discovery

def load_user(var='file'):
    url = 'http://127.0.0.1:5000/users/'
    if var == 'file':
        path = '/Users/gerardovitaleerrico/Documents/DataCamp/chat-api/helpers/instagram_data_api/responses/gerardovitale_profile.json'
        with open(path, mode='r') as json_file:
            response = json.load(json_file)
            # print(user_profile)
    else:
        params = business_discovery.getCreds(ig_username=var)
        response = business_discovery.getAccountInfo(params)
        
    user_profile = response['json_data']['business_discovery']
    requests.post(url, data=user_profile)

load_user(var='carola.vitale')