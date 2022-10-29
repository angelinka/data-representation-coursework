import requests
import json
from configGit import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/angelinka/aprivateone'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["gitHubToken"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())


with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
