def solution(price):
    
    if price >= 10 and price < 100000:
        return int(price)
    elif price >= 100000 and price < 300000:
        return int(price*0.95)
    elif price >= 300000 and price < 500000:
        return int(price*0.9)
    elif price >=500000:
        return int(price*0.8)