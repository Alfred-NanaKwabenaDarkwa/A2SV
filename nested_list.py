if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst = [name,score]
        record.append(lst)
    score_lst = []
    for i in range(len(record)):
        score_lst.append(record[i][1])
    score_lst.sort()
    s_l_grade = score_lst[1]
    name =[]
    for i in range(len(record)):
        if record[i][1] == s_l_grade:
            name.append(record[i][0])
        name.sort()
    for i in name:
        print(i)
        