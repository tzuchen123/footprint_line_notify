# 使用line notify 每日自動通知確診足跡
幫朋友寫的小玩具，每天去網站爬確診個案公共場域活動史，並用line notify 傳送，簡單紀錄之。

1. 爬蟲
1. line notify
1. heroku 自動排程

## 爬蟲
關於爬蟲的教學網路上很多，就不贅述了。


## line notify
### 發行權杖
line notify登入後，右上角點選"個人頁面"，換頁後，往下拉在發行存取權杖（開發人員用）區塊點選"發行權杖"，該填該選的弄好，把發行的權杖(token)記下來，如果沒記下來就關掉，是無法再看到的，要再重新發行一次。

### 設定專案env
```
$ pip install python-dotenv
```
安裝dotenv，並把.env.example改名成.env，把剛剛申請的token貼上去。

## 在heroku上發布
註冊、登入、連結GitHub、Automatic deploys一樣不贅述。

### heroku depoly需要的檔案
專案裡面都寫了，簡單解說如下。
- Procfile
- requirements.txt
    <br>專案所需的套件。
```
<!-- 顯示當前這台電腦所安裝的所有套件 -->
$ pip3 freeze
```    
```
<!-- 安裝文件中的套件 -->
$ pip3 install -r requirements.txt
```
- runtime.txt
<br>用來標示使用的程式語言運行環境與版本。
[這裡查目前支援的版本](https://devcenter.heroku.com/articles/python-support#supported-python-runtimes)

### 設定heroku Config Vars
點選Settings分頁，分別設定兩組Config Vars<br>
{
    IS_HEROKU:TRUE,
    line_token : "剛剛貼在.env的token"
}

### heroku resource

#### Dynos 
內容就是寫在Procfile的command，每次push都會執行一次，如果不想要每次push都執行一次，記得改off。

#### Add-ons
搜尋Heroku Scheduler 並安裝，用來設定定時排程。會依照schedule去 Run Command。<br>
搜尋JawsDB MySQL free mysql db。

#### heroku log
如果一直不能work，Open app 旁邊的More點下去，View logs。
<br>
<small>居然一直眼殘沒發現，筆記一下</small>

