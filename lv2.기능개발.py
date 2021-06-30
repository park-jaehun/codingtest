import math
def solution(progresses, speeds):
    tmp = []
    answer = []
    count,value = 0,100
    for i,speed in zip(progresses, speeds):
        tmp.append(math.ceil((100-i)/speed))
    for idx in range(len(tmp)):
        if idx == 0:
            value = tmp[idx]
            count += 1
        elif tmp[idx] <= value:
            count += 1
        else:
            answer.append(count)
            count = 1
            value = tmp[idx]
    answer.append(count)
    return answer