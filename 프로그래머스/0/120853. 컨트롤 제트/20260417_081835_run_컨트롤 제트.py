def solution(s):
    #Z의 index를 먼저 찾자!
    Z_list = []
    i = 0
    new_s = s.list('')
    n = len(new_s)
    
    return n


    #for i in s[i]:
    while i < n:
        if s[i] == "Z":
            Z_list.append(i)
            i += 1
    
            
    answer = 0
    

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