from random import uniform
def update_stock_price(stock):
    stock[2]=stock[2]*(1+uniform(*stock[3]))