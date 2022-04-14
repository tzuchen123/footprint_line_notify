#coding=UTF-8
import requests
from bs4 import BeautifulSoup 
from datetime import datetime,timezone,timedelta
import os
from dotenv import load_dotenv
import pymysql


def crawler(url):
    # 獲得網頁資料
    res = requests.get(url) 
    #將網頁資料以html.parser
    soup = BeautifulSoup(res.text,"html.parser")
    return soup

def checkStatus():
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT * from notify where id = 0")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    return data[1]
 
def setStatus(status):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    mysql = "UPDATE b13w1ozz6z1n6dv4.notify set has_sent= " + str(status) + " where id =0"
    cursor.execute(mysql)
    # 使用 fetchone() 方法获取单条数据.
    db.commit()
    return 'ok'

load_dotenv()
# 打开数据库连接
db = pymysql.connect(host=os.environ.get('db_host'),
                    user=os.environ.get('db_user'),
                    password=os.environ.get('db_password'),
                    database=os.environ.get('db_database'))

utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
tw_time = utc_time.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
if tw_time.strftime('%H') == '01':
    setStatus(0)

else:   
    status = checkStatus()
    if  status == 0:
        headers = {"Authorization": "Bearer " + os.environ.get('line_token')}
        soup = crawler("https://www.gov.taipei/covid19/News.aspx?n=A626FBC2AB83E19F&sms=1A1B3A5B4DBDEDEB")
        urls = soup.select("td.CCMS_jGridView_td_Class_1 span a") 
        dates = soup.select("td.CCMS_jGridView_td_Class_2 span") 

        month = tw_time.strftime('%m')
        day = tw_time.strftime('%d')

        for row_index,date in enumerate(dates):
            split_date = date.text.split("-")
            # 判斷是否今天
            if(split_date[2] == day and split_date[1] == month ):
                url = 'https://www.gov.taipei/covid19/' + urls[row_index]['href']
                title = urls[row_index].text
                # 爬圖片
                soup = crawler(url)
                images = soup.select("div.p span img") 
                for index,image in enumerate(images):
                    res = requests.get(image['src'])
                    with open(str(index) + '.png','wb') as f:
                        #將圖片下載下來
                        f.write(res.content)
                    
                    #開圖片
                    img = open(str(index) + '.png', 'rb') 
                    #傳line
                    files = {'imageFile': img}
                    params = {"message": '第' + str(row_index +1 ) +'篇' + title + '案例' + str(index+1)}
                    r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params, files=files)
                    #關圖片
                    img.close()
                    #刪圖片 
                    os.remove(str(index) + '.png')

                setStatus(1)
# # 关闭数据库连接
db.close()
print('finish')
