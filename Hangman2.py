yapilan_tahminler = []
bulunacak_kelime = "bapython"
tahmin_sayisi = 10
kelime = ''

while tahmin_sayisi > 0:
    tahmin = input("Bir tahminde bulununuz")
    yapilan_tahminler.append(tahmin)
    if kelime == bulunacak_kelime: # Kelime bilme durumu
        print("Kazandınız!", bulunacak_kelime)
        break
    elif len(tahmin) > 1 and tahmin == bulunacak_kelime: # Direk tahminle kelimeyi bulma
        print("Kazandınız", bulunacak_kelime)
        break
    else:
        kelime=''
        for karakter in bulunacak_kelime:
            if karakter in yapilan_tahminler:
                kelime += karakter
            else:
                kelime += '_'
        print("Kelime", kelime)
        print("Tahminler", yapilan_tahminler)
        tahmin_sayisi -= 1
else: # Break ile çıkılmadıysa çalışır
    print("\nKaybettiniz")

