def solution(my_string):
    #직전에 모음만 replace하는 방식을 다뤄서인지 replace밖에 생각이 나지 않는데
    #dictionary 방식이라던지 더 효율적인 방식이 있을것 같음 일단 노가다
    
    new_string = my_string
    new_string = new_string.replace("a",'')
    new_string = new_string.replace("b",'')
    new_string = new_string.replace("c",'')
    new_string = new_string.replace("d",'')
    new_string = new_string.replace("e",'')
    new_string = new_string.replace("f",'')
    new_string = new_string.replace("g",'')
    new_string = new_string.replace("h",'')
    new_string = new_string.replace("i",'')
    new_string = new_string.replace("j",'')
    new_string = new_string.replace("k",'')
    new_string = new_string.replace("l",'')
    new_string = new_string.replace("m",'')
    new_string = new_string.replace("n",'')
    new_string = new_string.replace("o",'')
    new_string = new_string.replace("p",'')
    new_string = new_string.replace("q",'')
    new_string = new_string.replace("r",'')
    new_string = new_string.replace("s",'')
    new_string = new_string.replace("t",'')
    new_string = new_string.replace("u",'')
    new_string = new_string.replace("v",'')
    new_string = new_string.replace("w",'')
    new_string = new_string.replace("x",'')
    new_string = new_string.replace("y",'')
    new_string = new_string.replace("z",'')
    new_list = list(new_string)
    new_list.sort()

    new_list2 = []
    for c in new_list:
        a = int(c)
        new_list2.append(a)
        
    return new_list2

#여기까지 잘 풀었는데 리스트 안에 값이 string 으로 반환됨. 
#int로 반환하는 방법 생각해본 적이 없는것 같음