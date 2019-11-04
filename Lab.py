import random as rnd
# Soru 1:
# Bir liste oluşturun ve rastgele bir elemanı ekranda gösteriniz.
# liste = [1,2,3,4,5]
# sayi = random.randint(0,5)
# print('Rastgele sayi : ', sayi)

#--------------------------------------------------------------------------------------------------------------------

# Soru 2:
# Sırasıyla kullanıcıdan 5 adet kayıt alın. Bu kayıtlar bir listede tutulsun ve 5 elemaanda eklendikten sonra hepsi sırasıyla ekranda gösterilsin.
# liste = []
# for x in range(5):
#     deger = input('Sayi giriniz : ')
#     liste.append(deger)
# print(liste)

#--------------------------------------------------------------------------------------------------------------------

# Soru 3:
# Kullanıcıdan girdiği metinsel değer bir palindrom mudur kontrolü yapılsın.

#--------------------------------------------------------------------------------------------------------------------

# Soru 4:
# Sayısal ve rastgele değerlerden bir dizi oluşturun (10 elemanlı). Bu dizideki max ve min değerleri ekranda gösteriniz.
# sayac = 0
# sayilar = []
# while sayac < 10:
#     sayilar.append(random.randint(0,100))
#     sayac += 1
#
# sayac = 0
# max = sayilar[0]
# min = sayilar[0]
# while sayac < 10:
#     if max < sayilar[sayac]:
#         max = sayilar[sayac]
#     if min > sayilar[sayac]:
#         min = sayilar[sayac]
#     sayac += 1
#
# print('Sayılar dizisi : ', sayilar)
# print('Max değer : ', max)
# print('Min değer : ', min)

#--------------------------------------------------------------------------------------------------------------------

#-----SİPARİŞ UYGULAMASI-----
# Önden hazılanmış ana yemek yan yemek ve içecekler üzerinden bir kullanıcı sırasıyla birer item seçecek ve sonucunda tutarı kişiye gösterilecek

