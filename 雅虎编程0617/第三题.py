import sys
import functools

maxn = 0

def dfs(step,now):
    if step> k:
        if now > maxn:
            maxn = now
        return
    for  i in range(n):
        if s[i] == 0:
            pass



line_num = 0
count = 0
a = list()
b = list()

for line in sys.stdin:
    if line_num == 0:
        n = int(line.spilt()[0])
        k = int(line.split()[1])

        pass

    else:
        line_num += 1
        a.append(line.split()[:-1])
        b.append(line.split()[-1])
        pass

    if line_num == n + 1:
        break
s = [0]*n

dfs(0)

