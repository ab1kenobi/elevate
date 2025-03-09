import yfinance as yf
import numpy as np

def risk(income, savings, debt):
    score = (savings-debt)/income
    return score


income = 500000
savings = 1000000
debt = 50000

print(risk(income,savings,debt))