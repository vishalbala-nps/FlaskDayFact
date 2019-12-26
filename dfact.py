from flask import Flask, render_template, request
import requests

#Global Vars
API_URL = "http://numbersapi.com/"

#Internal Functions
def get_fact(tdate):
    month = tdate.split('-')[1]
    date = tdate.split('-')[2]
    CURL = API_URL+month+"/"+date+"/date"
    response = requests.get(CURL)
    if response.status_code != 200:
        return "error"
    else:   
        return response.text

#Main Program starts here

app = Flask(__name__)


#Default Route
@app.route('/') 
def main():
    return render_template('index.html')

#Displays Fact
@app.route('/get_fact')
def pod():
    tdate = request.args.get('date')
    fact = get_fact(tdate)
    if fact != "error":
        return render_template('details.html', tdate=tdate, fact=fact)
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
