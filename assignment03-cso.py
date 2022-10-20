'''
Assignment 03 for Data representation module
Author: Angelina Belotserkovskaya

Task: Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO,
and stores it into a file called "cso.json"

RESTful API URL:
https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en
'''

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response = requests.get(url)
data = response.json()
#print(data)

with open("cso.json", 'wt') as fp:
    json.dump(data, fp)