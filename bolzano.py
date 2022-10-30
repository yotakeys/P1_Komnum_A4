import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Bolzano untuk persamaan polinomial


class Bolzano():

    # Variabel
    koefList = []
    _iterlist = []
    _xUpper = 0.0
    _xLower = 0.0
    _firstxUpper = 0.0
    _firstxLower = 0.0
    _xR = 0.0
    ketelitian = 0
    maxiter = 0
    root = 0.0
    df = pd.DataFrame()

    def countXR(self):
        self._xR = float((float(self._xUpper) + float(self._xLower))) / 2.0

    def countFX(self, x):
        l = len(self.koefList) - 1
        hasil = 0
        for pkt in range(l, -1, -1):
            hasil += self.koefList[l-pkt] * pow(x, pkt)

        return hasil

    def __init__(self, koefList=[1], intervalBawah=-1000, intervalAtas=1000, ketelitian=4, maxiter=2000):
        self.koefList = koefList
        self._xUpper = intervalAtas
        self._xLower = intervalBawah
        self._firstxUpper = intervalAtas
        self._firstxLower = intervalBawah
        self.ketelitian = ketelitian
        self.maxiter = maxiter
        self.countXR()

    def fXToString(self):
        l = len(self.koefList) - 1
        for i in range(l, -1, -1):
            if(self.koefList[l-i] > 0 and i != l):
                print("+", end="")

            if(self.koefList[l-i] == 0):
                continue
            elif(self.koefList[l-i] != 1 and self.koefList[l-i] != -1 and i != 0):
                print(self.koefList[l-i], end="")

            if(i == 1):
                if(self.koefList[l-i] < 0):
                    print("", end="")
                print("X", end="")
            elif(i > 1):
                print("X^", end="")
                print(i, end="")
            else:
                print(self.koefList[l-i], end="")
        print()

    def rounding(self):
        self._xUpper = round(self._xUpper, self.ketelitian)
        self._xLower = round(self._xLower, self.ketelitian)
        self._xR = round(self._xR, self.ketelitian)

    def findRoot(self):
        iter = 0
        while(1):
            iter += 1
            if(iter >= self.maxiter):
                print(
                    "No root for equation/No root in the interval/Lack of iteration")
                return

            self.rounding()
            fXUpper = round(self.countFX(self._xUpper), self.ketelitian-1)
            fXLower = round(self.countFX(self._xLower), self.ketelitian-1)
            fXR = round(self.countFX(self._xR), self.ketelitian-1)

            tempList = [self._xLower, self._xUpper,
                        self._xR, fXLower, fXUpper, fXR]

            self._iterlist.append(tempList)

            if((fXLower <= 1*pow(10, (self.ketelitian-1) * -1)) and
                    (fXLower >= 1*pow(10, (self.ketelitian-1) * -1)*-1)):
                self.root = self._xLower
                break
            elif((fXUpper <= 1*pow(10, (self.ketelitian-1) * -1)) and
                 (fXUpper >= 1*pow(10, (self.ketelitian-1) * -1)*-1)):
                self.root = self._xUpper
                break
            elif((fXR <= 1*pow(10, (self.ketelitian-1) * -1)) and
                 (fXR >= 1*pow(10, (self.ketelitian-1) * -1)*-1)):
                self.root = self._xR
                break
            if(fXLower * fXR < 0):
                self._xUpper = self._xR
            else:
                self._xLower = self._xR
            self.countXR()
        print("Root Found")

    def tabel(self):
        self.df = pd.DataFrame(data=self._iterlist, columns=[
            "Xl", "Xu", "Xr", "F(Xl)", "F(Xu)", "F(Xr)"])
        print(self.df)

    def grafik(self):
        x = np.linspace(self._firstxLower, self._firstxUpper)
        y = self.countFX(x)
        plt.hlines(y=0, xmin=self._firstxLower,
                   xmax=self._firstxUpper, color='black')
        plt.vlines(x=0, ymin=min(y),
                   ymax=max(y), color='black')
        plt.plot(x, y)
        lst_clr = ['r', 'orange', 'y', 'g', 'b', 'violet', 'purple', 'c']
        j = 0
        for i in self.df["Xr"]:
            plt.axvline(x=i, c=lst_clr[j])
            j += 1 if j < 7 else 0
        plt.title("Grafik Bolzano")
        plt.show()

# Memanggil kelas bolzano dengan parameter
if __name__ == "__main__":
    BZ = Bolzano(
        koefList=[1, 10, -7, -196],
        intervalBawah=-6,
        intervalAtas=6,
        ketelitian=5,
        maxiter=2000
    )
# Menampilkan fungsi f(x)
    print("Function :", end=" ")
    BZ.fXToString()
# Mengecek adanya akar persamaan f(x), jika ada akan ditampilkan
    BZ.findRoot()
    print("Root : ", end=" ")
    print(BZ.root)
    print("Tabel : ")
# Menampilkan proses metode bolzano dengan tabel dan juga grafik
    BZ.tabel()
    BZ.grafik()
