## 檔案結構
### templates > post.html
HTML結構
`{{參數}}` 為 `views.py` 裡 `return render(request, "post.html",{dict}` 回傳的內容

### mysite > urls.py
當使用者連到網址`/search-post`時，會去`ads.views`這個檔案執行`search_post` function

 `return render(request, "post.html",{dict}` 會回傳參數給 `post.html`

### ads > views 
相當於`main`
`initialize()` 宣告所有全域變數
`request.method == "POST"` 抓使用者上傳的檔案和要抓的分頁名稱
`makeHandle()`
`fillData()`
`makeFile()`
輸出完成訊息並列出所有產品及圖片

當使用者連到網址/search-post時，會去`ads.views`這個檔案執行`search_post`

### ads > getSheets
抓取行銷編輯的那份需求表單內容

### ads > globals
宣告全域變數

### ads > makeFile
產生輸出檔案要的所有內容，呼叫`ads.WriteFile`寫進表單

### ads > makeHandle
把device + product line 合成 handle

### ads > fillFile
把空白的資料補上

### ads > writeFile
將內容寫進指定表單

##注意事項
### credentials.json
為了讓程式在上傳heroku後還是抓的到`credentials.json`，記得join路徑
`JSON_FILE = os.path.join(Settings.BASE_DIR, "credentials.json")`
### Procfile
注意不能有副檔名！
`web: gunicorn --pythonpath mysite mysite.wsgi`
這一行指令分成兩個部分，其格式 `<process_type>: <command>` 表示：

> 啟用名為 web 的應用，用 `gunicorn` 執行 `mysite.wsgi` 這個模組。

> `Gunicorn` 是一個用 Python 開發的 WSGI 工具，可以用來執行 Django 的網站。

### Permission denied (publickey)
請透過下列指令新增 public key，然後再重新 git push。

`heroku keys:add`

## git push
`git add .`

`git commit -m "yaya"`

`git push heroku master`

## 網站初始化
* 在第一次上傳專案後，我們必須稍微做一點設定，讓 Heroku 有正確的初始環境。首先用下面的指令，告訴 Heroku 我們需要一台機器（Heroku 叫 dyno）來執行網站：

`heroku ps:scale web=1`

* 接著用下面的指令初始化資料庫：

`heroku run python mysite/manage.py migrate`
