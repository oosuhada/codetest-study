def solution(a, b):
    new_a = 0
    new_b = 0
    for c in range(2,b):
        if a % c == 0 and b % c == 0:
            new_a = (a // c)
            new_b = (b // c)
    d = 2
    array = []
    while d < new_b:
        if new_b // d == 0:
            array.append(d)
    answer = 0
    return array.append


#최대 공약수 구하는 공식이 있을것 같다
