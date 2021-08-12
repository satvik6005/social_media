import requests
import json



url = 'http://127.0.0.1:8000/api/login'
dic={'username':'mansig1998@gmail.com','password':'charu123'}
r = requests.post(url=url,data=dic)
print(r.json())