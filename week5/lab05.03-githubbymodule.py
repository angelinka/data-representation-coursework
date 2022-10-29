import requests
from github import Github
from configGit import config as cfg

apikey = cfg["gitHubToken"]
# use your own key
g = Github(apikey)

#for repo in g.get_user().get_repos():
 #print(repo.name)

repo = g.get_repo("angelinka/aprivateone")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contenetOfFile = response.text
#print(contenetOfFile)

newContents = contenetOfFile + " more stuff \n"


gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)