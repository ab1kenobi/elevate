# backend/app.py (new file)
from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
from algorithm import risk

app = Flask(__name__)
CORS(app)

@app.route('/api/calculate-risk', methods=['POST'])
def calculate_risk():
    try:
        data = request.get_json()
        income = float(data.get('income', 0))
        savings = float(data.get('savings', 0))
        debt = float(data.get('debt', 0))
        
        risk_score = risk(income, savings, debt)
        
        return jsonify({
            'risk_score': risk_score
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")
        return jsonify(hist.to_dict('records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)