from scipy.stats import binom

print("何連するか入力してください")
ren = int(input())

print("☆5は何人PUですか？")
pusuu = int(input())
if pusuu == 1:
    kakuritsu = 0.01
else:
    print("☆5で欲しい推しは何人ですか？")
    oshi = int(input())
    kakuritsu = 0.013 / pusuu * oshi

print("キーホルダーは使いますか？(y/n)")
key = input()
if key == "y":
    kakuritsu = kakuritsu * 2.5

print("欲しい枚数を入力してください")
maisuu = int(input())

print("ランダム確定チケット付きですか？(y/n)")
stepup = input()

# maisuu枚以上出したくてren連する場合で確率がkakuritsu%の場合の出ない確率をaに代入
a = binom.cdf(maisuu - 1, ren, kakuritsu)

if stepup == "y":
    a = a * binom.cdf(1 - 1, 1, oshi / pusuu)

# aを当らない確率から当たる確率に変換
a = 1 - a

print("{}％".format(round(a * 100, 2)))