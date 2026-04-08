def solution(s):

    s2 = s.replace(" Z","*0")
    new_s = s2.split()
    
    answer = 0
    for c in new_s:
        if "*" in c:
            new_s.remove(c)
        else:
            answer += int(c)
    
    return answer  

#     TypeError: 'str' object cannot be interpreted as an integer
#     s2 = s.replace(" Z","*0")
#     new_s = s2.split()
    
#     answer = 0
#     for c in new_s:
#         if "*" in c:
#             new_s.pop(c)
#         else:
#             answer += int(c)
    
#     return answer   

#AttributeError: 'str' object has no attribute 'contrains'
#     s2 = s.replace(" Z","*0")
#     new_s = s2.split()
    
#     answer = 0
#     for c in new_s:
#         if c.contrains(Z):
#             new_s.pop(c)
#         else:
#             answer += int(c)
    
#     return answer 
    
# 엄청 획기적인 접근이라고 생각했는데
# ValueError: invalid literal for int() with base 10: '-3*0'
#     s2 = s.replace(" Z","*0")
#     new_s = s2.split()
    
#     answer = 0
#     for c in new_s:
#         answer += int(c)
    
#     return answer 
    
#     #Z의 index를 먼저 찾자!
#     Z_list = []
#     i = 0
#     new_s = s.split()
#     n = len(new_s)
    
#     while i < n:
#     #while i < n:
#         if new_s[i] == "Z":
#             Z_list.append(i)
#         i += 1
#         # i += 1 는 무조건 if 블록 밖에 있어야 함!! 무한순환 안되려면
            
# Z_list의 index and index-1을 제외하고 총합을 구함.
# remove 외에 인덱스 값으로 리스트 요소 삭제하는법 몰라서 검색해봄!
# 값으로 삭제 (remove): list.remove(value)는 지정한 첫 번째 값만 삭제.
# 인덱스로 삭제 (pop): list.pop(index)는 해당 위치의 요소를 삭제하고 반환.
# 위치로 삭제 (del): del list[index]는 특정 인덱스나 슬라이스 범위를 삭제.
# 전체 삭제 (clear): list.clear()는 리스트의 모든 요소를 지워 빈 리스트로 만
# for c in Z_list:
#     new_s.pop(c)
#IndexError: pop index out of range 오류 발생함
#     for c in Z_list:
#         x = c-1
#         new_s.pop(x)  
    
#     return new_s

# 이 코드에서 무한 순환이 되었는데 왜 무한 순환이 되는지 모르겠음.
# while i < n:
#     if s[i] == "Z":
#         Z_list.append(i)
#         i += 1

# 이 코드에서 왜 n값이 s의 길이만큼 제대로 안나오는지 모르겠음.. 아 리스트가 아니라 문자열이다!
#     Z_list = []
#     i = 0
#     n = len(s)
#     return n

# 아래 코드로 시도 했으나 결국에는 s.split() 이었음 다시 복습
# new_s = list(s)
# n = len(new_s)

# 이 코드에서도 알 수 없는 이유로 무한 순환이 되고 있음
# def solution(s):
#     #Z의 index를 먼저 찾자!
#     Z_list = []
#     i = 0
#     new_s = s.split()
#     n = len(new_s)
    
#     while i < n:
#     #while i < n:
#         if new_s[i] == "Z":
#             Z_list.append(i)
#             i += 1
#             if i == n:
#                 break 
#     return Z_list

# def solution(s):
#     #Z의 index를 먼저 찾자!
#     Z_list = []
#     i = 0
#     new_s = s.split()
#     n = len(new_s)
    
#     while i <= n:
#     #while i < n:
#         if new_s[i] == "Z":
#             Z_list.append(i)
#             i += 1
#         elif i == n:
#             break;          
#     return Z_list

# 추천 풀이
# def solution(s):
#     stack = []
#     for token in s.split():
#         if token == "Z":
#             stack.pop()       # 마지막 숫자 제거
#         else:
#             stack.append(int(token))  # 숫자 추가
#     return sum(stack)