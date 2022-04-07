import requests
from bs4 import BeautifulSoup 
from datetime import datetime
import os
from dotenv import load_dotenv

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code


if __name__ == '__main__':
  message = '[LINE Notify] Hello World (local)' 
  load_dotenv()
  token = os.getenv('line_token')

  is_prod = os.environ.get('IS_HEROKU', None)
  if is_prod:
    token =  os.environ('line_token')
    message = '[LINE Notify] Hello World (online)' 

  lineNotifyMessage(token, message)

# # 爬列表
# #將網頁資料GET下來
# res = requests.get("https://www.gov.taipei/covid19/News.aspx?n=A626FBC2AB83E19F&sms=1A1B3A5B4DBDEDEB") 
# #將網頁資料以html.parser
# soup = BeautifulSoup(res.text,"html.parser")

# urls = soup.select("td.CCMS_jGridView_td_Class_1 span a") 
# dates = soup.select("td.CCMS_jGridView_td_Class_2 span") 

# month = datetime.today().strftime('%m')
# day = datetime.today().strftime('%d')

# for index,date in enumerate(dates):
#     split_date = date.text.split("-")
#     # 判斷是否今天
#     if(split_date[2] == day and split_date[1] == month ):
#         url = 'https://www.gov.taipei/covid19/' + urls[index]['href']
#         title = urls[index].text
#         # 爬圖片
#         res = requests.get(url) 
#         soup = BeautifulSoup(res.text,"html.parser")
#         images = soup.select("div.p span img") 
#         # 下載圖片
#         for index,image in enumerate(images):
#             #創建目錄
#             os.makedirs('./img/' + month + day, exist_ok=True)
#             res = requests.get(image['src'])
#             with open('./img/'+ month + day + '/' + str(index) + '.png','wb') as image:
#             #將圖片下載下來
#                 image.write(res.content)        
#             files = {'imageFile': open('./img/'+ month + day + '/' + str(index) + '.png', 'rb')}
#             params = {"message": title + '案例' + str(index+1)}
#             r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params, files=files)







