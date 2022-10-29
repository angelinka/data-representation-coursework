from cgitb import handler
import requests
import urllib.parse
from config import config as cfg

targetUrl= 'https://en.wikipedia.org'
# apiKey = 'TFA8FGlWwxlAuV2lRRFA8V0aNytm48phxRI9cbqw3bOOsVisSPpOrTDDtaz2PJqj'
apiKey = cfg['htmlToPdfKey']

apiUrl = 'https://api.html2pdf.app/v1/generate'

# ?url=https://example.com&apiKey={your-api-key}

params = {'url': targetUrl, 'apiKey': apiKey}
parcedParam = urllib.parse.urlencode(params)
completeUrl = apiUrl + '?' + parcedParam

response = requests.get(completeUrl)
print(response.status_code)

result = response.content
with open('Wiki.pdf', 'wb') as fp:
    fp.write(result)