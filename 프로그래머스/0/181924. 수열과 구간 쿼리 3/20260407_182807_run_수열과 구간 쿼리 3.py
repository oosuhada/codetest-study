def solution(arr, queries):
    
    #문제 이해
    #arr[i], 0=<i<len(arr)
    #queries[i,j]
    
    arr2 = arr
    
    for i,j in queries(i,j):
        arr[i] = arr2[j]
        arr[j] = arr2[i]
        #arr(i) <-> arr2(j) exchange 어떤 수식으로?
    
    return arr
