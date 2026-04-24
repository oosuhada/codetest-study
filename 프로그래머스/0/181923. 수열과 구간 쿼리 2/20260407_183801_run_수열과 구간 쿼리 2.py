def solution(arr, queries):
    
    answer = []
    for s, e, k in queries:
        for i in arr:
            if s <= i <= e:
                if arr[i] >= k:
                    return answer += min(arr[i])
                else:
                    return answer += "-1"
                    
    return answer