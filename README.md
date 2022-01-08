# 新春虎卷軸

## 如何使用
1. 只要創一個新的 json 檔案，並且符合以下格式
    ```json=1
    {
        "pre_sale_price": 0.044,
        "mint_price": 0.08,
        "lucky_prize": 44,
        "critical": 4,
        "prize_prob": 0.1,
        "eth_usdt": 3500,
        "threshold": [743, 1443, 2443, 3443, 4887],
        "total": 4888,
        "free_air_drop": 300
    }
    ```
2. 到 `main.py` 找到 `config_name = 'critical.json' # 改名字`，並且改成新的 json 檔名
3. `python3 main.py` (main 是第二版，第一版是 v1)

## 參數介紹
1. pre_sale_price 白單價格
2. mint_price 公售價格
3. lucky_prize 編號中獎獎金 
    (ex. 編號 44 倍數以及尾數是 444，額外贈送 44 U)
4. critical 爆擊率
5. prize_prob 中獎機率
6. eth_usdt: 兌換價格
7. threshold: 門檻設置，這邊要將門檻值減一 (假如捲軸編號是 1~4888，門檻是 744，那麼這邊要寫 743)
8. total: 總發行量
9. free_air_drop: 空投給虎友或其他的人的福利品
