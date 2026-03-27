def solution(num_list):
    
    n = len(num_list)
    last = num_list[len(num_list)]
    secondLast = num_list[len(num_list)-1]
    
    if last > secondLast:
        return num_list += (last - secondLast)
    else:
        return num_list += (2*last)
    