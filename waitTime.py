# Requests used to pull REST API results
import requests
from flask import Flask, request, render_template
from xml.etree import ElementTree


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['airportCode']
    processed_text = text.upper()
    print(processed_text); 
    return processed_text

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
        return int('10'); 

    else: 
        return int(currentWaitIndex) * int('10'); 


# Beginning of Main 

my_form()
my_form_post()