# tutar = 0
# i =0
# menu = [{'Menü Adı :': 'Menü 1','Yiyecek :': 'Hamburger'  , 'İçecek': 'Cola Veya Ayran', 'Ekstra : ': 'Patates', 'Fiyat : ': '20 TL'},
#         {'Menü Adı :': 'Menü 2','Yiyecek :': 'Zurna'      , 'İçecek': 'Cola Veya Ayran', 'Ekstra : ': 'Patates', 'Fiyat : ': '15 TL'},
#         {'Menü Adı :': 'Menü 3','Yiyecek :': 'Tavuk Döner', 'İçecek': 'Cola Veya Ayran', 'Ekstra : ': 'Patates', 'Fiyat : ': '13 TL'},
#         {'Menü Adı :': 'Menü 4','Yiyecek :': 'Et Döner'   , 'İçecek': 'Cola Veya Ayran', 'Ekstra : ': 'Patates', 'Fiyat : ': '16 TL'},
#         {'Menü Adı :': 'Menü 5','Yiyecek :': 'Çiğ Köfte'  , 'İçecek': 'Cola Veya Ayran', 'Ekstra : ': 'Patates', 'Fiyat : ': '10 TL'},
#         {'Menü Adı :': 'Menü 6','Yiyecek :': 'Pizza'      , 'İçecek': 'Ayran'          , 'Ekstra : ': 'Patates', 'Fiyat : ': '25 TL'}]
#
# yemekler = [{'Yiyecek :': 'Hamburger'  , 'Fiyat :': '10 TL'},
#             {'Yiyecek :': 'Zurna'      , 'Fiyat :': '7 TL'},
#             {'Yiyecek :': 'Tavuk Döner', 'Fiyat :': '7 TL'},
#             {'Yiyecek :': 'Et Döner'   , 'Fiyat :': '8 TL'},
#             {'Yiyecek :': 'Çiğ Köfte'  , 'Fiyat :': '5 TL'},
#             {'Yiyecek :': 'Pizza'      , 'Fiyat :': '15 TL'}]
#
# icecek = [{'İçecek : ': 'Cola'   , 'Fiyat :': '4 TL'},
#           {'İçecek : ': 'İce Tea', 'Fiyat :': '4 TL'},
#           {'İçecek : ': 'Ayran'  , 'Fiyat :': '2 TL'},
#           {'İçecek : ': 'Soda'   , 'Fiyat :': '2 TL'},
#           {'İçecek : ': 'Gazoz'  , 'Fiyat :': '4 TL'},
#           {'İçecek : ': 'Su'     , 'Fiyat :': '2 TL'}]
#
# print('--------HOŞGELDİNİZ...---------')
# print('----------MENÜLER--------------')
# musteri_sayisi = int(input('Kaç Kişi Olduğunu Giriniz : '))
# sayac = 0
# while i < musteri_sayisi :
#     while sayac < len(menu):
#         print(menu[sayac]["Menü Adı :"], ':', menu[sayac]['Yiyecek :'], '-', menu[sayac]['İçecek'], '-', menu[sayac]['Ekstra : '], '-', menu[sayac]['Fiyat : '])
#         sayac += 1
#     print('----------YEMEKLER---------')
#     sayac = 0
#     while sayac < len(yemekler):
#         print(yemekler[sayac]['Yiyecek :'], '-', yemekler[sayac]['Fiyat :'])
#         sayac += 1
#     print('---------İÇECEKLER---------')
#     sayac = 0
#     while sayac < len(icecek):
#         print(icecek[sayac]['İçecek : '], '-', icecek[sayac]['Fiyat :'])
#         sayac += 1
#
#     istenilen_yemek = input('Lütfen Yemek İstediğiniz Menü, Yemek Veya İçmek İstediğiniz İçeceği Seçiniz : ')
#     if istenilen_yemek == 'Menü 1':
#         print(menu[0]["Menü Adı :"], ':', menu[0]['Yiyecek :'], '-', menu[0]['İçecek'], '-', menu[0]['Ekstra : '], '-', menu[0]['Fiyat : '])
#     elif istenilen_yemek == 'Menü 2':
#         print(menu[1]["Menü Adı :"], ':', menu[1]['Yiyecek :'], '-', menu[1]['İçecek'], '-', menu[1]['Ekstra : '], '-', menu[1]['Fiyat : '])
#     elif istenilen_yemek == 'Menü 3':
#         print(menu[2]["Menü Adı :"], ':', menu[2]['Yiyecek :'], '-', menu[2]['İçecek'], '-', menu[2]['Ekstra : '], '-', menu[2]['Fiyat : '])
#     elif istenilen_yemek == 'Menü 4':
#         print(menu[3]["Menü Adı :"], ':', menu[3]['Yiyecek :'], '-', menu[3]['İçecek'], '-', menu[3]['Ekstra : '], '-', menu[3]['Fiyat : '])
#     elif istenilen_yemek == 'Menü 5':
#         print(menu[4]["Menü Adı :"], ':', menu[4]['Yiyecek :'], '-', menu[4]['İçecek'], '-', menu[4]['Ekstra : '], '-', menu[4]['Fiyat : '])
#     elif istenilen_yemek == 'Menü 6':
#         print(menu[5]["Menü Adı :"], ':', menu[5]['Yiyecek :'], '-', menu[5]['İçecek'], '-', menu[5]['Ekstra : '], '-', menu[5]['Fiyat : '])
#     elif istenilen_yemek == 'Hamburger':
#         print('Fiyat :', yemekler[0]['Fiyat :'])
#     elif istenilen_yemek == 'Zurna':
#         print('Fiyat :', yemekler[1]['Fiyat :'])
#     elif istenilen_yemek == 'Tavuk Döner':
#         print('Fiyat :', yemekler[2]['Fiyat :'])
#     elif istenilen_yemek == 'Et Döner':
#         print('Fiyat :', yemekler[3]['Fiyat :'])
#     elif istenilen_yemek == 'Çiğ Köfte':
#         print('Fiyat :', yemekler[4]['Fiyat :'])
#     elif istenilen_yemek == 'Pizza':
#         print('Fiyat :', yemekler[5]['Fiyat :'])
#     elif istenilen_yemek == 'Cola':
#         print('Fiyat :', icecek[0]['Fiyat :'])
#     elif istenilen_yemek == 'İce Tea':
#         print('Fiyat :', icecek[1]['Fiyat :'])
#     elif istenilen_yemek == 'Ayran':
#         print('Fiyat :', icecek[2]['Fiyat :'])
#     elif istenilen_yemek == 'Soda':
#         print('Fiyat :', icecek[3]['Fiyat :'])
#     elif istenilen_yemek == 'Gazoz':
#         print('Fiyat :', icecek[4]['Fiyat :'])
#     elif istenilen_yemek == 'Su':
#         print('Fiyat :', icecek[5]['Fiyat :'])
#     else:
#         print('Hatalı Giriş Yapılmıştır!!!')
#     i += 1

#------------------------------------------------------------------------------------------------------------------

