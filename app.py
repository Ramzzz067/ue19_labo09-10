import requests
import json

response = requests.get('https://punapi.rest/api/pun')
if response:
    data = json.loads(response.text)
    print(data["pun"])
else:
    print('An error has occurred.')
