import requests

response = requests.get('https://punapi.rest/api/pun')
if response:
    print(response.text)
else:
    print('An error has occurred.')
