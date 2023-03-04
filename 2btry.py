from numpy import matrix

class PSO():
    def __init__(self,xy0,xy1,xy2,v0,c1,c2,r2,r1,w):
        self.xy0 = xy0
        self.xy1 = xy1
        self.xy2 = xy2
        self.v0 = v0
        self.c1 = c1
        self.c2 = c2
        self.r2 = r2
        self.r1 = r1
        self.w = w
        self.iterasi = 1

    def fungsi(self,xy):
        x = xy[0]
        y = xy[1]
        return(1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2

    def cariGBest(self):
        if (self.fungsi(self.xy0) < self.fungsi(self.xy1) and self.fungsi(self.xy2)):
            return self.xy0
        elif (self.fungsi(self.xy1) < self.fungsi(self.xy0) and self.fungsi(self.xy2)):
            return self.xy1
        else:
            return self.xy2

    def printIterasi(self):
        print(
            f"Iterasi ke-{self.iterasi}\n"
            f"x0y0 = {self.xy0}\n"
            f"x1y1 = {self.xy1}\n"
            f"x2y2 = {self.xy2}\n"
            f"nilai minimum = {self.fungsi(self.cariGBest())}\n")

    def optimasi(self,pBest0=None,pBest1=None,pBest2=None):
        self.printIterasi()
        gBest = self.cariGBest()

        if self.iterasi < 3:
            turunan_xy0 = self.fungsi(self.xy0)
            turunan_xy1 = self.fungsi(self.xy1)
            turunan_xy2 = self.fungsi(self.xy2)

            if (self.iterasi == 1):
                pBest0 = xy0
                pBest1 = xy1
                pBest2 = xy2
            else:
                if self.fungsi(pBest0) > turunan_xy0:
                    pBest0 = xy0
                if self.fungsi(pBest1) > turunan_xy1:
                    pBest1 = xy1
                if self.fungsi(pBest2) > turunan_xy2:
                    pBest2 = xy2

            V0 = [w * v0[0] + c1 * r1 * (pBest0[0] - xy0[0]) + c2 * r2 * (gBest[0] - xy0[0]), w * v0[1] + c1 * r1 * (pBest0[1] - xy0[1]) + c2 * r2 * (gBest[1] - xy0[1])]
            V1 = [w * v0[0] + c1 * r1 * (pBest1[0] - xy0[0]) + c2 * r2 * (gBest[0] - xy0[0]), w * v0[1] + c1 * r1 * (pBest1[1] - xy0[1]) + c2 * r2 * (gBest[1] - xy0[1])]
            V2 = [w * v0[0] + c1 * r1 * (pBest2[0] - xy0[0]) + c2 * r2 * (gBest[0] - xy0[0]), w * v0[1] + c1 * r1 * (pBest2[1] - xy0[1]) + c2 * r2 * (gBest[1] - xy0[1])]

            self.xy0 = [self.xy0[0] + V0[0], self.xy0[1] + V0[1]]
            self.xy1 = [self.xy1[0] + V1[0], self.xy1[1] + V1[1]]
            self.xy2 = [self.xy2[0] + V2[0], self.xy2[1] + V2[1]]

            self.iterasi += 1
            self.optimasi(pBest0,pBest1,pBest2)


if __name__ == "__main__":
    #Variabel dari soal
    xy0=[0,0]
    xy1=[-1,-1]
    xy2=[2,-1]
    v0=[0,0]
    c1=1
    c2=1/2
    r2=1
    r1=r2
    w=1
    # buat objek pso
    pso = PSO(xy0,xy1,xy2,v0,c1,c2,r2,r1,w)
    #manggil fungsi optimasi
    pso.optimasi()