
# Requests used to pull REST API results
import requests
from xml.etree import ElementTree

# Functions that will be used by the web application in order to display the appropiate wait time for the airport

def getWaitTime ():

    api_url = "https://apps.tsa.dhs.gov/MyTSAWebService/GetConfirmedWaitTimes.ashx"

    api_parameters = {}
    api_parameters['ap'] = "DEN" 
    api_parameters['output'] = "XML"

    r = requests.get(url = api_url, params = api_parameters)
    tree = ElementTree.fromstring(r.content)

    token = tree.find("WaitTime")
    estimatedWait = token.find("WaitTimeIndex")

    return estimatedWait.text

def calculateWaitTime():

    currentWaitIndex = getWaitTime()
    
    if currentWaitIndex == 0: 
        return 10; 

    else: 
        return int(currentWaitIndex) * int('10'); 






time = calculateWaitTime()
print(time); 