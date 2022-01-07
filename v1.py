import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

PHASE_COUNT = 5 # 5 階段
cost = [0]*PHASE_COUNT
profit = [0]*PHASE_COUNT
tmp_cost = []
tmp_profit = []

## 參數設定
ETH = 3863
target_profit = 200*ETH

## 成本參數
gas_fee = 40
phase_gas_fee = [0, 0, 4*gas_fee, 8*gas_fee, 8*gas_fee] # 前兩個階段沒有送 eth，後三個階段才有
lucky_prize = 44 # U
free_air_drop = 270 # 空投給虎友
gift = [44*444, 34*1444, 24*2444+4*ETH, 14*3444+21.6*ETH, 4*4444+49.6*ETH+54496.90]
threshhold = [444, 1444, 2444, 3444, 4444]

## 獲利參數
mint_price = [0.044, 0.08, 0.08, 0.08, 0.08] # eth

if free_air_drop >= threshhold[0]:
    print("空投 & 門檻的比例不對！")

phase = 0
gift_phase = -1
for i in range(1, 4445):
    if i <= threshhold[phase] and i > free_air_drop:
        profit[phase] += mint_price[phase]*ETH
        if (len(str(i))>2 and str(i)[-3:] == "444") or (i%44==0):
            cost[phase] += lucky_prize
        if i == threshhold[phase]:
            cost[phase] += gift[phase]
            cost[phase] += phase_gas_fee[phase]
            phase += 1
    
    tmp_cost.append(sum(cost))
    tmp_profit.append(sum(profit))

x = np.arange(1, 4445, 1)

# 淨值計算
net_value = []
show_target_idx = False
for i in range(4444):
    tmp_net = tmp_profit[i] - tmp_cost[i]
    if not show_target_idx and tmp_net >= target_profit:
        print("賣 {0} 包，即可達到目標獲利 : {1} U".format(i+1, target_profit))
        show_target_idx = True
    net_value.append(tmp_net)


plt.rcParams['font.family'] = ['Heiti TC']
fig = plt.gcf()
fig.set_size_inches(18.5, 6.5)

plt.plot(x, net_value, label="淨利 (獲利 - 成本)")
plt.xticks(np.arange(min(x), max(x)+1, 200.0))
plt.yticks(np.arange(min(net_value), max(net_value)+1, (max(net_value)-min(net_value))/20))

idx = 1
tmp_phase = 0 # 0~5
for x,y in zip(x, net_value):
    ## 印出門檻值之前一個點 (ex: 443, 1443 ...)
    if idx == threshhold[tmp_phase]-1:
        label = "{:.2f}".format(y)
        plt.annotate(label, 
                    (x,y), 
                    textcoords="offset points", 
                    xytext=(-3,3),
                    ha='left')
    ## 印出門檻值 (ex: 444, 1444 ...)
    if idx == threshhold[tmp_phase]:
        tmp_phase += 1
        label = "{:.2f}".format(y)
        plt.annotate(label, 
                    (x,y), 
                    textcoords="offset points", 
                    xytext=(3,-3), 
                    ha='left')
    idx += 1

plt.xlabel('Mint 捲軸數目', fontsize=20)
plt.ylabel('虎群獲利', fontsize=20)
plt.savefig("v1.png")
plt.legend()
plt.show()
