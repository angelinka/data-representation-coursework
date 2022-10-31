'''
Assignment 04 for Data representation module
Author: Angelina Belotserkovskaya

Task: Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name.
The program should then commit those changes and push the file back to the repository.

'''
# Importing necessary modules. Note: you might need to install them first.
import requests
from github import Github
# Importing config file which contains token/key for GitHub
from configGit import config as cfg

# saving the key from config file
apikey = cfg["gitHubToken"]
# using it with GitHub libraty
g = Github(apikey)

# Passing account name and repo name. Note you can change it to youraccount/reponame
repo = g.get_repo("angelinka/aprivateone")

# Specifying name of the file where the string will be replaced. 
#original_file = "allAboutNames.txt"

# Getting contents of the file and download URL
fileInfo = repo.get_contents("allAboutNames.txt")
urlOfFile = fileInfo.download_url

# print (urlOfFile)
# Using URL to make a http request to the file 
response = requests.get(urlOfFile)
contentOfFile = response.text

with  open("original_file.txt", "w") as fp:
    fp.writelines(contentOfFile)

# credit to https://pythonexamples.org/python-replace-string-in-file/
# solution 1: making changes to the same file on GitHub

#read input file
fin = open("original_file.txt", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace('Andrew', 'Angelina')
#close the input file
fin.close()
#open the input file in write mode
fin = open("original_file.txt", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()

content = open("original_file.txt", "r").read()
gitHubResponse=repo.update_file(fileInfo.path,"Replaced name Andrew with Angelina",
content, fileInfo.sha)
print (gitHubResponse)
'''
# solution 2: using two files input file
fin = open("original_file.txt", "rt")
#output file to write the result to
fout = open("out.txt", "wt")

for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('Andrew', 'Angelina'))
#close input and output files
fin.close()
fout.close()

content = open("out.txt", "r").read()
# Upload new file we created with replaced name to GitHub
uploadNewFile = repo.create_file("out.txt", "Changed name in a file", content)
print (uploadNewFile)
'''