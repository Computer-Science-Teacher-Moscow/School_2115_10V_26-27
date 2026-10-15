with open('24_31204.txt') as file:
    s = file.readline()
d = {}
with open('31204.csv') as file:
    for s1 in file:
        i, rim = s1.split()
        d.setdefault(rim, i)
res = []
for x in d:
    if x in s:
        res.append(x)
# print(res)
m = max(res, key=lambda x: (len(x), d[x]))
print(m)
m1 = [x for x in res if len(x) == 14]
for f in m1:
    print(f, d[f])

print(s.index(m) + 14 - 1)
