def solution(s):
    result = 0
    for order in s:
        if result < 0:
            return False
        if order == "(":
            result += 1
        else:
            result -= 1
    if result == 0:
        return True
    else:
        return False

