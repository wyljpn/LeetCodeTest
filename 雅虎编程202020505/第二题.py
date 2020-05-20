# ベストセラー2
# 编程挑战说明：
# 一週間にN個の購買履歴データがあります。
# それぞれの購買履歴データは購入日、商品名、単価、個数からなり、購入日が古いものから順番に並んでいます。
# 1日ごとに合計の購入個数が一番おおい商品を、日付と個数とともに表示してください。
# 結果は日付の昇順で表示してください。
# ただし1日の購入個数が等しい商品が複数ある場合は、そのすべての商品を商品名の昇順で表示してください。
# ある1日に1個も商品が売れなかった場合は、その日の結果を表示する必要はありません。
#
# 输入：
# 標準入力の一行目に購買履歴の個数Nが与えられます。
# 続くN行は販売履歴データです。
# 入力データの各行の行末には改行があります。
# 販売履歴のそれぞれの行はそれぞれ1つの販売履歴を表し、空白区切りで左から購入日、商品名、単価、個数です。
# 入力は次の制約を満たします。
#
# Nは1以上300以下の整数
# 販売履歴は購入日が古いものから並んでいる
# 購入日はYYYY-MM-DDの形式の10文字の文字列で、YYYYは年を表す1000から3000の4桁の数字、MMは月を表す01から12の2桁の数字、DDは日にちを表す01から31の2桁の数字（後述の入力例も参照のこと）
# 商品名はアルファベット小文字で構成された1文字以上20文字以下の文字列
# 単価は1以上10000以下の整数
# 個数は1以上1000以下の整数
# 输出：
# 各行は空白区切りで左から、日付、商品名、合計販売個数である必要があります。
# 1日に売り上げた個数が等しい商品が複数ある場合でも、日付を省略したりせず、日付、商品名、合計販売個数をそれぞれ出力する必要があります。
# 問題説明にある行の出力順序を守ってください。
#
# たとえば入力が
#
# 5
# 2030-01-14 cherrypie 1150 5
# 2030-01-14 cherrypie 1150 6
# 2030-01-15 cherrypie 1150 3
# 2030-01-15 tiramisu 980 2
# 2030-01-15 burntcream 1980 3
# のとき、期待される出力は
#
# 2030-01-14 cherrypie 11
# 2030-01-15 burntcream 3
# 2030-01-15 cherrypie 3
# になります
#
# 出力は概ね10秒以内に得られるようにしてください。処理時間が長すぎる場合は得点が得られません。


import sys
import functools

line_num =0
count = 0

def cmp(a,b):

    if a[1] != b[1]:
        return 1 if a[1] < b[1] else -1

    return 1 if a[0] > b[0] else -1

for line in sys.stdin:
    if line_num == 0:
        line_num += 1
        n = int(line)
        map_r = {}
        pre_date = ""
        local_max = 0
    else:

        line_num += 1
        date, item, price, num = line.split()
        if pre_date != date:
            new_list = [(x, y) for x, y in map_r.items()]

            new_list = sorted(new_list, key=functools.cmp_to_key(cmp))

            for tmp in new_list:
                if tmp[1] == local_max:
                    print("{} {} {}".format(tmp[0][0], tmp[0][1], tmp[1]))
                else:
                    break

            map_r = {}
            local_max = 0

        pre_date = date

        price, num = int(price), int(num)
        if (date, item) not in map_r:
            map_r[(date, item)] = num
            count += 1
        else:
            map_r[(date, item)] += num
        local_max = max(map_r[(date, item)], local_max)

    if line_num == n+1:
        break

new_list = [(x, y) for x, y in map_r.items()]

new_list = sorted(new_list, key=functools.cmp_to_key(cmp))

for tmp in new_list:
    if tmp[1] == local_max:
        print("{} {} {}".format(tmp[0][0], tmp[0][1], tmp[1]))
    else:
        break
