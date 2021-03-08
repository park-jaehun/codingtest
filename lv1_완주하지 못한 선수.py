from collections import Counter
def solution(participant, completion):
    answer = ''
    participant.extend(completion)
    al_ex = Counter(participant)
    for i,j in al_ex.items():
        if j % 2 != 0:
            answer = i
    return answer