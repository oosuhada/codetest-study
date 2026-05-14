def solution(array, n):
    
    new_array = array
    new_array.append(n)
    new_array.sort()
    new_array.append(101)
                     
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