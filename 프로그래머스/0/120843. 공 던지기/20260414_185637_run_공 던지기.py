def solution(numbers, k):
    #배열 개수가 짝수일때랑 홀수일때 계산이 다를것 같음
    #배열을 두배로 만들면 같은 계산식으로 가능할 것 같음
    new_numbers = numbers*2 #가능할지
    #new_numbers = numbers + numbers
    
    #[1,2,3,1,2,3] 홀수번째 순서 = index 0,2,4
    #k = 2 => index = 2
    #k = 5 => index = 8
    #k = 3 => index = 4
    #index = (k-1)*2
    
    return new_numbers((k-1)*2)
    
    
