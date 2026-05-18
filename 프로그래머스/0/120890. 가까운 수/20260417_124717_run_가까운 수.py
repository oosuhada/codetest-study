def solution(array, n):
    
    new_array = array
    new_array.append(n)
    new_array.sort()
    # new_array.append(200)
    # IndexError: list index out of range 문제 해결하기 위해
    # 가장 클 200를 더했는데, 과연 이게 최선의 대응책일지 의문
    # 역시나 테스트17, 18은 틀렸음
    
    x = len(new_array)
    
    if new_array[0] == n:
        return new_array[1]
    elif new_array[x-1] == n:
        return new_array[x-2]
    
    for i in range(1,x):
        if new_array[i] == n:
            if (n - new_array[i-1]) > (new_array[i+1]-n):
                return new_array[i+1]
            elif (n - new_array[i-1]) <= (new_array[i+1]-n):
                return new_array[i-1]

# IndexError: list index out of range
# new_array = array
# new_array.append(n)
# new_array.sort()

# for i in range(0,len(new_array)):
#     if new_array[i] == n:
#         if (n - new_array[i-1]) > (new_array[i+1]-n):
#             return new_array[i+1]
#         elif (n - new_array[i-1]) <= (new_array[i+1]-n):
#             return new_array[i-1]

# null값 오류
#    new_array = array
#     new_array.append(n)
#     new_array.sort()
#     new_array.append(200)
#     new_array2 = [-100]
#     new_array2.append(new_array)
#     # IndexError: list index out of range 문제 해결하기 위해
#     # 가장 클 200를 더했는데, 과연 이게 최선의 대응책일지 의문
#     # 역시나 테스트17, 18은 틀렸음
                     
#     for i in range(0,len(new_array2)):
#         if new_array2[i] == n:
#             if (n - new_array2[i-1]) > (new_array2[i+1]-n):
#                 return new_array2[i+1]
#             elif (n - new_array2[i-1]) <= (new_array2[i+1]-n):
#                 return new_array2[i-1]