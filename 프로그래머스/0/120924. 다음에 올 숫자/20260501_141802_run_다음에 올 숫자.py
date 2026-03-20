def solution(common):
    if (common[2] - common[1]) == (common[1] - common[0]):
        #등차수열임
        return common[-1] + (common[2] - common[1])
    elif (common[2] / common[1]) == (common[1] / common[0]):
        #등비수열임
        return common[-1] * (common[2] / common[1])

#등차수열인지 등비수열인지 파악하는 코드