

import sys

temperatures = (int(i) for i in input().split())
temperatures = list(temperatures)
highTemperatures = []
for i in range(0, 14):
    if (i+1) % 2 == 0:
        highTemperatures.append(temperatures[i])

for i in highTemperatures:
    print(i,end=' ')