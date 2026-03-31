def solution(num_list):
    
    n = len(num_list)
    last = num_list[len(num_list)-1]
    secondLast = num_list[len(num_list)-2]
    
    if last > secondLast:
        return num_list[:n] + "last - secondLast"
    else:
        return num_list[:n] + "2*last"
    