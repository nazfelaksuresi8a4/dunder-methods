class Ogrenci:
    def __init__(self,puan):
        self.puan = puan

    def __eq__(self, value):        #equal
        return value == self.puan

    def __gt__(self, value):        #greater
        return value > self.puan

    def __ge__(self,value):         #greater or equal
        return value >= self.puan

    def __lt__(self,value):         #lesser then
        return value < self.puan

    def __le__(self,value):         #lesser or equal
        return value <= self.puan

ogrenci_1 = Ogrenci(100)
ogrenci_2 = Ogrenci(60)

print(ogrenci_1>ogrenci_2)      #ogrenci_1.puan > ogrenci_2.puan
print(ogrenci_1<ogrenci_2)      #ogrenci_1.puan < ogrenci_2.puan
print(ogrenci_1==ogrenci_2)     #ogrenci_1.puan == ogrenci_2.puan
print(ogrenci_1>=ogrenci_2)     #ogrenci_1.puan >= ogrenci_2.puan
print(ogrenci_1<=ogrenci_2)     #ogrenci_1.puan >= ogrenci_2.puan
