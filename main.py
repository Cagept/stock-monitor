import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

URL = 'https://ryu.land/collections/sv10-destined-rivals'

# Function to check stock
def check_stock():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    stock_status = soup.find('div', {'class': 'product-status'})  # Change according to page structure
    return 'In Stock' if stock_status and 'Out of Stock' not in stock_status.text else 'Out of Stock'

@app.route('/')
def index():
    stock_status = check_stock()
    return render_template('index.html', stock_status=stock_status)

if __name__ == "__main__":
    app.run(debug=True)
