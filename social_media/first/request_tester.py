import requests
import json



url = 'http://127.0.0.1:8000/api/data'
dic={'name':"satvik",'email':'mastergoyal2001@gmail.com','age':10}
r = requests.post(url=url,data=dic)
print(r)