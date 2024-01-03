import math

dolar=28.68

while True:
    fiyat = input("Syıyı giriniz: ")
    
    
    fiyat = fiyat.replace(".","")
    fiyat = fiyat.replace(",", ".")  # Virgülü noktaya dönüştür
    fiyat = float(fiyat)
    
    fiyat = fiyat-(fiyat*7/100)
    fiyat = fiyat-(fiyat*15/100)
    fiyat = fiyat/dolar
    fiyat=str(round(fiyat,2))
    fiyat = fiyat.replace(".", ",")
    
    print(fiyat)
    
    