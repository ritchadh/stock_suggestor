# Define routes here
from flask import Flask, render_template, request, redirect
import requests
from iexfinance import Stock
import datetime
import stocks 
import json

with open('stocks.json') as f:
    data = json.loads(f)

app = Flask(__name__)

global s

class Stock:

    def __init__(self, amount,strategies):
        self.amount = amount
        self.strategies = strategies

    def inputStrategies(self, strategies):
        self.strategies = strategies    

@app.route('/', methods = ['GET'])
def display_strategies():
    strategies = ['Ethical Investing','Growth Investing','Index Investing','Quality Investing','Value Investing']
    return render_template('index.html', strategies = strategies)

@app.route('/stocks', methods = ['POST'])
def display_stocks():
    stocks = []
    userAmount = request.form['Amount']
    strategiesPicked = request.form.getlist("strategies")
    s =  Stock(userAmount,strategiesPicked)

    for s in strategiesPicked:s
        stocks.append(data[s])

    return render_template('displayStock.html', stocks = stocks)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)