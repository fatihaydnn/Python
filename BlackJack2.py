import random as rnd
import os




# Bir Deste Oluşturunuz
# Destede: 2,3,4,5,....,10,11,12,13,14 sayılarından olmalı. Bunlar 4 kez tekrar etmeli.

deste = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4



# random shuffle araştrın

# A => 1 veya 11
# J-Q-K => 10


# Kağıtları bilgisayara ve kendimize dağtmak için
def dagit(deste):
    eldeki_kartlar = []
    for x in range(2):
        rnd.shuffle(deste)
        kart = deste.pop()
        if kart == 11:
            kart = "J"
        if kart == 12:
            kart = "Q"
        if kart == 13:
            kart = "K"
        if kart == 14:
            kart = "A"
        eldeki_kartlar.append(kart)
    return eldeki_kartlar

# Anlık bir elin toplamını vermesi için
def el_toplami(eldeki_kartlar):
    toplam = 0
    for kart in eldeki_kartlar:
        if kart == "J" or kart == "Q" or kart == "K":
            toplam += 10
        elif kart == "A":
            if toplam >= 11:
                toplam += 1
            else:
                toplam += 11
        else:
            toplam += kart
    return toplam


# Bir adet kart oyuncuya sunulacak

def kart_iste(eldeki_kartlar):
    kart = deste.pop()
    if kart == 11:
        kart = "J"
    if kart == 12:
        kart = "Q"
    if kart == 13:
        kart = "K"
    if kart == 14:
        kart = "A"
    eldeki_kartlar.append(kart)
    return eldeki_kartlar


# Ekrandaki yazıları temizler. Yeni oyun için
def temizle():
    if os.name == 'nt':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')
    return

# Oyuncuların elindeki kartlar ve toplamları bastırılır

def durumu_goster(kurpiyer_eli, oyuncu_eli):
    temizle()
    print("Kurpiyerin elinde {} vardır. Toplamı ise: {}".format(kurpiyer_eli, el_toplami(kurpiyer_eli)))
    print("Oyuncunun elinde {} vardır. Toplamı ise: {}".format(oyuncu_eli, el_toplami(oyuncu_eli)))
    return
# 21 oldu mu kontorlü
def blackjack(kurpiyer_eli, oyuncu_eli):
    if el_toplami(oyuncu_eli) == 21:
        print("21!! Kazandınız!")
    elif el_toplami(kurpiyer_eli) == 21:
        print("Kaybettiniz... Kurpiyer 21 ile kazandı!")
    return

# Kazanma-Kaybetme Durumu kontrolü
def puan_kontorlu(kurpiyer_eli, oyuncu_eli):
    if el_toplami(oyuncu_eli) == 21:
        print("21!! Kazandınız\n")
        tekrar_oyna()
    elif el_toplami(kurpiyer_eli) == 21:
        print("Kaybettiniz.. Kurpiyer 21 ile kazandı\n")
        tekrar_oyna()
    elif el_toplami(oyuncu_eli) > 21:
        print("Kaybettiniz... Eliniz 21'i geçti")
        tekrar_oyna()
    elif el_toplami(kurpiyer_eli) > 21:
        print("Kazandınız.. Kurpiyer 21'i geçti")
        tekrar_oyna()
    elif el_toplami(oyuncu_eli) > el_toplami(kurpiyer_eli):
        print("Kazandınız, Elinizde daha yüksek bir puan var")
    elif el_toplami(kurpiyer_eli) > el_toplami(oyuncu_eli):
        print("Kaybettiniz.. Kurpiyerin elinde daha yüksek puan var")
    return

# Tekrar oyunu sıfırlayıp oynayabilmek için
def tekrar_oyna():
    temizle()
    karar = input("Tekrar Oynamak İster Misiniz? ([E]vet/[H]ayır)").lower()
    if karar == "e":
        play()
    else:
        print("Hoşçakalın")
        exit()

# Oyunun Oynanması için
def play():
    secim = 0
    print("Blackjack Oyununa Hoşgeldiniz")
    kurpiyer_eli = dagit(deste)
    oyuncu_eli = dagit(deste)
    while secim != "q":
        durumu_goster(kurpiyer_eli, oyuncu_eli)
        blackjack(kurpiyer_eli, oyuncu_eli)
        secim = input("[K]art ister misiniz?, [D]urmak ister misiniz?, [B]ırakmak ister misiniz?").lower()
        temizle()
        if secim == "k":
            kart_iste(oyuncu_eli)
            while el_toplami(kurpiyer_eli) < 14 or (el_toplami(kurpiyer_eli) < el_toplami(oyuncu_eli) and el_toplami(oyuncu_eli) <= 20):
                kart_iste(kurpiyer_eli)
            durumu_goster(kurpiyer_eli, oyuncu_eli)
            puan_kontorlu(kurpiyer_eli, oyuncu_eli)
        elif secim == "d":
            while el_toplami(kurpiyer_eli) < 14 or (
                    el_toplami(kurpiyer_eli) < el_toplami(oyuncu_eli) and el_toplami(oyuncu_eli) <= 20):
                kart_iste(kurpiyer_eli)
            durumu_goster(kurpiyer_eli, oyuncu_eli)
            puan_kontorlu(kurpiyer_eli, oyuncu_eli)
            secim = "q"
        elif secim == "b":
            exit()
    tekrar_oyna()
    return

play()