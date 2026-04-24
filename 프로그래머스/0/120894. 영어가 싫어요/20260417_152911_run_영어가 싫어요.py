def solution(numbers):
    
    numbers0 = numbers.replace("zero","0")
    numbers1 = numbers0.replace("one","1")
    numbers2 = numbers1.replace("two","2")
    numbers3 = numbers2.replace("three","3")
    numbers4 = numbers3.replace("four","4")
    numbers5 = numbers4.replace("five","5")
    numbers6 = numbers5.replace("six","6")
    numbers7 = numbers6.replace("seven","7")
    numbers8 = numbers7.replace("eight","8")
    numbers9 = numbers8.replace("nine","9")
    
    return int(numbers9)