import json
import requests
from instagram_data_api import get_comments, business_discovery

def load_publications():
    path = '/Users/gerardovitaleerrico/Documents/DataCamp/chat-api/helpers/instagram_data_api/responses/gerardovitale_posts.json'
    with open(path, mode='r') as json_file:
        publications = json.load(json_file)
        # print(publications)
    publications = [dic for dic in publications['json_data']['data']]
    params = get_comments.getCreds() # get creds
    url = 'http://127.0.0.1:5000/publications'
    for pub in publications:
        media_id = pub['id']
        response = get_comments.get_comments(params, media_id) # get insights for a specific media id
        pub['comments'] = [json.dumps(dic) for dic in response['json_data']['data']]
        requests.post(url, data=pub) 

load_publications()