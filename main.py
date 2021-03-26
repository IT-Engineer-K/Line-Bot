import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import datetime
def format_date(date):
    __WEEKDAY = ('月','火','水','木','金','土','日')
    return "%s" % (__WEEKDAY[date.weekday()])

now = datetime.datetime.now()
print(now.hour)
if now.hour < 12:
    time = "朝"
else:
    time = "夜"

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = format_date(datetime.date.today()) + "曜日の" + time + "です。\n薬飲んだ？")
    line_bot_api.push_message(USER_ID, messages=messages)
    
if __name__ == "__main__":
    main()