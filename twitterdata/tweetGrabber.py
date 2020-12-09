import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()
client_key = os.environ.get('client_key');
client_secret= os.environ.get('client_secret');

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# Check status code okay
#print(auth_resp.status_code)

# Keys in data response are token_type (bearer) and access_token
access_token = auth_resp.json()['access_token']

# Init search
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
#i.e. 'BRFS3'
searchWords=os.environ.get('subject');
sinceDate= '2020-08-26'
language='pt'

search_params = {
    'q': searchWords,
    'lang':'pt',
    'result_type': 'recent',
    'since': sinceDate,
    'count': 3 # how many returns are we looking for - Vai Giorgenes!
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)
tweet_data = search_resp.json()

print(len(tweet_data))
print(search_resp.json())


for x in tweet_data['statuses']:
    print('--------------------------')
    print(x['created_at'] + '\n')
    print(x['text'] + '\n')
    #print(x + '\n')
