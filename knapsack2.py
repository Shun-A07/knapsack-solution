#(以下「items」の配列に品物18個のそれぞれの容量,価格を格納)
items =[
    (4,6),(8,12),(3,4),(5,3),(9,7),(2,1),(3,3),(1,2),(5,7),
    (2,3),(4,4),(2,2),(7,10),(10,13),(3,5),(13,16),(11,14),(8,9)
]
capacity =45 #(最大容量)
perWeightList=[] #(単位重さあたりの価格を入れる配列)

#(それぞれの品物の単位重さあたりの価格を求め、perWeightListに代入。itemsの何番目の要素に対応するか記録するためにiの情報も代入。)
for i in range(len(items)):
    perWeight = items[i][1]/items[i][0]
    perWeightList.append([i,perWeight])

#(sort関数で並び替える(key=lambda x : x[1]...配列の1(2番目)を基準とする。(lambdaは無名関数の意)　reverse=True...大きい順(降順)に並べる))
perWeight.sort(key=lambda x: x[1], reverse=True)

totalWeight =0 #(現在の総容量)
totalValue =0 #(総価格を代入する変数)
combination =[] #(品物の組み合わせを格納する配列)


for p in perWeightList:
#(perWeightに対応したitems内の重さ・価格を取り出す)
    number =p[0]
    weight =items[number][0]
    value =items[number][1]

#(総容量をオーバーしないか確認しながら、単位重さあたりの価格順に加える)
    if totalWeight + weight <= capacity:
        totalWeight += weight
        totalValue += value
        combination.append(number + 1)

print("品物の組み合わせは", combination)
print("最大の総価格は=", totalValue)