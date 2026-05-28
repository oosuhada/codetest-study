def solution(arr):
    stk = []
    i = 0
    
    while len(i) > len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.append(-1)
    
    return stk