# 独立リスト
# 编程挑战说明：
# 10個の非負整数のリストが与えられます。リスト中の数値それぞれに次の除外条件を適用して新たなリストを作成してください。
#
# 0であれば除外する
# リストの左側に同じ数値が出てきたことがあれば除外する
# 出力する数値のリストは、もとの順序を保っている必要があります。
#
# 例えば入力が
#
# 3 1 100 200 300 0 201 200 100 10
# であれば、左から6番目の0、8番目の200、9番目の100を除外し
#
# 3 1 100 200 300 201 10
# を出力します。

import sys

nums = (int(i) for i in input().split())
nums = list(nums)

res = []
tmp = {}
for num in nums:
    if num == 0:
        continue
    if num in tmp:
        continue
    else:
        res.append(num)
        tmp[num] = 1
for i in res:
    print(i, end=' ')
