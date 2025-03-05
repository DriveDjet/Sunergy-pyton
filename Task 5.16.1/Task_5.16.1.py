class cassa:
    nall=11384

    def top_up(self, n):
        self.n=n
        cassa.nall+=n
        return cassa.nall 

    def count_1000(self):
        print(cassa.nall//1000)

    def take_away(sels, n):
        if cassa.nall>=n:
            cassa.nall-=n
            print (cassa.nall)
        else:
            print('Error!!! Not enough money')

r=cassa()
print(r.top_up(16000))
