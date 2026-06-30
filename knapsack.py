# (ループにて総当たりを効率よく行えるライブラリ)
import itertools
# (以下「品物」の配列に18種それぞれの容量,価格を格納)
items=[
    (4,6),(8,12),(3,4),(5,3),(9,7),(2,1),(3,3),(1,2),(5,7),
    (2,3),(4,4),(2,2),(7,10),(10,13),(3,5),(13,16),(11,14),(8,9)
]
capacity=45
maxValue=0
maxCombination=[]
# (itertool.productでrange(2)(0〜1の意)をitemsの長さの数(今回は18)並べるものの全パターン(2^18通り)を順番に生成。それを配列patternsに格納する。)
patterns =list(itertools.product(range(2),repeat=len(items)))
for p in range(len(patterns)):
    totalWeight=0
    totalValue=0
    combination=[]
    for i in range(len(items)):
        #(pで生成した全パターンの変更、iでパターンごとの18つの2進数を確認。)
        if patterns[p][i]==1:
            totalWeight +=items[i][0]
            totalValue +=items[i][1]
            combination.append(i+1)
    if totalWeight <=capacity and maxValue <totalValue:
        maxValue =totalValue
        maxCombination =combination

print("品物の組み合わせは",maxCombination)
print("最大の総価格は=", maxValue)