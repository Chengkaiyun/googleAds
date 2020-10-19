import pandas as pd
import ads.globals as Var
import mysite.settings as Settings
import pandas as pd
import os

def makeFile():
    global indexColor
    Var.new_df = pd.DataFrame(columns = Var.df.columns)

    for i in range(len(Var.df.index)):
        # 抓需要的產品
        if(Var.df['Handle'][i] in Var.handle and Var.df['Variant SKU'][i] in Var.sku):

            # 改顏色寫法(Option1 Value)
            indexHandle = [index for index, value in enumerate(Var.handle) if value == Var.df['Handle'][i]]
            indexColor = indexHandle[0]

            # 把顏色 大寫改成小寫 空格改成_
            Var.df['Option1 Value'][i] = Var.caseColor[indexColor].replace(" ","_").lower()

            # 從表單合併出圖名
            if (Var.bumperColor[indexColor].strip() != ""):
                imgName = "merged-" + Var.bumperColor[indexColor] + "_" + \
                          Var.sku[indexColor] + "_" + \
                          Var.dashDevice[indexColor]
            else:
                imgName = "merged-" + Var.sku[indexColor] + "_" + \
                          Var.dashDevice[indexColor]

            # 放新圖片URL
            url = Var.url_dict[Var.country] + imgName + ".png"
            Var.df['Image Src'][i] = url
            Var.df['Variant Image'][i] = url

            # Mod 要改價錢 + SEO
            if ("mod-nx" in Var.df['Handle'][i]):
                BumperPrice = Var.countryInfo[Var.country][0]
                Var.df['Variant Price'][i] = round(Var.df['Variant Price'][i] + float(BumperPrice),2)

                SEO = Var.countryInfo[Var.country][1]
                Var.df['SEO Description'][i] = SEO
                Var.df['Body (HTML)'][i] = SEO

                # IO/FR MOD "背板"要刪掉
                Var.df['Title'][i] = Var.df['Title'][i].replace(Var.backplate[Var.country], '')

            # Airpods 要 + SEO
            if ("airpods-case" in Var.df['Handle'][i]):
                SEO = Var.countryInfo[Var.country][2]
                Var.df['SEO Description'][i] = SEO
                Var.df['Body (HTML)'][i] = SEO

            # SSA 要 + SEO
            if ("airpods-case" in Var.df['Handle'][i]):
                SEO = Var.countryInfo[Var.country][3]
                Var.df['SEO Description'][i] = SEO
                Var.df['Body (HTML)'][i] = SEO

            # 存入新dataFrame
            Var.new_df = Var.new_df.append(Var.df.loc[i],ignore_index=True)

    # Handle 加上 -for-google
    Var.new_df['Handle'] = Var.new_df['Handle'] + "-for-google"

    # SKU 加上 -google
    Var.new_df['Variant SKU'] = Var.new_df['Variant SKU'] + "-google"

    # 移除/加上 tag
    Var.new_df['Tags'] = [tag.replace("discountable, ","") for tag in Var.new_df['Tags']]
    Var.new_df['Tags'] = [tag.replace("searchable, ", "") for tag in Var.new_df['Tags']]
    Var.new_df['Tags'] = [tag.replace("indexable, ", "") for tag in Var.new_df['Tags']]
    Var.new_df['Tags'] = Var.new_df['Tags'] + ", google-only, type-ignore, offline"

    # 寫入檔案 C:\Users\user/Downloads/
    FILE_ROOT = 'C:/Users/user/Downloads/'
    #FILE_ROOT = os.path.expanduser("~") + "/Downloads/" + Var.fileName + '.csv'
    Var.new_df.to_csv(FILE_ROOT, index=False, encoding='utf_8_sig')
    print(FILE_ROOT)





    return len(Var.new_df['Handle'])