import ads.globals as Var

def makeHandle():
    # 把device + product line 合成 handle
    for i in range(len(Var.sku)):
        # productLine
        if (Var.productLine[i] == "Mod NX"):
            tempProductLine = "mod-nx-backplate"
        elif  (Var.productLine[i] == "SolidSuit"):
            if ("iPhone" in Var.device[i]):
                tempProductLine = "solidsuit-classic"
            else:
                tempProductLine = "solidsuit-android"
        else:
            tempProductLine = Var.productLine[i]

        # device
        if (Var.device[i] == "iPhone SE (2nd generation)"):
            tempDevice = "iPhone SE 2nd generation"
        elif (Var.device[i] == "Samsung Galaxy Note9"):
            tempDevice = "Samsung Galaxy Note 9"
        elif (Var.device[i] == "Samsung Galaxy Note10"):
            tempDevice = "Samsung Galaxy Note 10"
        elif (Var.device[i] == "Samsung Galaxy Note10+"):
            tempDevice = "Samsung Galaxy Note 10 plus"
        else:
            tempDevice = Var.device[i].replace("+","-plus").\
                replace(" / ", "-").\
                replace("/", "-").\
                replace(" (4G)", "")


        # 從表單合併出 handle
        temp = (tempDevice + "-" + tempProductLine + "-" + Var.designSku[i]).lower()
        Var.handle.append(temp.replace(' ','-'))


        #  從表單合併出 device
        Var.dashDevice.append(tempDevice.replace(' ','-').lower())

    print(Var.handle)