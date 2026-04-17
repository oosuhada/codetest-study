def solution(order):
    order2 = order.join()
    order2.replace('3','a')
    
    answer = 0
    return order2