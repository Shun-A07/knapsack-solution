import itertools #(ループにて総当たりを効率よく行えるライブラリ)
#(以下「items」の配列に品物18個のそれぞれの容量,価格を格納)
items=[
    (4,6),(8,12),(3,4),(5,3),(9,7),(2,1),(3,3),(1,2),(5,7),
    (2,3),(4,4),(2,2),(7,10),(10,13),(3,5),(13,16),(11,14),(8,9)
]
capacity=45 #(最大容量)
maxValue=0 #(最終的に最大の総価格を代入する変数(初期値0))
maxCombination=[] #(ライブラリで生成したパターン内で最適なものを格納する配列)

# (itertool.productでrange(2)(0〜1の意)をitemsの長さの数(今回は18)並べるものの全パターン(2^18通り)を順番に生成。それを配列patternsに格納する。)
patterns =list(itertools.product(range(2),repeat=len(items)))
for p in range(len(patterns)):
    totalWeight=0 #(それぞれのパターンでの総容量を代入する変数)
    totalValue=0 #(それぞれのパターンでの総価格を代入する変数)
    combination=[] #(それぞれのパターンでの品物の組み合わせを記録する配列)

    for i in range(len(items)):
        #(pで生成した全パターンの変更、iでパターンごとの18個の2進数を確認し、1なら加えるものとして容量と価格を増加(組み合わせを保存する配列にも追加))
        if patterns[p][i]==1:
            totalWeight +=items[i][0]
            totalValue +=items[i][1]
            combination.append(i+1)
    if totalWeight <=capacity and maxValue <totalValue: #(容量がオーバーしていない且つ総価格が現在保存している値より大きいなら更新)
        maxValue =totalValue
        maxCombination =combination

print("品物の組み合わせは",maxCombination)
print("最大の総価格は=", maxValue)