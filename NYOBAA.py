import numpy as np

def func(x, y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2

class SwarmMethod:
    def __init__(self, x, y, v, c, r, w):
        self.x = x
        self.y = y
        self.vX = []
        self.vY = []
        self.c = c
        self.r = r
        self.w = w
        self.f = []
        self.gBestX = None
        self.gBestY = None
        self.pBestY = []
        self.pBestX = []
        self.oldX = []
        self.oldY = []

        for i in range(0, len(x)):
            self.vX.append(v)
            self.vY.append(v)
            self.f.append(None)
            self.pBestY.append(None)
            self.pBestX.append(None)
            self.oldX.append(None)
            self.oldY.append(None)

    
    def swarm(self, n):
        def particle(x, y, vX, vY):
            for i in range(len(x)):
                self.x[i] = x[i]
                self.y[i] = y[i]
            for i in range(len(vX)):
                self.vX[i] = vX[i]
                self.vY[i] = vY[i]

        def mencariNilaiFungsi():
            for i in range(len(self.x)):
                self.f[i] = func(self.x[i], self.y[i])

        def gBest():
            self.gBestX = self.x[self.f.index(min(self.f))]
            self.gBestY = self.y[self.f.index(min(self.f))]

        def pBest():
            if(self.pBestX[0] == None):
                for i in range(len(self.x)):
                    self.pBestX[i] = self.x[i]
                    self.pBestY[i] = self.y[i]
            else:
                for i in range(len(self.x)):
                    if(func(self.oldX[i], self.oldY[i]) >= self.f[i]):
                        self.pBestX[i] = self.x[i]
                        self.pBestY[i] = self.y[i]
                    else:
                        self.pBestX[i] = self.oldX[i]
                        self.pBestY[i] = self.oldY[i]

        def updateV():
            for i in range(len(self.vX)):
                self.vX[i] = self.w * self.vX[i] + self.c[0] * self.r[0] * (self.pBestX[i] - self.x[i]) + self.c[1] * self.r[1] * (self.gBestX - self.x[i])
                self.vY[i] = self.w * self.vY[i] + self.c[0] * self.r[0] * (self.pBestY[i] - self.y[i]) + self.c[1] * self.r[1] * (self.gBestY - self.y[i])

        def updateX():
            for i in range(len(self.oldX)):
                self.oldX[i] = self.x[i]
                self.oldY[i] = self.y[i]

            for j in range(len(self.x)):
                self.x[j] = self.x[j] + self.vX[j]
                self.y[j] = self.y[j] + self.vY[j]
        
        print("PSO Algoritm:")
        for i in range(0, n):
            particle(self.x, self.y, self.vX, self.vY)
            mencariNilaiFungsi()
            gBest()
            pBest()
            updateV()
            updateX()
            print(f"===Iterasi-{i + 1}=======================================================")
            print("Sebelum:", end=" ")
            for i in range(0, len(self.x)):
                if(i == len(self.x) - 1):
                    print(f"x{i} = {self.oldX[i], self.oldY[i]}", end="\n")
                else:
                    print(f"x{i} = {self.oldX[i], self.oldY[i]}", end=", ")
            print(f"gBest = {self.gBestX, self.gBestY}")
            print(f"pBest = {self.pBestX, self.gBestY}")
            print(f"v = {self.vX, self.vY}")
            print("Sesudah:", end=" ")
            for i in range(0, len(self.x)):
                if(i == len(self.x) - 1):
                    print(f"x{i} = {self.x[i], self.y[i]}", end="\n")
                else:
                    print(f"x{i} = {self.x[i], self.y[i]}", end=", ")
            print("Nilai Fungsi:", end=" ")
            for i in range(0, len(self.x)):
                if(i == len(self.x) - 1):
                    print(f"f(x{i}) = {self.f[i]}", end="\n")
                else:
                    print(f"f(x{i}) = {self.f[i]}", end=", ")

x = np.random.randint(-10, 10, size=10)
y = np.random.randint(-10, 10, size=10)
r = np.random.rand(2)
print(f"Nilai Random x: {x}")
print(f"Nilai Random y: {y}")
print(f"Nilai Random r: {r}")
sm = SwarmMethod(x, y, 0, [1, 0.5], r, 1)
sm.swarm(3)