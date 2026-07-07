import os
import json
import requests


API_KEY = os.environ["GEMINI_API_KEY"]

URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.0-flash:generateContent"
    f"?key={API_KEY}"
)


prompt = """
你是 AMRC Order Flow 市場分析師。

請分析以下市場：

1. XAUUSD 黃金
2. NASDAQ 指數
3. BTC

請嚴格輸出 JSON 格式，不要加入任何文字。

JSON格式：

{
 "date":"",
 "condition":"AI Generated",
 "markets":[
   {
    "name":"",
    "bias":"",
    "market_structure":"",
    "liquidity":"",
    "order_flow":"",
    "key_level":"",
    "trading_plan":"",
    "risk_management":""
   }
 ]
}


分析標準：

Market Structure:
- 趨勢方向
- HH/HL 或 LH/LL
- 結構轉換

Liquidity:
- Buy Side Liquidity
- Sell Side Liquidity
- Sweep位置

Order Flow:
- Delta
- CVD
- Absorption
- Initiative / Responsive

Trading Plan:
- Entry zone
- Confirmation
- Invalid level

請保持專業交易員語氣。

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

if "candidates" in result:
    text = result["candidates"][0]["content"]["parts"][0]["text"]
else:
    text = "AI Error: " + str(result)


data = {
    "error": str(result)
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