#------RENT A CAR---------
# araclar = [{'Marka': 'Volvo'   , 'Model': 'V40'    , 'Yıl': '2015', 'Yakıt': 'Benzin'      ,'Vites': 'Otomatik', 'Fiyat(Gün Başı)': '200 TL', 'Tarih': '1.08.2019/5.08.2019'},
#            {'Marka': 'Mercedes', 'Model': 'A180'   , 'Yıl': '2017', 'Yakıt': 'Benzin'      ,'Vites': 'Otomatik','Fiyat(Gün Başı)': '175 TL', 'Tarih': '5.08.2019/10.08.2019'},
#            {'Marka': 'Ford'    , 'Model': 'Focus'  , 'Yıl': '2010', 'Yakıt': 'Benzin / Gaz','Vites': 'Otomatik','Fiyat(Gün Başı)': '75 TL', 'Tarih': '10.08.2019/15.08.2019'},
#            {'Marka': 'Toyota'  , 'Model': 'Corolla', 'Yıl': '2019', 'Yakıt': 'Hybrid'      ,'Vites': 'Otomatik','Fiyat(Gün Başı)': '100 TL', 'Tarih': '15.08.2019/20.08.2019'},
#            {'Marka': 'Bmw'     , 'Model': '520D'   , 'Yıl': '2019', 'Yakıt': 'Dizel'       ,'Vites': 'Otomatik','Fiyat(Gün Başı)': '350 TL', 'Tarih': '20.08.2019/25.08.2019'},
#            #{'Marka': 'Seat'    , 'Model': 'Leon'   , 'Yıl': '2015', 'Yakıt': 'Dizel'       ,'Vites': 'Otomatik','Fiyat(Gün Başı)': '125 TL', 'Tarih': '4.08.2019/8.08.2019'},
#            {'Marka': 'Honda'   , 'Model': 'Civic'  , 'Yıl': '2018', 'Yakıt': 'Benzin / Gaz','Vites': 'Otomatik','Fiyat(Gün Başı)': '200 TL', 'Tarih': '25.08.2019/31.08.2019'}]
# sayac = 0
# print('---------HOŞGELDİNİZ---------')
# istenilen_tarih = int(input('Lütfen Kiralamk İstediğiniz Tarihin Gününü Giriniz(Ağustos Ayı Araçları) :'))
# sahip_olunan_para = int(input('Lütfen Sahip Olduğunuz Bütçeyi Giriniz(TL) :'))
# print('MODELLERİMİZ:')
# while sayac < len(araclar):
#     print(araclar[sayac]['Marka'], '-', araclar[sayac]['Model'], '-', araclar[sayac]['Yıl'], '-', araclar[sayac]['Yakıt'], '-', araclar[sayac]['Vites'], '-', araclar[sayac]['Fiyat(Gün Başı)'], '-', araclar[sayac]['Tarih'])
#     sayac += 1
#
# print('-----------------------------')
# isteniilen_araç = input('Lütfen Kiralamk İstediğiniz Aracın Markasını Giriniz : ')
#
# if isteniilen_araç == 'Volvo':
#     if istenilen_tarih < 5:
#         if sahip_olunan_para > 200:
#             print('Aracınız Başarıyla Kiralanmıştır...')
#             print('Lütfen Dikkatli Ve Kurallara Uyarak Kullanınız...')
#         else:
#             print('Girmiş Olduğunuz Tutar Bu Araç İçin Yeterli Değildir :(')
#     else:
#         print('İstediğiniz Tarihlerde Bu Aracı Kiralayamazsınız :(')
#
# elif isteniilen_araç == 'Mercedes':
#     if (istenilen_tarih > 5) and (istenilen_tarih < 10):
#         if sahip_olunan_para > int('175'):
#             print('Aracınız Başarıyla Kiralanmıştır...')
#             print('Lütfen Dikkatli Ve Kurallara Uyarak Kullanınız...')
#         else:
#             print('Girmiş Olduğunuz Tutar Bu Araç İçin Yeterli Değildir :(')
#     else:
#         print('İstediğiniz Tarihlerde Bu Aracı Kiralayamazsınız :(')
#
# elif isteniilen_araç == 'Ford':
#     if (istenilen_tarih > 10) and (istenilen_tarih < 15):
#         if sahip_olunan_para > int('75'):
#             print('Aracınız Başarıyla Kiralanmıştır...')
#             print('Lütfen Dikkatli Ve Kurallara Uyarak Kullanınız...')
#         else:
#             print('Girmiş Olduğunuz Tutar Bu Araç İçin Yeterli Değildir :(')
#     else:
#         print('İstediğiniz Tarihlerde Bu Aracı Kiralayamazsınız :(')
#
# elif isteniilen_araç == 'Toyota':
#     if (istenilen_tarih > 15) and (istenilen_tarih < 20):
#         if sahip_olunan_para > int('100'):
#             print('Aracınız Başarıyla Kiralanmıştır...')
#             print('Lütfen Dikkatli Ve Kurallara Uyarak Kullanınız...')
#         else:
#             print('Girmiş Olduğunuz Tutar Bu Araç İçin Yeterli Değildir :(')
#     else:
#         print('İstediğiniz Tarihlerde Bu Aracı Kiralayamazsınız :(')
#
# elif isteniilen_araç == 'Bmw':
#     if (istenilen_tarih > 20) and (istenilen_tarih < 25):
#         if sahip_olunan_para > int('350'):
#             print('Aracınız Başarıyla Kiralanmıştır...')
#             print('Lütfen Dikkatli Ve Kurallara Uyarak Kullanınız...')
#         else:
#             print('Girmiş Olduğunuz Tutar Bu Araç İçin Yeterli Değildir :(')
#     else:
#         print('İstediğiniz Tarihlerde Bu Aracı Kiralayamazsınız :(')
#
# elif isteniilen_araç == 'Honda':
#     if (istenilen_tarih > 25) and (istenilen_tarih < 31):
#         if sahip_olunan_para > int('200'):
#             print('Aracınız Başarıyla Kiralanmıştır...')
#             print('Lütfen Dikkatli Ve Kurallara Uyarak Kullanınız...')
#         else:
#             print('Girmiş Olduğunuz Tutar Bu Araç İçin Yeterli Değildir :(')
#     else:
#         print('İstediğiniz Tarihlerde Bu Aracı Kiralayamazsınız :(')

