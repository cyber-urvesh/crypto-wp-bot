from flask import Flask, request
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'Hi' in incoming_msg:
        text = f'*Please enter one of the following option to get current rates in INR👇* \n *1*. Bitcoin *(BTC)* \n *2*. Litecoin *(LTC)* \n *3*. Ethereum *(ETH)* \n *4*. Tether *(USDT)* \n *5*. Cardiano *(ADA)* \n *6*. Steller *(XRP)* \n *7*. Dogecoin *(DOGE)* '
        msg.body(text)
        responded = True

    if '1' in incoming_msg or 'btc' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Bitcoin(BTC) Rate in INR*: Rs.{data["bitcoin"]["inr"]}'
        msg.body(rate)
        responded = True

    if '2' in incoming_msg or 'ltc' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Litecoin(LTC) Rate in INR*: Rs.{data["litecoin"]["inr"]}'
        msg.body(rate)
        responded = True

    if '3' in incoming_msg or 'eth' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Ethereum(ETH) Rate in INR*: Rs.{data["ethereum"]["inr"]}'
        msg.body(rate)
        responded = True

    if '4' in incoming_msg or 'usdt' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Tether&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Theter(USDT) Rate in INR*: Rs.{data["tether"]["inr"]}'
        msg.body(rate)
        responded = True

    if '5' in incoming_msg or 'ada' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Cardano&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Cardano(ADA) Rate in INR*: Rs.{data["cardano"]["inr"]}'
        msg.body(rate)
        responded = True
    
    if '6' in incoming_msg or 'xlm' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Stellar&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Stellar(XLM) Rate in INR*: Rs.{data["stellar"]["inr"]}'
        msg.body(rate)
        responded = True

    if '7' in incoming_msg or 'doge' in incoming_msg:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Dogecoin&vs_currencies=inr')
        data = response.json()
        rate = f'*Current Dogecoin(DOGE) Rate in INR*: Rs.{data["dogecoin"]["inr"]}'
        msg.body(rate)
        responded = True
    
    if not responded:
        text = f'*Please enter one of the following option to get current rates in INR👇* \n *1*. Bitcoin *(BTC)* \n *2*. Litecoin *(LTC)* \n *3*. Ethereum *(ETH)* \n *4*. Tether *(USDT)* \n *5*. Cardiano *(ADA)* \n *6*. Steller *(XRP)* \n *7*. Dogecoin *(DOGE)* '
        msg.body(text)
        responded = True

    return str(resp)


if __name__ == '__main__':
    app.run()