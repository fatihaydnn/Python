

# Oyuncu classı oluşturun

# Her oyuncunun bakiyesi olacak.
# Para yatırma fonksiyonu olacak
# Zar at fonksiyonu olacak
# Bilgisayar da yatırılan parayı karşılayacak
# Yüksek zar atan tüm parayı alacak

from random import randint as r


import time

class Oyuncu:
    bakiye = 500
    def __init__(self, isim):
        self.name = isim
    def zar_at(self):
        return r(1, 6)
    def para_yatir(self, miktar):
        if miktar > self.bakiye:
            print("Yeterli bakiyeniz yoktur")
            return False
        elif miktar < 50:
            print("En az 50 kredi girmelisiniz")
            return False
        self.bakiye -= miktar
        return miktar

insan = Oyuncu("Fatih")
bilgisayar = Oyuncu("Robot")

havuz = 0

def Cikis():
    print("Oyundan Çıkılıyor...")
    time.sleep(3)

while True:
    oyuncu_miktari = int(input("Lütfen bir miktar giriniz"))
    if insan.para_yatir(oyuncu_miktari) == False:
        continue
    havuz += oyuncu_miktari
    bilgisayar_miktari = bilgisayar.para_yatir(r(50, bilgisayar.bakiye))
    print(bilgisayar.name, bilgisayar_miktari,"kadar para yatırdı")
    havuz += bilgisayar_miktari
    while True:
        x = insan.zar_at()
        y = bilgisayar.zar_at()
        if x > y:
            insan.bakiye += havuz
            print("Oyuncu zarı : {}, robot zarı {}, Toplam Bakiyeniz: {}, Kazanılan Miktar {}, oyuncu kazandı!".format(x, y, insan.bakiye, havuz))
            havuz = 0
            break
        elif x < y:
            bilgisayar.bakiye += havuz
            print(
                "Oyuncu zarı : {}, bilgisayar zarı {}, Robot Bakiye: {}, Kazanılan Miktar {}, robot kazandı!".format(x, y, bilgisayar.bakiye, havuz))
            havuz = 0
            break
        elif x == y:
            print("Berabere... Tekrar Zar Atılıyor...")
            continue

    if insan.bakiye < 50:
        print("Kaybettiniz")
        Cikis()
    elif bilgisayar.bakiye < 50:
        print("Kazandınız. Toplam Bakiyeniz {}".format(insan.bakiye))
        Cikis()


