from collections import defaultdict

s = "ababcbacadefegdehijhklij"

n = len(s)
rev_s = s[::-1]
lst = []
d = defaultdict(int)
for i in range(n):
    if d[rev_s[i]] == 0:
        d[rev_s[i]] = n-i-1
print(d)
for j in range(n):
    if d[s[j]] == j :
        a = s.index(s[j])
        for z in range(j+1):
            if s[:j+1][z] in s[j+1:]:
                break
        else:
            lst.append(len(s[:j])+1)
print(lst)
sumi = 0
for i in range(len(lst)):
    if i == 0:
        sumi += lst[i]
        pass
    else:
        lst[i] -= sumi
        sumi += lst[i]

print(lst)


