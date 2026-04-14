def solution(numbers, k):
    #배열 개수가 짝수일때랑 홀수일때 계산이 다를것 같음
    #배열을 두배로 만들면 같은 계산식으로 가능할 것 같음
    #new_numbers = numbers*2 #가능할지
    #print(new_numbers) #실행한 결괏값 null
    
    new_numbers = numbers + numbers
    print(new_numbers)