# coding=UTF-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv
import pymysql


def crawler(url):
    # 獲得網頁資料
    res = requests.get(url)
    # 將網頁資料以html.parser
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


load_dotenv()

location="桃園市"

headers = {"Authorization": "Bearer " + os.environ.get('line_token')}
soup = crawler("https://www.cdc.gov.tw/Category/List/_FFjBSOizDNbJZZV1Bosew")  # 衛福部網站
countyList = soup.select("div.col-md-12 ul li a")  # 縣市連結


for countyurl in countyList:
    if countyurl.text == location:
        fullLink = "https://www.cdc.gov.tw/"+ countyurl["href"]
print(fullLink)

soup = crawler(fullLink)
photoList=soup.select("div.download p a")

# 從照片list取出照片連結
for photos in photoList:
    photoPosts="https://www.cdc.gov.tw/"+photoList["href"]
    #photoDates=photo.get("title")[-15:-11] #取得日期

print(photoPosts)


# soup = crawler("https://www.gov.taipei/covid19/News.aspx?n=A626FBC2AB83E19F&sms=1A1B3A5B4DBDEDEB")
# urls = soup.select("td.CCMS_jGridView_td_Class_1 span a") 
# dates = soup.select("td.CCMS_jGridView_td_Class_2 span") 
# print(urls)
