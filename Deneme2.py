import json


d_adi = "alis_fiyat_list.json"
d = open(d_adi, 'r')
djs = json.load(d)

d.close()   

for dd in djs:
    if dd["urun_kod"]=="123456-PPPPP":
        print(dd["alis_fiyat"])


#json_data = json.dumps(liste, ensure_ascii=False, indent=4)
