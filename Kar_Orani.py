
dolar= 28.76

while True:
    urun_gelis= input("Urun geliş fiyatı : ")
    urun_guncel= input("Urun guncel fiyat kdvsiz : ")
    urun_gelis= float(urun_gelis)
    urun_gelis= urun_gelis*float(dolar)
    urun_guncel= float(urun_guncel)
    
    oran=((urun_guncel - urun_gelis)*100)/urun_gelis
    
    print(oran)
