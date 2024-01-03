from influxdb import InfluxDBClient

# InfluxDB client oluşturun
client = InfluxDBClient(host='192.168.253.71', port=8086, username='root', password='Deneme123!', database='satisdb')

# İlk tablodan veriyi alın
query1 = 'SELECT * FROM "dmo_veri" order by time desc limit 36'
result1 = client.query(query1)
a=1
# İkinci tablodan veriyi alın
query2 = 'SELECT * FROM "urunler"'
result2 = client.query(query2)

# Sonuçları işleyerek iç katman birleştirmesi yapın
for point1 in result1.get_points():
    
    for point2 in result2.get_points():
        
        if point1['number'] == point2['number']:
            print("Birleştirilmiş Veri: ", point1, point2)
            a=a+1
            print(a)

# Bağlantıyı kapatın
client.close()

##SELECT * FROM "urunler" order by time desc limit 1