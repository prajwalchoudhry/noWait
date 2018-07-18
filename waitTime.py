
# Requests used to pull REST API results
import requests
from xml.etree import ElementTree


# TSA Waitimes API URL 
api_url = "https://apps.tsa.dhs.gov/MyTSAWebService/GetConfirmedWaitTimes.ashx"

api_parameters = {}
api_parameters['ap'] = "DEN" 
api_parameters['output'] = "XML"

r = requests.get(url = api_url, params = api_parameters)
tree = ElementTree.fromstring(r.content)

token = tree.find("WaitTime")
estimatedWait = token.find("WaitTimeIndex")

print(estimatedWait.text)