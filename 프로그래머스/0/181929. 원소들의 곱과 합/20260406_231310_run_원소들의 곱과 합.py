def solution(num_list):
    
    product_num = 1
    sum_num = 0
    
    #원소들의 곱
    for i in num_list:
        product_num = product_num * i
    
    #원소들의 합
    for i in num_list:
        sum_num += i
    
    if product_num < sum_num * sum_num:
        return 1
    
    if product_num > sum_num * sum_num:
        return 0
