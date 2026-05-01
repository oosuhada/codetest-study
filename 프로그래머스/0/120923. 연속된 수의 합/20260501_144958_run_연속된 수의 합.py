def solution(num, total):
    for n in range(-1000,1000):
        if sum(range(n,n+num)) == total:
            return n