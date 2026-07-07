import os
import json
import requests


API_KEY = os.environ["GEMINI_API_KEY"]

URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-1.5-flash:generateContent"
    f"?key={API_KEY}"
)


prompt = """
你是 AMRC Order Flow 市場分析師。

請每日分析：

1. XAUUSD 黃金
2. NASDAQ
3. BTC

使用以下架構：

Market Structure:
分析市場結構

Liquidity:
分析流動性位置

Order Flow:
分析 Delta、CVD、吸收、主動買賣

Trading Plan:
提供交易規劃

輸出 JSON 格式。
"""


response = requests.post(
    URL,
    headers={
        "Content-Type": "application/json"
    },
    json={
        "contents":[
            {
                "parts":[
                    {
                        "text":prompt
                    }
                ]
            }
        ]
    }
)


result = response.json()


print(result)

if "candidates" not in result:
    raise Exception(result)

text = result["candidates"][0]["content"]["parts"][0]["text"]


data = {
    "date":"AUTO UPDATE",
    "condition":"AI Generated",
    "analysis":text
}


with open(
    "market.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=4
    )


print("AMRC AI UPDATE COMPLETE")
