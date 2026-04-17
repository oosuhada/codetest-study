def solution(num, total):
    for n in range(-num,num):
        if sum(range(n,n+num)) == total:
            return n