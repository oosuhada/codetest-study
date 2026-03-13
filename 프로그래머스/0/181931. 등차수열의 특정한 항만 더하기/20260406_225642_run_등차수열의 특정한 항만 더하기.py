def solution(a, d, included):
    
    # 🔴 included 길이 = n (사용해도 되고 안 써도 됨)
    n = len(included)
    
    # 등차수열:
    # a, a+d, a+2d, ..., a+(n-1)*d
    # 👉 i번째 항 = a + i*d  (i는 0부터 시작)
    
    answer = 0
    
    # 🔴 [실수 1] for문 뒤에 콜론(:) 빠짐
    for i in range(len(included)):  # ✅ 콜론 추가
        
        # 🔴 [실수 2] 리스트 접근은 ()가 아니라 [] 사용
        # ❌ included(i)
        # 👉 함수 호출처럼 보임 → 에러
        
        # 🔴 [실수 3] True 비교는 생략 가능 (Python 스타일)
        # ❌ included[i] == True
        # 👉 included[i] 자체가 True/False
        
        if included[i]:  # ✅ 이렇게 쓰는게 정석
            
            # 🔴 [개념 체크] i번째 항 계산
            # a + (i * d)
            # i=0 → a
            # i=1 → a+d
            # i=2 → a+2d
            
            answer += (a + (i * d))
    
    return answer