class cherepaha:
    x=0
    y=0
    s=0

    def __init__(self, x, y, s):
        self.x=x
        self.y=y
        self.s=s

    def go_up(self,s):
        self.y+=self.s
        return self.y

    def go_down(self, s):
        self.y-=self.s
        return self.y

    def go_left(self, s):
        self.x-=self.s
        return self.x

    def go_right(self, s):
        self.x+=self.s
        return self.x

    def evolve(self):
        self.s+=1
        return self.s

    def degrade(self):
        self.s-=1
        return self.s

    def count_moves(self, x2, y2):
        return self.x-x2, self.y-y2

r=cherepaha(28, 15, 3)
print(r.count_moves(3,3 ))

