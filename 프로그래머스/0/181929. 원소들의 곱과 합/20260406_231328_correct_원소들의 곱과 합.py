def solution(num_list):
    
    # 🔴 [실수 1] 곱의 초기값을 0으로 하면 안됨
    # ❌ product_num = 0
    # 👉 0 * 어떤 수 = 0 → 계속 0이 됨
    # ✅ 곱은 1부터 시작해야 함
    
    product_num = 1  # ✅ 수정
    sum_num = 0
    
    # 🔴 [실수 2] for문 뒤에 콜론(:) 빠짐
    # 🔴 [실수 3] 리스트 순회는 OK (i는 각 원소)
    
    # 원소들의 곱
    for i in num_list:  # ✅ 콜론 추가
        product_num = product_num * i
    
    # 원소들의 합
    for i in num_list:  # ✅ 콜론 추가
        sum_num += i
    
    # 🔴 [실수 4] return 타입 문제 ("문자열" vs "정수")
    # ❌ return "1"
    # 👉 문제는 정수 1 또는 0을 요구함
    
    # 🔴 [실수 5] 조건 2개로 나눌 필요 없음 (else 사용 가능)
    
    if product_num < sum_num * sum_num:
        return 1   # ✅ 정수로 반환
    
    else:
        return 0   # ✅ 나머지는 전부 여기