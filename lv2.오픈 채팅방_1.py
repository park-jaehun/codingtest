# -*- coding: euc-kr -*-
# -*- coding: utf-8 -*-
import time
start = time.time()
def solution(record):
    start = time.time()
    # Enter 문이 들어왔을 때
    id_name_dic = {}
    id_ls = []
    act_ls = []
    ans_ls = []
    def Enter(e_value):
        return [e_value.split(" ")[0], e_value.split(" ")[1], e_value.split(" ")[2]]

    def Leave(e_value):
        return [e_value.split(" ")[0], e_value.split(" ")[1]]

    def Change(e_value):
        return [e_value.split(" ")[1], e_value.split(" ")[2]]

    for i in record:
        if i.split(" ")[0] == "Enter":
            if Enter(i)[1] not in id_name_dic:
                id_name_dic[Enter(i)[1]] = Enter(i)[2]
                id_ls.append(Enter(i)[1])
                act_ls.append("Enter")

        elif i.split(" ")[0] == "Leave" and id_name_dic[i.split(" ")[1]]:
            id_ls.append(i.split(" ")[1])
            act_ls.append("Leave")
            del id_name_dic[i.split(" ")[1]]

        else:
            id_name_dic[Change(i)[0]] = Change(i)[1]

    for uid, act in zip(id_ls, act_ls):
        ans_ls.append(id_name_dic[uid] + "님이" + " " + act)

    return ans_ls

sol = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
print(time.time() - start)
print(sol)