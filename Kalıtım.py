# Miras/Kalıtım sayesinde bir sınıftaki method ve özellikleri, başka bir sınıf altına gönderme şansına sahibiz..

# Parent Class => Miras/Kalıtım veren sınıf
# Child Class  => Miras/Kalıtım alan sınıf

# class muzik_aleti:
#     name =  ''
#     price = 0
#     brand = ''
#
#     def cal(self):
#         print('Müzik Aleti Sesi')
#
# Child Class
# class gitar(muzik_aleti):
#     pass
#
# g = gitar()
# g.name = 'F310'
# g.price = 1170
# g.brand = 'Yamaha'
#
# print(g.name)


# PARENT CLASS
# class muzik_aleti:
#     def __init__(self, name, price, brand):
#         self.name = name
#         self.price = price
#         self.brand = brand
#
#     def cal(self):
#         print('Müzik Aleti Sesi')


#Child Class
# class gitar(muzik_aleti):
#     pass

# g = gitar('F310', 1170, 'Yamaha')
# print(g.name)

# Eğer gitar sınıfının da sadece kendisine ait özellikleri olacak ve bir init yapısı kullanılacaksa, alttaki şekle çevirebiliriz.

# PARENT CLASS
class muzik_aleti:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def cal(self):
        print('Müzik Aleti Sesi')

#Child Class
class gitar(muzik_aleti):
    def __init__(self, name, price, brand, string_brand):
        muzik_aleti.__init__(self, name, price, brand)
        self.string_brand = string_brand

    def cal(self):
        print('Gitar Sesi')
# Bu yönteme override denir. Miras aldığınız fonksiyon içerisinde küçük düzenlemeler/değişiklikler yapacaksanız, miras alan sınıf aynı isimde açarak içeriği değitirmemiz yeterlidir


# Son gitar classında sadece gitarlarlara özel tel markası diye bir özellik ekledik. muzik_aleti sınıfında string_brand yokken gitar'da var olacaktır.
# Gitar nesnesi oluşturulduğunda ilk 3 özelliği hala muzik_aleti

gtr = gitar('F310', 1170, 'yamaha', 'd\'addario')
print(gtr.name, gtr.string_brand)
gtr.cal()

class keman(muzik_aleti):
    def __init__(self, name, price, brand, string_brand):
        muzik_aleti.__init__(self, name, price, brand)
        self.string_brand = string_brand

    def cal(self):
        print('Keman Sesi')

kmn = keman('AVLX1 4/4', 18439, 'Amanda', 'd\'addario')
kmn.cal()  # Override sayesinde kemanlardan keman sesi çıkarabiliriz :)

# Python da çoklu miras vardır
# Parent Class 1
class A:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def funcA(self):
        return 'Function From Class A'
# Parent Class 2
class B:
    def __init__(self,attr):
        self.attr = attr

    def funcB(self):
        return 'Function From Class B'
# Child Class
class AB(A,B):
    def __init__(self,attr1, attr2, attr, child_attr):
        A.__init__(self,attr1,attr2)
        B.__init__(self,attr)
        self.child_attr = child_attr

    def funcA(self):
        return 'Function-A is override by Child Class AB'

obj_a = A('attribute-1', 'attribute-2')
obj_b = B('attribute')
obj_ab = AB('attr-1','attr-2','attr','child_attr')

print('obj-a nesnesinin funcA', obj_a.funcA())
print('obj-ab nesnesinin funcA', obj_ab.funcA())
print('---------')
print('obj-b nesnesinin funcA', obj_b.funcB())
print('obj-ab nesnesinin funcA', obj_ab.funcB())