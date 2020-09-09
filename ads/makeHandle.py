import ads.globals as Var

def makeHandle():
    # 把device + product line 合成 handle
    for i in range(len(Var.sku)):
        if (Var.productLine[i] == "Mod NX"):
            tempProductLine = "mod-nx-backplate"
        else:
            tempProductLine = Var.productLine[i]

        if (Var.device[i] == "iPhone SE (2nd generation)"):
            tempDevice = "iPhone SE 2nd generation"
        else:
            tempDevice = Var.device[i].replace("+","-plus").replace(" / ", "-").replace("/", "-")


        # 從表單合併出 handle
        temp = (tempDevice + "-" + tempProductLine + "-" + Var.designSku[i]).lower()
        Var.handle.append(temp.replace(' ','-'))

        #  從表單合併出 device
        Var.dashDevice.append(tempDevice.replace(' ','-').lower())