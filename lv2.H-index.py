def solution(citations):
    count = 1
    while(count):
        if count <= len([i for i in citations if count <= i]):
            count += 1
        else:
            return count-1