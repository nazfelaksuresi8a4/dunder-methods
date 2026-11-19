class Counter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.curr_count = 0
   
    def __iter__(self):
        return self     #ilk çağrıds iter fonksiyomu bunu tetikler ve self return edilir 
        
    def __next__(self):
        if self.curr_count < self.max_count:  #next fonksiyomu tetikler ve her seferinde döngüsel olarak çağırılır 

            self.curr_count += 1
            return self.curr_count
        
        else:
            raise StopIteration
 
counter = Counter(10)

for _ in range(89):
    print(next(counter)) 