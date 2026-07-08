import json
from datetime import datetime
import requests


symbols = {
    "黃金 XAUUSD": "GC=F",
    "NASDAQ": "^IXIC",
    "BTC": "BTC-USD",
    "DXY": "DX-Y.NYB",
    "VIX": "^VIX"
}


data = []

for name, symbol in symbols.items():

    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

    try:
        r = requests.get(url).json()

        price = r["chart"]["result"][0]["meta"]["regularMarketPrice"]

        data.append({
            "商品": name,
            "價格": price,
            "市場結構": "等待分析",
            "流動性": "等待分析",
            "訂單流程": "等待分析",
            "交易計畫": "等待分析"
        })

    except:

        data.append({
            "商品": name,
            "價格": "N/A",
            "市場結構": "資料錯誤",
            "流動性": "",
            "訂單流程": "",
            "交易計畫": ""
        })


market = {
    "日期": datetime.now().strftime("%Y-%m-%d"),
    "狀態": "每日市場更新",
    "市場": data
}


with open("market.json","w",encoding="utf-8") as f:
    json.dump(
        market,
        f,
        ensure_ascii=False,
        indent=2
    )


print("Market update complete")
