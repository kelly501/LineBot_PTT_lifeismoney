import requests as requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

if __name__ == '__main__':
    r = requests.get('https://www.ptt.cc/bbs/Lifeismoney/index.html', timeout=2)
    soup = BeautifulSoup(r.text, "html.parser")  # 解析器
    links = soup.find_all('a')

    result = "PTT省錢最新資訊: \n"
    title = ""
    href = ""
    # 過濾
    for link in links:
        if 'href' not in link.attrs:  # 回傳此Tag可獲取的屬性
            continue
        if not link['href'].startswith('/bbs/Lifeismoney/M.'):
            continue
        if link['href'] in href:
            continue
        if link.text in title:
            continue
        title = title + link.text
        href = href + link['href']
        result = result + link.text + "\n" + "ptt.cc" + link['href'] + "\n"

line_uuid = LINE_UUID
line_bot_api = LineBotApi(TOKEN)
line_bot_api.push_message(
    line_uuid,
    TextSendMessage(text=result))
