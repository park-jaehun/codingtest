def solution(array, commands):    
    answer = []
    
    for start, end, sorts in commands:
        start = (start  - 1)
        sorts = (sorts - 1)
        
        if start == (end-1) :
            answer.append(array[start])
        # start와 end가 같은 경우
        
        else:
            for idx, value in enumerate(sorted(array[start:end])):
                if idx == sorts:
                    answer.append(value)
        # start와 end가 다른 경우
        
    return answer