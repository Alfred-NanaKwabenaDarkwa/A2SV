t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    lst = []
    l = 0
    m = ''
    temp = []


    for r in range(n):
        if a[r] > 0 :
            if m != '-':
                l = r
                temp.append(a[r])
            else:
                lst.append(max(temp) if temp else 0)
                temp = [a[r]]
            m = '+'

        elif a[r] < 0 :
            if m != '+':
                l = r
                temp.append(a[r])
            else:
                lst.append(max(temp) if temp else 0)
                temp = [a[r]]
            m = '-'

    if temp:
        lst.append((max(temp)))
    print(sum(lst))




