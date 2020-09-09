from django.contrib import messages
global url
from django.shortcuts import render
import ads.globals as Var
import ads.getSheet as getSheet
import ads.fillFile as fillFile
import ads.makeFile as makeFile
import ads.makeHandle as makeHandle
import re
from django.shortcuts import redirect

import os
import mysite.settings as Settings

# 回傳 render() ，留意參數的順序，第一個是 request ，第二個是樣板檔案，第三個則是樣板對應變數的字典
def search_post(request):

    Var.initialize()
    global uploadedFile

    # Var.uploadedFile 存取上傳檔案內容，存進google_ads.csv
    if request.method == "POST":
        # 抓取分頁名稱
        sheetName = request.POST['sheetName']
        Var.fileName =  sheetName.replace("/","")
        if sheetName == "":
            messages.info(request, '請輸入分頁名稱')
            return redirect("/search-post")

        # 抓取上傳檔案
        try :
            uploadedFile = request.FILES['uploadedFile'].read()
        except:
            messages.info(request, '請選擇檔案')
            return redirect("/search-post")

        # 選擇國家
        pattern = '^[a-zA-z]{2}'
        Var.country = re.match(pattern,sheetName).group()

        # 取得線上表單資料(行銷給的50個產品)
        wrongSheet = getSheet.main(sheetName)
        if wrongSheet:
            messages.info(request, '抓不到表單')
            return redirect("/search-post")

        # 上傳檔案
        uploadedFile = str(uploadedFile, encoding = "utf-8")
        file = open(Var.fileName + '.csv', 'w', encoding='utf8',newline='')
        file.write(uploadedFile)
        file.close()

        # 從產品名產生handle (小寫含dash)
        makeHandle.makeHandle()

        # 把空白資料補齊
        fillFile.fillData()

        # 把不需要資料刪除
        countRow = makeFile.makeFile()

        # 完成
        text = 'DONE, 共生成 {} 筆資料'.format(str(countRow))
        messages.info(request, text)

        # 列出圖片
        url = Var.new_df['Variant Image'].tolist()
        handle = Var.new_df['Handle'].tolist()
        title = Var.new_df['Title'].tolist()
        sku = Var.new_df['Variant SKU'].tolist()
        imgUrl = []
        for i in range(len(url)):
            imgUrl.append({"url": url[i], "handle": handle[i], "title": title[i], "sku": sku[i]})

        return render(request, "post.html", {"url": imgUrl})

    else:
        return render(request, "post.html")