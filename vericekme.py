import time
import requests
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient

# InfluxDB bağlantı bilgileri
host = '192.168.253.71'
port = 8086
user = 'root'
password = 'Deneme123!'
dbname = 'satisdb'

client = InfluxDBClient(host, port, user, password, dbname)
# InfluxDB bağlantı bilgileri

base_url ="https://www.dmo.gov.tr/EMagaza/Magaza/Standart/170027?s=&k=&p={}&d=TM&e=1" ## {} kısmını formatını değiştirerek içerisine i değişkeni gelicek
while True:
    for i in range(1,4): 
        # Veri çekmek istediğiniz URL'yi buraya ekleyin
        url =base_url.format(i)  # URL'yi biçimlendirin
    
        # Web sayfasına GET isteği gönderin
        response = requests.get(url)
    
        # Yanıtın durum kodunu kontrol edin
        if response.status_code == 200:
            # İçeriği BeautifulSoup kullanarak işleyin
            soup = BeautifulSoup(response.content, 'html.parser')
    
            # Örnek bir işlem: tüm başlıkları alın
            divs = soup.find_all("div", class_="product-item")
        
        
        
            for div in divs:
                try:
                    fiyat = div.find("span", class_="price-current")
                    number = div.find("div", class_="brand")
                    number = number.find("span")
                    
                    
                    fiyat = fiyat.text.strip().replace(".","")
                    fiyat = fiyat.replace("₺", "")  # Para birimi simgesini kaldır
                    fiyat = fiyat.replace(",", ".")  # Virgülü noktaya dönüştür
                    fiyat = float(fiyat)*100/120
            
                    print(fiyat)
                    print("&&&&&&")
                    print(number.text.strip())
                    print("----------------")
                    json_body = [
                        {
                            "measurement": "dmo_veri",
                            "tags": {
                                "number": number.text.strip()
                            },
                            "fields": {
                                "fiyat": fiyat
                            }
                        }
                    ]
                    client.write_points(json_body)
                except:
                        a=1
                
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        else:
                    print(f'İstek başarısız oldu. Durum kodu: {response.status_code}')
    time.sleep(86400)
        
        
        
        
        
        
        