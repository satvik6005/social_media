import requests
import json



url = 'http://127.0.0.1:8000/api/registration'
dic={'email':'officialwork.rahul@gmail.com','username':'chutiya','password':'rahul234','password2':'rahul234'}
r = requests.post(url=url,data=dic)
print(r)