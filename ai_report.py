import json
from datetime import datetime
import urllib.request
import os


API_KEY = os.environ["GEMINI_API_KEY"]

URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.0-flash:generateContent?key="
    + API_KEY
)


prompt = """
你是 AMRC Order Flow 交易分析師。

請產生今日市場分析。

分析商品:
1. XAUUSD 黃金
2. NASDAQ
3. BTC

使用：
Market Structure
Liquidity
Order Flow
Trading Plan

輸出 JSON 格式:

{
"日期":"",
"狀態":"",
"市場":[
{
"商品":"",
"市場結構":"",
"流動性":"",
"訂單流":"",
"交易計畫":""
}
]
}

不要加入其他文字。
"""


data = {
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


req = urllib.request.Request(
    URL,
    data=json.dumps(data).encode(),
    headers={
        "Content-Type":"application/json"
    }
)


response = urllib.request.urlopen(req)

result = json.loads(
    response.read()
)


text = result["candidates"][0]["content"]["parts"][0]["text"]


text = text.replace("```json","")
text = text.replace("```","")


report = json.loads(text)


report["日期"] = datetime.now().strftime("%Y-%m-%d")


with open(
    "market.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        ensure_ascii=False,
        indent=2
    )


print("AMRC AI Update Complete")
