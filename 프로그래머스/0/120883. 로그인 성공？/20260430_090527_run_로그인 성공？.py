def solution(id_pw, db):
    answer = "fail"
    id_try, pw_try = id_pw
    for array in db:
        a,b = array
        if id_try == a:
            answer = "wrong pw"
            if pw_try == b:
                answer = "login"
    return answer