# 新春虎卷軸

## 如何使用
1. 只要創一個新的 json 檔案，並且符合以下格式
    ```json=1
    {
        "pre_sale_price": 0.044,
        "mint_price": 0.06,
        "lucky_prize": 44,
        "critical": 10,
        "prize_prob": 0.05,
        "eth_usdt": 3500
    }
    ```
2. 到 `main.py` 找到 `config_name = 'critical.json' # 改名字`，並且改成新的 json 檔名
3. `python3 main.py` (main 是第二版，第一版是 v1)

## 參數介紹
1. pre_sale_price 白單價格
2. mint_price 公售價格
3. lucky_prize 編號中獎獎金 
    (ex. 編號 44 倍數以及尾數是 444，額外贈送 44 U)
4. critical 白單價格
5. prize_prob 中獎機率