#--------------------------------------------------------------------------------------------------------------------

# Reverse kullanmadan diziyi ters çevirme

# isim = 'fatih'
# uzunluk = len(isim)-1
# while uzunluk >= 0:
#     print(isim[uzunluk])
#     uzunluk -= 1

#--------------------------------------------------------------------------------------------------------------------

# deger = input('Lütfen bir kelime giriniz : ')
# if deger == deger[::-1]:
#     print('Zaten palindrom ama birde karakter çıkarark bakalım :)')
#
# pos = 0
# sonuc = False
# while pos < len(deger):
#     kelime = deger[:pos] + deger[(pos +1):]
#
#     if kelime == kelime[::-1]:
#         print('{} pozisyonundaki {} karakterri çıkarılırsa palindrom olacaktır.'.format(pos,deger[pos]))
#         sonuc = True
#         break
#     else:
#         pos = pos + 1
# if sonuc == False:
#     print('Karakter çıkararak palindrom bulamadım !')

#--------------------------------------------------------------------------------------------------------------------

# dizi = []
# eleman_Sayisi = 0
# while eleman_Sayisi < 10:
#     sayi = rnd.randint(0,12)
#     if sayi not in dizi:
#         dizi.append(sayi)
#         eleman_Sayisi += 1
# print(dizi)

#--------------------------------------------------------------------------------------------------------------------

dizi = [500,45,36,15,89,90,2,47]
index = 0
for x in dizi:
    for y in dizi:
        if index + 1 < len(dizi):
            if dizi[index] < dizi[index + 1]:
                dizi[index], dizi[index + 1] = dizi[index +1], dizi[index]
            index = index + 1
    index = 0
print(dizi)

# ÖDEV: palindorm sorusuna ek olarak eğer bir karakter palidromu bozuyorsa, '... karakteri çıkarıldığında palindrom olacaktır' şeklinde mesaj ekrana getirilsin.
# Örnek: abacaa : b karakteri çıkarılırsa palindrom olacaktır

# Sort metodu kullanmadan diziyi sıralayınız.

# Reverse metodu kullanmadan diziyi tersine çeviriniz.

# 10 elemanlı 0-12 aralığında tekrar etmeyen sayılardan oluşan bir dizi oluşturunuz (RANDOM).

# Sizin önden belirleyeceğiniz bir kelime ile kullanıcının gireceği kelimeyyi kıyaslayınız. Eğer girilen kelime, önden belirlenen kelimenin anagramıysa, ekranda gösteriniz.

# Rent A Car otomasyonu. Tasarım bizde. (fazladan araç ekleyip sonradan kullanılabilir kullanılamaz durumunu da ekleyebilirsin)
