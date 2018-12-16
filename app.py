# Define routes here
from flask import Flask, render_template, request, redirect
import requests
from iexfinance import Stock
import datetime
import json

with open('stocks.json') as f:
    data = json.load(f)

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
    print(userAmount)
    strategiesPicked = request.form.getlist("strategies")
    print(strategiesPicked)
    s =  Stock(userAmount,strategiesPicked)

    for s in strategiesPicked:
        stocks.append(data[s])

    stocks_list = [item for sublist in stocks for item in sublist]
    print(stocks_list)
    
    # Find the change percent for all the stocks 
    stock_dict = {}

    for stock in stocks_list:
        ticker_symbol = data[stock]
        now = datetime.datetime.now()
        current_datetime = str(now.month)+" "+str(now.day)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" "+str(now.year)
        stock_info = requests.get('https://api.iextrading.com/1.0/stock/'+ticker_symbol+'/quote')

        if stock_info.status_code == 200:
            json_data = stock_info.json()
            changePercent = json_data['changePercent']
            stock_dict[stock] = changePercent
        
        else:
            print("Error: API not reachable!!")

    print(stock_dict)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)