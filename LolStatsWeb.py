# Imports

from flask import Flask, render_template
import requests
import json
from main import main


# LolStats

run = main(str(raw_input('Enter API Key: ')), "StirlingArcher69", 1960675310)
_events = run.getEventsPerPerson()

# Flask
app = Flask(__name__)

@app.route('/')
def home():
    headers = {'Content-Type': 'application/json'}
    url = 'http://httpbin.org/post'
    r = requests.post(url, data=json.dumps(_events), headers=headers)
    return json.dumps(r.json(), indent=4)
    #return render_template('home.html')

if __name__ == '__main__':
    app.run()
