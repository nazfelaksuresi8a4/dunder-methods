class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getattr__(self,attr):      #Sinif.degisken cagrisinda calisan dunderdır
        return attr

    def __setattr__(self, variable, value):    #Sinif.degisken = atanan cagrisinde calisan dunderdır
        if variable == 'age' and int(value) <= 0:
            raise ValueError('Yaş 0 veya negatif olamaz!')
        
        super().__setattr__(variable,value)      #super() burada object metodlara erişmemizi sağlar pratikte alt sınıfın üst sınıfa erişmesini sağlar ancak başka bir alanda kullanılmıtır.

    def __delattr__(self,attr):          #del Sinif.degisken cagrisinde calisan dunderdır
        if attr == 'name':
            return PermissionError('İsim değişkeni silinemez!')

        super().__delattr__(attr)

ali = Person('Ali',35)


ali.name = 'mustafa'
ali.name
ali.age = 10
ali.age = 4
del ali.age 
