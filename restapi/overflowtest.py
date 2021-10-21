import requests
import json
#install flask
#install flask-sqlalchemy
response=requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')


for data in response.json()['items']:
    if data['answer count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print('skipped')
    print()