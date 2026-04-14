def solution(numbers, k):
    #배열 개수가 짝수일때랑 홀수일때 계산이 다를것 같음
    #배열을 두배로 만들면 같은 계산식으로 가능할 것 같음
    #new_numbers = numbers*2 #가능할지 return 해봄
    new_numbers = numbers + numbers
    
    #[1,2,3,1,2,3] 홀수번째 순서 = index 0,2,4
    # k = 2 => index = 2
    # k = 5 => index = 8
    # k = 3 => index = 4
    # index = (k-1)*2
    
    return new_numbers[(k-1)*2]
    #실패 (런타임 에러...)
    
    #배열 짝수, len(numbers) // 2 >= k 일때,
    #index = (k-1)*2
    
    #배열 짝수, len(numbers) // 2 < k 일때,
    #index = k % (len(numbers) // 2)
    
    #배열 홀수, len(numbers)+1 // 2 >= k 일때,
    #index = (k-1)*2

    #배열 홀수, len(numbers)+1 // 2 < k 일때,
    #홀수바퀴
    #짝수바퀴 
    
    #index = k % (len(numbers) // 2)
    
    # 1 2 3 4 5 6 7   ,4 -> 7 i=6
    # 1 2 3 4 5 6 7   ,5 -> 2 i=1 2바퀴
    # 1 2 3 4 5 6 7   ,10 -> 5 i=4 3바퀴
    # 1 2 3 4 5 6 7   ,13 -> 4 i=3 4바퀴
    # (7까지 2바퀴, 8부터 3바퀴)