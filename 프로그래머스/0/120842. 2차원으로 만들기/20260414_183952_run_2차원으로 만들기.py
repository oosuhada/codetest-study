def solution(num_list, n):
    answer = []
    
    #n 슬라이싱으로 깔끔한 코드 구성이 가능하지 않을지
    #num_list[0], .. ,num_list[n-1]
    #num_list[n], .. ,num_list[2*n-1]
    #num_list[2n], .. ,num_list[3*n-1]
    #len(num_list) // 2 반복
    
    i = 1
    
    if n == 2:
        while i <= len(num_list) // 2:
            answer += [num_list[(i-1)*n : i*n]]
            i += 1
    elif:
        while i < len(num_list) // 2:
            answer += [num_list[(i-1)*n : i*n]]
            i += 1
    
    return answer