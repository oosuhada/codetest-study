def solution(price):

    if price >= 10 and price < 100,000:
        return int(price)
    elif price >= 100,000 and price < 300,000:
        return int(price*0.95)
    elif price >= 300,000 and price < 500,000:
        return int(price*0.9)
    elif price >=500,000:
        return int(price*0.8)