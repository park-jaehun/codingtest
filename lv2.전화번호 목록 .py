def solution(phone_book):
    answer = True
    idx = 0
    phone_book = sorted(phone_book)
    while idx < len(phone_book):
        for i in range(1, len(phone_book) + 1):
            if (idx + i) < len(phone_book):
                if phone_book[idx] == (phone_book[idx + i])[0:(len(phone_book[idx]))]:
                    answer = False
                    return answer

                
        idx = idx + 1
        
    return answer
    # 효율성 문제...