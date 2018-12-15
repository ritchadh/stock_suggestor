from flask import Flask, render_template, request, redirect
import requests
from iexfinance import Stock
import datetime
app = Flask(__name__)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)