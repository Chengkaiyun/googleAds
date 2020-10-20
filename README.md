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

