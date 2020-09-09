import ads.globals as Var
import ads.getSheet as getSheet
import pandas as pd
import numpy as np
import ads.globals as Var

def getData():
    Var.df = pd.read_csv(Var.fileName + '.csv')
    return len(Var.df.index)

# 把空白的資料補上
def fillData():
    lenData = getData()
    for i in range(lenData):
        if pd.isnull(Var.df['Title'][i]):
            Var.df['Title'][i] = Var.df['Title'][i-1]
            Var.df['Vendor'][i] = Var.df['Vendor'][i-1]
            Var.df['Type'][i] = Var.df['Type'][i-1]
            Var.df['Tags'][i] = Var.df['Tags'][i-1]
            Var.df['Published'][i] = Var.df['Published'][i-1]
            Var.df['Option1 Name'][i] = Var.df['Option1 Name'][i-1]
            Var.df['Gift Card'][i] = Var.df['Gift Card'][i-1]

    Var.df['Option2 Name'] = np.nan
    Var.df['Option2 Value'] = np.nan
    Var.df['Option3 Name'] = np.nan
    Var.df['Option3 Value'] = np.nan
    Var.df['Body(HTML)'] = np.nan

    #print(Var.df)
