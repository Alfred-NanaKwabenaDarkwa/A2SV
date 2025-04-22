t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    maxi = 1
    mini = 1
    for i in range(n):
        if a[i] > a[maxi-1]:
            maxi = i+1
        if a[i] < a[mini-1]:
            mini = i +1
    print(' '.join(map(str, (mini, maxi))))
