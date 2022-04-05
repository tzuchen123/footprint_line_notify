import requests
from bs4 import BeautifulSoup 
from datetime import datetime

# 爬所有發文
#將網頁資料GET下來
r = requests.get("https://www.gov.taipei/covid19/News.aspx?n=A626FBC2AB83E19F&sms=1A1B3A5B4DBDEDEB") 
#將網頁資料以html.parser
soup = BeautifulSoup(r.text,"html.parser")

urls = soup.select("td.CCMS_jGridView_td_Class_1 span a") 
dates = soup.select("td.CCMS_jGridView_td_Class_2 span") 

month = datetime.today().strftime('%m')
day = datetime.today().strftime('%d')
for index,date in enumerate(dates):
    split_date = date.text.split("-")
    # 判斷是否今天
    if(split_date[2] == day and split_date[1] == month ):
        url = 'https://www.gov.taipei/covid19/' + urls[index]['href']
        print(url)
        # 在爬一次
        r = requests.get(url) 
        soup = BeautifulSoup(r.text,"html.parser")
        images = soup.select("div.p span img") 
        for image in images:
            print(image['src'])


# linetes