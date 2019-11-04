class Karakter:
    isim = ""
    meslek = ""
    irk = ""
    level = 1
    silah = 0
    zirh = 0
    can = 100

    def Saldir(self):
        return self.silah + self.level

    def Korun(self):
        return self.zirh + self.level

    def Kac(self):
        print("Savaştan Kaçıldı!")
    # def Zirh_Belirle(self, kazanilan_level):
    #     self.zirh *= kazanilan_level


# bir düşman karakteri bir oyuncu karakteri oluşturun.
# oyuncu kaçana kadar veya galip/kaybedene kadar oyunu devam ettirin.


oyuncu = Karakter()
oyuncu.isim = "Can"
oyuncu.meslek = "Silahşör"
oyuncu.silah = 10
oyuncu.irk = "İnsan"
oyuncu.level = 3
oyuncu.zirh = 0

dusman = Karakter()
dusman.isim = "Bilgisayar"
dusman.meslek = "Okçu"
dusman.silah = 5
dusman.irk = "Ork"
dusman.level = 2
dusman.zirh = 0

while True:
    sonuc = input("Saldırmak için s'ye, kaçmak için k'ye basabilirsiniz")
    if sonuc == "s":
        dusman.can -= oyuncu.Saldir() - dusman.Korun()
        oyuncu.can -= dusman.Saldir() - oyuncu.Korun()
        print("Verdiğiniz hasar:", oyuncu.Saldir()-dusman.Korun())
        print("Aldığınız hasar:", dusman.Saldir()-oyuncu.Korun())
        print("Oyuncu kalan Can", oyuncu.can)
        print("Düşman kalan Can", dusman.can)
        # print(
        #     "Saldırınız sonucunda verdiğiniz hasar {}. Düşmanın kalan canı => {}. Aldığınız hasar=> {}, Kalan canınız=> {}".format((oyuncu.Saldir() - dusman.Korun(), dusman.can, dusman.Saldir() - oyuncu.Korun(), oyuncu.can)))
    elif sonuc == "k":
        oyuncu.Kac()
        break
    if (dusman.can <= 0 and oyuncu.can > 0):
        print("Tebrikler!")
        break
    elif (dusman.can <= 0 and oyuncu.can <= 0):
        print("Bu dünya kimseye kalmaz")
        break
    elif (dusman.can > 0 and oyuncu.can <= 0):
        print("Düşman Kazandı!")
        break
