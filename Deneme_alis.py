

liste = []


while True :
    urun_kod = input("Ürün kodu :")
    alis_fiyat = input("Alış fiyatı :")
    
    urun_dict = {"urun_kod": urun_kod, "alis_fiyat": alis_fiyat}
    
    liste.append(urun_dict)
    print("-----------------")
    print(liste)
    print("-------****----------")
        
    for urun in liste:
        print(urun["urun_kod"])
        print(urun["alis_fiyat"])
        print("\\\\\\\\\\\\\\")
    
    

