# 使用line notify 每日自動通知確診足跡
幫朋友寫的小玩具，每天去網站爬確診個案公共場域活動史，並用line notify 傳送。主要寫的語言非python，程式碼多是辜狗來的，再湊成一台拼裝車，故可能有很奇怪的地方。
<br>簡單紀錄網上比較少寫到的地方，供之後回憶用。

1. 爬蟲
1. line notify
1. heroku 自動排程

## 爬蟲
關於爬蟲的教學網路上很多，就不贅述了。


## line notify
### 發行權杖
line notify登入後，右上角點選"個人頁面"，換頁後，往下拉在發行存取權杖（開發人員用）區塊點選"發行權杖"，該填該選的弄好，把發行的權杖(token)記下來，如果沒記下來就關掉，是無法再看到的，要再重新發行一次。

### 存在專案env
```
$ pip install python-dotenv
```
安裝dotenv，並把.env.example改名成.env，把剛剛申請的token貼上去。

## 在heroku上發布
註冊、登入、連結GitHub、Automatic deploys一樣不贅述。
