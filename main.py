import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from matplotlib import font_manager
plt.rcParams['font.family'] = ['Heiti TC']
fig = plt.gcf()
fig.set_size_inches(18.5, 6.5)
fig.savefig('test2png.png', dpi=100)


cost = [0]*5
phase = [False]*5
profit = [0]*5
ETH = 3863
mint_price = [0.044, 0.08, 0.08, 0.08, 0.08] # eth
gift = [44*444, 1444*34, 2444*24+4*ETH, 3444*14+21.6*ETH, 4444*4+49.6*ETH+54496.90]


threshhold = [444, 1444, 2444, 3444, 4444]
lucky_prize = 44 # U

tmp_cost = []
tmp_profit = []

phase = 0
for i in range(1, 4445):
    if i <= threshhold[phase]:
        profit[phase] += mint_price[phase]*ETH
        if (len(str(i))>2 and str(i)[-3:] == "444") or (i%44==0):
            cost[phase] += lucky_prize
        if i == threshhold[phase]:
            cost[phase] += gift[phase]
            phase += 1
    tmp_cost.append(sum(cost))
    tmp_profit.append(sum(profit))

x = np.arange(1, 4445, 1)

pure = []
for i in range(4444):
    pure.append(tmp_profit[i] - tmp_cost[i])

plt.plot(x, pure, label="淨利 (獲利 - 成本)")
plt.xticks(np.arange(min(x), max(x)+1, 200.0))
plt.yticks(np.arange(min(pure), max(pure)+1, (max(pure)-min(pure))/20))


idx = 1
tmp_phase = 0
for x,y in zip(x, pure):
    if idx == threshhold[tmp_phase]-1:
        label = "{:.2f}".format(y)
        plt.annotate(label, # this is the text
                    (x,y), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(-3,3), # distance from text to points (x,y)
                    ha='left')

    if idx == threshhold[tmp_phase]:
        tmp_phase += 1
        label = "{:.2f}".format(y)
        plt.annotate(label, # this is the text
                    (x,y), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(3,-3), # distance from text to points (x,y)
                    ha='left')
    idx += 1

# plt.xlabel('Mint 捲軸數目', fontsize=20)
# plt.ylabel('虎群獲利', fontsize=20)
# plt.plot(x, tmp_cost)
# plt.plot(x, tmp_profit)
plt.legend()
plt.show()
