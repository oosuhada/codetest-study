def solution(s):
    #Z의 index를 먼저 찾자!
    Z_list = []
    i = 0
    new_s = s.split()
    n = len(new_s)
    
    while i <= n:
    #while i < n:
        if new_s[i] == "Z":
            Z_list.append(i)
        i += 1
        # i += 1 는 무조건 if 블록 밖에 있어야 함!! 무한순환 안되려면
            
    return Z_list

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