import sys


# def main(n, k):
#     if (2 * k - 1) <= n:
#         return "YES"
#     else:
#         return "NO"


n, k = (int(i) for i in input().split())

result = ''
if (2 * k - 1) <= n:
    result = result.join('YES')
else:
    result = result.join('NO')
print(result)
