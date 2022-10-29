# In this lab we will write a module to interact with the API at
# http://andrewbeatty1.pythonanywhere.com/books
# author: Angelina Belotserkovskaya

from urllib import response
import requests
#import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def readAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + '/' + str(id)
    response = requests.get(geturl)
    return response.json()

def addBook(book):
    response = requests.post(url, json=book)
    # alternative, more complicated solution:
    #headers = {"Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    return response.json()

def updateBook(id, bookUpdate):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=bookUpdate)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__== "__main__":
    book = {
        'Author': "test",
        'Title': "a title",
        'Price': 111
    }
    bookUpdate={
        'Price': 500000
    }
    #print(readAllBooks())
    #print(getBookById(1))
    #print(deleteBook(95))
    #print(addBook(book))
    print(updateBook(106,bookUpdate))