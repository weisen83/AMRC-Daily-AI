import json
import os
import urllib.request
from datetime import datetime
import time
import urllib.error


API_KEY = os.environ["GEMINI_API_KEY"]

URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.0-flash-lite:generateContent?key="
    + API_KEY
)


prompt = """
你是 AMRC Institutional Order Flow 分析師。

請產生今日市場分析。

分析：
1. XAUUSD 黃金
2. NASDAQ
3. BTC

每個商品需要：

- 市場結構 Market Structure
- 流動性 Liquidity
- Order Flow
- Trading Plan


只輸出 JSON，不要 Markdown。

格式：

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
"""


payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}


request = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json"
    }
)


for attempt in range(3):
    try:
        response = urllib.request.urlopen(request)
        break

    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("Gemini API busy, retry...")
            time.sleep(60)
        else:
            raise

else:
    print("Gemini unavailable, keep old report")
exit(0)

result = json.loads(
    response.read().decode("utf-8")
)


text = result["candidates"][0]["content"]["parts"][0]["text"]


text = text.replace("```json", "")
text = text.replace("```", "")


report = json.loads(text)


report["日期"] = datetime.now().strftime("%Y-%m-%d")


with open(
    "market.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        report,
        file,
        ensure_ascii=False,
        indent=2
    )


print("AMRC AI Report Updated")
