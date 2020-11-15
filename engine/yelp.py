import requests
# from YelpAPI import get_my_key
import json
from google.cloud import datastore

CLIENT_ID = 'swrB5WT4LC7GpVWC3WCTGA'
API_KEY = 'nRoY-Rsbta12-uZh6QzM3SxTnkSTwlWNF-mFsIjs-KMNi02KE5EZACwVC_mdzzoPwydaQW2C2rzOCGEJi3PvXZCmuvnoZKtjCN4MgaVfb9d_RdsNLHKmUGnHH2ywX3Yx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
PARAMETERS = {'term': 'restuarant','location': 'Toronto'}
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

response = requests.get(url = ENDPOINT,
                        params = PARAMETERS, 
                        headers = HEADERS)


# Conver the JSON String
business_data = response.json()

# print the response
# print(json.dumps(business_data, indent = 3))


# req = requests.get(SAMPLE_SCHEDULE_API)
data = json.loads(response.text)
# data = json.loads(data_json)
print (data['businesses'])

client = datastore.Client()
kind = 'Restaurant'
for b in data['businesses']:
    print(b['name'])
    b_id = b['id']
    item_key = client.key(kind, b_id)

    item = datastore.Entity(key=item_key)
    item.update(b)
    client.put(item)




