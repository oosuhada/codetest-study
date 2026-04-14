def solution(num_list, n):
    answer = []
    
    #n 슬라이싱으로 깔끔한 코드 구성이 가능하지 않을지
    #num_list[0], .. ,num_list[n-1]
    #num_list[n], .. ,num_list[2*n-1]
    #num_list[2n], .. ,num_list[3*n-1]
    #len(num_list) // 2 반복
    
    i = 1
    
    if n % 2 == 0:
        while i <= len(num_list) // n:
            answer += [num_list[(i-1)*n : i*n]]
            i += 1
        return answer
    else:
        while i <= len(num_list) // n:
            answer += [num_list[(i-1)*n : i*n]]
            i += 1
        return answer
    
#코드 실행하면서 테스트 결과는 맞췄는데, 정작 왜 n == 2 일때랑 더 클때랑 결과가 다른지,
#슬라이싱이 num_list[(i-1)*n : i*n-1]이 아니라 num_list[(i-1)*n : i*n]인지 정확히 이해하지 못함. 적다가 이해함 i*n는 포함되지 않기 때문일것