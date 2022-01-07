import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math 
import json

config_name = 'critical.json' # 改名字
config = open(config_name)
config = json.load(config)

PHASE_COUNT = 5 # 5 階段
costs = []
profits = []

## 參數設定
ETH = config["eth_usdt"]

## 獲利參數
pre_sale_price = config["pre_sale_price"]
mint_price = config["mint_price"]
mint_price_phase = [pre_sale_price, mint_price, mint_price, mint_price, mint_price] # eth

## 成本參數
free_air_drop = 270 # 空投給虎友
lucky_prize = config["lucky_prize"] # U

cirtical = config["critical"]
prize_prob = config["prize_prob"]

threshhold = [643, 1443, 2443, 3443, 4443]
prize_prob_phase = [0.04, prize_prob, prize_prob, prize_prob, prize_prob, prize_prob]
prize = mint_price*cirtical*ETH # 獎金是 x 倍 mint 價格暴擊
phase_bonus = [0, 0, 0, 0, 59718] # 特斯拉


if free_air_drop >= threshhold[0]:
    print("空投 & 門檻的比例不對！")

phase = 0
tmp_profit = 0
bonus = 0 

def calc_lucky_prize(i):
    i += 1
    if (len(str(i))>2 and str(i)[-3:] == "444") or (i%44==0):
        return lucky_prize  
    else:
        return 0

for i in range(0, 4444):
    tmp_cost = 0
    if i < free_air_drop:
        tmp_profit = 0
    else:
        tmp_profit += mint_price_phase[phase]*ETH
        if i == threshhold[phase]:
            bonus += phase_bonus[phase] # 達到門檻，額外送多少獎金
            phase += 1
        prize_ctr = math.floor(prize_prob_phase[phase]*i) # 配合不同階段期望值，算出目前要送出多少包獎金
        tmp_cost = prize_ctr*prize
    tmp_cost += calc_lucky_prize(i)
    tmp_cost += bonus
    costs.append(tmp_cost)
    profits.append(tmp_profit)
    
x = np.arange(0, 4444, 1)

# 淨值計算
net_value = []
show_target_idx = False
profit_index = 0
result = {}

result["max_loss"] = {"id":-1, "value":0}
result["max_profit"] = {"id":-1, "value":0}

threshhold_net = []
net_ratio = []
for i in range(4444):
    tmp_net_value = (profits[i] - costs[i])/ETH
    if tmp_net_value < 0: # 找出最大虧損點
        profit_index = i+1
        if tmp_net_value < result["max_loss"]["value"]:
            result["max_loss"]["value"] = tmp_net_value
            result["max_loss"]["id"] = i
    else:# 找出最大獲利點
        if tmp_net_value > result["max_profit"]["value"]:
            result["max_profit"]["value"] = tmp_net_value
            result["max_profit"]["id"] = i
    net_value.append(tmp_net_value)

    if profits[i] == 0:
        net_ratio.append(0)
    else: # 計算 淨收入 / 收入
        ratio = (tmp_net_value*ETH) / profits[i]
        if ratio < -1:
            ratio = -1
        net_ratio.append(ratio)

    if i in threshhold:
        threshhold_net.append(tmp_net_value)

result["at_least"] = profit_index
result["sold_out"] = net_value[-1]

plt.rcParams['font.family'] = ['Heiti TC']
fig = plt.gcf()
fig.set_size_inches(18.5, 6.5)

plt.plot(x, net_value, label="淨利 (獲利 - 成本)")
plt.scatter(threshhold, threshhold_net, marker='o', color='r')
for i, txt in enumerate(threshhold_net):
    plt.annotate(txt, (threshhold[i]+28, threshhold_net[i]+10))

plt.xticks(np.arange(min(x), max(x)+1, 200.0))
plt.yticks(np.arange(min(net_value), max(net_value)+1, (max(net_value)-min(net_value))/20))

for p in range(PHASE_COUNT):
    plt.axvline(x=threshhold[p],color='k', linestyle='--')

idx = 1
tmp_phase = 0 # 0~5

print("第 {0} 包之前，都是虧錢".format(result["at_least"]))
print("{2:>5}: {0:>10} ETH / 在第 {1} 包".format(result["max_loss"]["value"], result["max_loss"]["id"]+1, "最大虧損"))
print("{2:>5}: {0:>10} ETH / 在第 {1} 包".format(result["max_profit"]["value"], result["max_profit"]["id"]+1, "最大收益"))
print("{2:>5}: {1:>10.2f} ETH".format(4444, result["sold_out"], "全部完售"))

fig1, ax1 = plt.subplots()
ax1.set_ylabel('虎群獲利百分比 (淨收入 / 收入)')
ax1.plot(x, net_ratio)

plt.xlabel('Mint 捲軸數目', fontsize=20)
plt.ylabel('虎群獲利', fontsize=20)
plt.title(config_name)
plt.legend()
plt.show()