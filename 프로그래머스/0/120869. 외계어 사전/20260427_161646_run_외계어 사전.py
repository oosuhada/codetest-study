from itertools import combinations

def solution(spell, dic):
    new_array = list(combinations(spell,3))
    answer = 0
    return new_array


# ab ba (2!)
# abc acb bac bca cab cba (3!)

# spell 요소들로 가능한 모든 콤비네이션을 만들고 싶은데 어떤 방법이 있을지

# 순열: 순서가 다르면 다른 경우로 취급 ex) ('사과','배') ≠ ('배','사과')
#result1 = list(permutations(['사과', '배', '바나나'], 2))

# 조합: 순서가 달라도 같은 경우로 취급 ex) ('사과','배') == ('배','사과')
#result2 = list(combinations(['사과', '배', '바나나'], 2))

# 중복조합: 조합에서 같은 값을 여러 번 뽑는 것도 허용 ex) ('사과','사과') 가능
#result3 = list(combinations_with_replacement(['사과', '배', '바나나'], 2))

# 곱집합: 여러 리스트에서 각각 하나씩 뽑는 모든 조합 ex) 빵 + 음료수 페어링
#result4 = list(product(['식빵', 'bagel'], ['우유', '주스']))

# 자주 쓰는 파이썬 표준 라이브러리들
# pythonfrom itertools import permutations, combinations, product # 순열, 조합
# from collections import Counter, defaultdict # 개수 세기, 기본값 딕셔너리
# import math # math.gcd(), math.sqrt() 등   