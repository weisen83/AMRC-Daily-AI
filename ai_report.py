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
你是 AMRC Order Flow 專業交易分析師。

請分析以下市場：
1. XAUUSD 黃金
2. NASDAQ 指數
3. BTC

分析需符合 Auction Market Theory 與 Order Flow 邏輯。

請輸出 JSON 格式，不要加入任何額外文字。

JSON格式：

{
 "date":"",
 "condition":"AI Generated",
 "markets":[
  {
   "name":"",
   "market_structure":"",
   "liquidity":"",
   "order_flow":"",
   "trading_plan":""
  }
 ]
}


分析要求：

Market Structure:
- 判斷 HTF Bias
- 趨勢或盤整
- HH/HL 或 LH/LL 結構
- 重要支撐阻力區


Liquidity:
- Buy Side Liquidity
- Sell Side Liquidity
- 流動性掃取區域
- Stop Hunt 可能位置


Order Flow:
- Delta方向
- CVD變化
- Absorption吸收
- Initiative / Responsive Flow
- 買賣力量失衡


Trading Plan:
- 多空兩種情境
- Entry Zone
- Confirmation
- Invalid Level
- Target


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
text = text.replace("```json", "")
text = text.replace("```", "")
data = josn.loads(text)
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
