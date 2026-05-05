def solution(arr, queries):
    
    for s,e,k in queries:
        for i in range(arr):
            if s <= i <= k and i % k == 0:
                arr[i] += 1
    return arr