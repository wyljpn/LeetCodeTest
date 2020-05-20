import sys
import functools

line_num =0
count = 0
for line in sys.stdin:
    if line_num == 0:
        line_num += 1
        n = int(line)
        map_r = {}

    else:
        line_num += 1
        date, item, price, num = line.split()
        price, num = int(price), int(num)
        if (date, item) not in map_r:
            map_r[(date,item)] = price * num
            count += 1
        else:
            map_r[(date, item)] += price * num
    if line_num == n+1:
        break


def cmp(a,b):

    if a[1] != b[1]:
        return 1 if a[1] < b[1] else -1

    return 1 if a[0] > b[0] else -1


new_list = [(x,y) for x,y in map_r.items()]

new_list = sorted(new_list,key=functools.cmp_to_key(cmp))



for i in range(k):
    print("{} {}".format(new_list[i][0],new_list[i][1]))


'''
5 5
2019 ch 100 1
2019 flu 101 1
2019 bur 100 1
2019 chesescake 100 1
2019 ti 101 1
'''