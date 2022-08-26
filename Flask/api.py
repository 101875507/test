import requests
import json
url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'
parameters = {'key':'ddf5ca77bf02ec0fc3e06182ef83041b','city':'北京'}
a = requests.get(url=url,params=parameters).json()
#a =json.load(requests.get(url=url,params=parameters).json())
print(a.get('lives'))
