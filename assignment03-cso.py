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

def getAll():
    response = requests.get(url)
    return response.json()
    
def saveToFile():
    with open("cso.json", 'wt') as fp:
        print(json.dumps(getAll()), file=fp)

if __name__ == "__main__":
    saveToFile()