def solution(s):
    count = 0
    ls = []
    while count <= len(s):
        tp_count = 1
        result = []
        answer = ""
        tmp_ls = []
        count += 1
        # 해당 문자열을 count로 리스트로 분리해서 저장
        for idx in range(0,len(s),count):
            if len(s)%count==0:
                result.append(s[idx:idx + count])
            else:
                if idx + count >= len(s):
                    answer = s[len(s)-(len(s)%count):]
                    result.append(answer)
                    break
                result.append(s[idx:idx + count])
        for i in range(0,len(result)):
            if i == 0:
                tmp_ls.append(result[i])
            elif result[i-1] == result[i]:
                tp_count += 1
                tmp_ls.pop()
                tmp = str(tp_count) + result[i]
                tmp_ls.append(tmp)
            else:
                tp_count = 1
                tmp_ls.append(result[i])
        ls.append(len("".join(tmp_ls)))
    return min(ls)


