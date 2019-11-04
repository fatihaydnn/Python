# Bağlantı için gerekli olan kütüphaneleri indiriyoruz.
# Pymongo indirmek için settings altında, project interpreter içerisinde + tuşuna tıklayarak açılan pencerede pymono yazıp install etmemiz yeterlidir.

from pymongo import MongoClient
from bson.objectid import ObjectId

# direk ObjectId ile çalışmamız için
# Bağlantı default değerlerimizde olduğu için, ekstra bir değer gerek yoktur ancak istersek;
# client = MongoClient("localhost", 27017)
# şeklinde tanımlanabilir

# Bağlantı kodumuz:
connection = MongoClient()
# Eğer veritabanı yoksa oluşacak
mydb_db = connection.MyDB
# collection yakalanır.
products = mydb_db.Products
# Kendimize yeni bir entry oluşturalım
entry = {"Name": "Yedigun",
         "Price":6.75,
         "Stock":15}
# Tabloya üstteki entry değerini girmek için insert komutunu kullanabiliriz
# products.insert_one(entry)
# Girilen değeri ekrana görüntlemek için;
print(list(products.find()))
print(list(products.find({"Name":"Yedigun"})))


# Güncelleme İşlemleri

products.update_one({"_id":ObjectId("5d57c6a88801aa15546b8214")},{"$set":{"Name":"AyranModified"}})
print(list(products.find({"Name":"AyranModified"})))

# Silme İşlemleri
# Eğer belirttiğimiz koşula uyan tğm kayıtları silmek istiyorsak
silinen_urunler = products.delete_many({"Name":"Yedigun"})
print("Silinen urun sayısı:", silinen_urunler.deleted_count)

# Bir koleksionu kaldırmak için
# products.drop()



#Bağlantıyı kapatmak için
connection.close()
