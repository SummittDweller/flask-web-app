import requests 
import json
# api-endpoint 
API_ENDPOINT =  "https://deploying-flask-web-app.azurewebsites.net/predict_api"
  
data=[[1,0]]
# sending get request and saving the response as response object 
r = requests.post(url = API_ENDPOINT, json = data)   
# extracting data in json format 
data = r.json() 
print(r)
print(data)
print(data['results'])