# Requests used to pull REST API results
import requests
from flask import Flask, request, render_template
from xml.etree import ElementTree


app = Flask(__name__, static_folder = 'static', template_folder = 'templates')

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/waitTime', methods=['POST'])
def my_form_post():
    text = request.form['airportCode']
    processed_text = text.upper()
    
    estimatedWaitIndex = getWaitTime(processed_text)
    currentLowerBound = calculateLowerBound(estimatedWaitIndex)
    currentUpperBound = calculateUpperBound(estimatedWaitIndex)

    green = False 
    yellow = False 
    red = False 

    if currentUpperBound <= 10: 
        green = True

    elif currentUpperBound > 10 and currentUpperBound <= 30: 
        yellow = True 

    else: 
        red = True 

    return render_template('waitTime.html', lowerBound = currentLowerBound, upperBound = currentUpperBound, green = green, yellow = yellow, red = red)
    

# Functions that will be used by the web application in order to display the appropiate wait time for the airport

def getWaitTime (airportCodeIn):

    api_url = "https://apps.tsa.dhs.gov/MyTSAWebService/GetConfirmedWaitTimes.ashx"

    api_parameters = {}
    api_parameters['ap'] = airportCodeIn 
    api_parameters['output'] = "XML"

    r = requests.get(url = api_url, params = api_parameters)
    tree = ElementTree.fromstring(r.content)

    token = tree.find("WaitTime")
    estimatedWait = token.find("WaitTimeIndex")

    return estimatedWait.text

def calculateLowerBound(estimatedWaitIndexIn): 

    if (estimatedWaitIndexIn == 0): 
        return int('0')

    else: 
        return int(estimatedWaitIndexIn) * int('10')

def calculateUpperBound(estimatedWaitIndexIn): 

    if (estimatedWaitIndexIn == 0): 
        return int('10')

    else: 
        return (int(estimatedWaitIndexIn) * int('10')) + int('10')


# Beginning of Main 
if __name__ == "__main__":
    app.run()
