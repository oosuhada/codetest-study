def solution(order):
    order2 = str(order)
    order3 = order2.replace('3','a')
    order3 = order3.replace('6','a')
    order3 = order3.replace('9','a')
    answer = order3.count('a')

    return answer