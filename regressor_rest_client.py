import json
import requests

url = ' http://127.0.0.1:8000/model'
request_data = json.dumps({'OverallQual':4,'ExterQual':1,'BsmtQual':2,'TotalBsmtSF':1,'1stFlrSF':800,'GrLivArea':1000,'FullBath':1,'KitchenQual':3,'GarageCars':2,'GarageArea':800})
response = requests.post(url,request_data)
print(response.text)