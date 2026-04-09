def solution(array):
    m = len(array.sorted())//2
    answer = array.sorted()[m]
    return answer

#sort() vs sorted() 차이