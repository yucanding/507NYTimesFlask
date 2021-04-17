from flask import Flask, render_template
from secrets import key
import requests
app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    dic = {'api-key': key}
    response = requests.get(url, dic)
    result = response.json()['results'][:5]
    headlines = [r['title'] for r in result]
    return render_template('headlines.html', name=nm, stories=headlines)

if __name__ == '__main__':   
    app.run(debug=True)