# あなたは現在，ダイエット支援アプリを作ろうとしています。ユーザが，現在の体重 ww [kg] と現在の身長 hh [cm] と目標BMI bb を入力すると，最小何kg 体重を落とすことで目標BMI以下を達成できるかを表示させる機能を作りたいです。 BMIの計算式はBMI = 10000 * 体重 [kg] / 身長 [cm] / 身長 [cm]です。
#
# しかし現在，全ての入出力機能が非負整数にしか対応していません！そのため，例えば 0.30.3 kg 体重を落とせば目標BMIを達成できるとしても，必要量より少し多いですが非負整数である 11 kg の体重を落とすように表示しなければなりません。
#
# 実装の詳細
# CLI
# 体重・身長・目標BMIが与えられるので，最小何kgの体重を落とせば目標BMI以下になれるかを表示するプログラムを実装してください。
# 詳細は末尾の「CLI アプリ作成用テンプレート」を参照ください。
#
# 入力ルール
# 以下のフォーマットのデータが標準入力から与えられます。
#
# w h b
# 制約は以下です。
#
# 20 \le w \le 10020≤w≤100, 整数
# 100 \le h \le 200100≤h≤200, 整数
# 10 \le b \le 3010≤b≤30, 整数
# ダイエット後の体重が 00 kg 以下になるような入力は与えられません。
# 体重を落としても身長は変わらないものとしてください。
# 出力ルール
# 以下のフォーマットを満たす標準出力を出力してください。
#
# ans
# 1行目に，最小何kg 体重を落とせば目標BMIを達成できるかを非負整数で出力してください。
# 現在の身長・体重で，目標BMIを達成している場合は 00 を出力してください。
# 入出力例
# 例 1
# 標準入力
#
# 90 180 23
# 標準出力
#
# 16
# 体重 9090 kg，身長 180180 cm の人が，BMI 2323 を目指しています。この人の現在のBMIは，10000 \times 90 / 180 / 180 = 27.777 \cdots10000×90/180/180=27.777⋯ なので，体重を落とす必要があります。この人が 1616 kg の体重を落とすと体重は 7474 kg となり，BMIは 10000 \times 74 / 180 / 180 = 22.8395 \cdots10000×74/180/180=22.8395⋯ を達成するので，目標BMI以下になることができました。また，これが最小です。


# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# BMIの計算式より、身長とBMIを入力して、体重を出力する
def calculateWeight(height, BMI):
    return BMI * pow(height, 2) / 10000

def main(lines):
    for i, v in enumerate(lines):
        # 体重、身長と目標BMIを分けて
        weight, height, target_BMI = v.split(" ")
        weight = int(weight)
        height = int(height)
        target_BMI = int(target_BMI)
        # 目標体重を計算する
        target_weight = calculateWeight(height, target_BMI)
        # 現在の体重と目標の体重の差を計算する
        loss_weight = int(weight - target_weight)
        if loss_weight > 0:
            print(loss_weight)
        # 既に目標BMI以下です。したがって，この人はダイエットをする必要がありません。
        else:
            print(0)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
