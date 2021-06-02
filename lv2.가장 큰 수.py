def solution(numbers):
    number = list(map(str, numbers))
    number.sort(key = lambda x:x*3, reverse = True)
    answer = str(int("".join(number)))

    return answer