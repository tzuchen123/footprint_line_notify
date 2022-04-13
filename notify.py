#coding=UTF-8
import requests
from bs4 import BeautifulSoup 
from datetime import datetime
import os
from dotenv import load_dotenv

def crawler(url):
    # 獲得網頁資料
    res = requests.get(url) 
    #將網頁資料以html.parser
    soup = BeautifulSoup(res.text,"html.parser")
    return soup

def checkUpload():
    headers = {"Authorization": "Bearer " + os.environ.get('line_token')}
    soup = crawler("https://www.gov.taipei/covid19/News.aspx?n=A626FBC2AB83E19F&sms=1A1B3A5B4DBDEDEB")
    urls = soup.select("td.CCMS_jGridView_td_Class_1 span a") 
    dates = soup.select("td.CCMS_jGridView_td_Class_2 span") 

    month = datetime.today().strftime('%m')
    day = datetime.today().strftime('%d')

    for row_index,date in enumerate(dates):
        split_date = date.text.split("-")
        # 判斷是否今天
        if(split_date[2] == '12' and split_date[1] == month ):
            # url = 'https://www.gov.taipei/covid19/' + urls[row_index]['href']
            # title = urls[row_index].text
            # # 爬圖片
            # soup = crawler(url)
            # images = soup.select("div.p span img") 

            # for index,image in enumerate(images):
            #     res = requests.get(image['src'])
            #     with open(str(index) + '.png','wb') as f:
            #         #將圖片下載下來
            #         f.write(res.content)
                
            #     #開圖片
            #     img = open(str(index) + '.png', 'rb') 
            #     #傳line
            #     files = {'imageFile': img}
            #     params = {"message": '第' + str(row_index +1 ) +'篇' + title + '案例' + str(index+1)}
            #     r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params, files=files)
            #     #關圖片
            #     img.close()
            #     #刪圖片 
            #     os.remove(str(index) + '.png')
            
            os.environ['sending_status']  = 'False'
            
    return 'check finish'


def clearSendingStatus():
    os.environ['sending_status']  = True
    return 'reset finish'

load_dotenv()
sendingStatus = os.environ.get('sending_status')
res = 'No need check'
if  sendingStatus:
    res = checkUpload()
print(res)






