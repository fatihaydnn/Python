# Televizyon Kumandası Uygulaması:

"""
İşlemler:
1. Televizyonu Aç  - tv durumu = "Açık"
2. Televizyonu Kapat - tv durumu = "Kapalı"
3. Televizyon Bilgileri - o anki kanal, ses durumu, tüm kanallar.
4. Kanal Ekle - kanal listesine kanalı ekle
5. Rastgele Kanal Aç - random bir kanalı açar
6. Sesi Azalt Arttır - ses arttır/azalt
"""

from random import randint as r

class Kumanda:
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        print("Kumanda Oluşturuluyor")
        self.tv_sesi = tv_ses
        self.tv_durumu = tv_durum
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def ses_azalt_arttir(self):
        while True:
            karakter = input("Ses Azaltmak için '<', arttırmak için '>' , Çıkış için 'q' ya basınız..")
            if karakter == '<':
                if self.tv_sesi != 0:
                    self.tv_sesi -= 1
                    print("Ses : {}".format(self.tv_sesi))
            elif karakter == '>':
                if self.tv_sesi != 15:
                    self.tv_sesi += 1
                    print("Ses : {}".format(self.tv_sesi))
            elif karakter == 'q':
                print("Ses : {}".format(self.tv_sesi))
                break

    def tv_kapat(self):
        print("TV Kapatılıyor..")
        self.tv_durumu = "Kapalı"
    def tv_ac(self):
        print("TV Açılıyor...")
        self.tv_durumu = "Açık"

    def __str__(self):
        return "TV Durumu {}\nSes: {}\nŞu Anki Kanal:{}\n".format(self.tv_durumu,self.tv_sesi,self.kanal)

    def rastgele_kanal(self):
        rastgele = r(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu an açık olan kanal",self.kanal)

    def kanal_ekle(self, kanal):
        print("Kanal Eklendi", kanal)
        self.kanal_listesi.append(kanal)


kumanda = Kumanda()


print("""
İşlemler:
1. Televizyonu Aç
2. Televizyonu Kapat
3. Televizyon Bilgileri
4. Kanal Ekle
5. Rastgele Kanal Aç
6. Sesi Azalt Arttır
""")

while True:
    islem = input("İslem Seçiniz")
    if islem == 'q':
        print("Programdan çıkılıyor")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        print(kumanda)
    elif islem == "4":
        kanallar = input("Eklemek istediğiniz kanalları ',' ile ayırarak giriniz")
        eklenecekler = kanallar.split(",")
        for x in eklenecekler:
            kumanda.kanal_ekle(x)
        print("Kanal Ekleme Başarılı")
    elif islem == "5":
        kumanda.rastgele_kanal()
    elif islem == "6":
        kumanda.ses_azalt_arttir()
    else:
        print("Geçersiz İşlem")




