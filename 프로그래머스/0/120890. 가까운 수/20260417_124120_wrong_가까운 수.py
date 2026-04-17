def solution(array, n):
    
    new_array = array
    new_array.append(n)
    new_array.sort()
    new_array.append(200)
    # IndexError: list index out of range 문제 해결하기 위해
    # 가장 클 101를 더했는데, 과연 이게 최선의 대응책일지 의문
                     
    for i in range(0,len(new_array)):
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