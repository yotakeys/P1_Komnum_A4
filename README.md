# BOLZANO METHOD WITH PYTHON

**Nama anggota:**
    1. M. Naufal Baihaqi    (5025211103)
    2. Keyisa Raihan        (5025211002)
    3. Tsaqif Deniar B.     (5025211151)
    4. Mavaldi Rizqy        (5025211086)
    5. Anas Azhar           (5025211043)
    6. Shaloom David T.     (5025211242)


## Penjelasan Metode Bolzano

Metode `bolzano` , `biseksi`, atau `bagi dua` merupakan salah satu metode yang digunakan untuk mencari nilai akar-akar dari suatu persamaan. `Inti` dari konsep akar-akar dalam suatu persamaan `f(x)` adalah ketika suatu nilai `x` dimasukkan kedalam persamaan dan menghasilkan `f(x) = 0`. Semakin kompleksnya suatu persamaan, akan semakin sulit menemukan nilai `x` tersebut.

Metode `bolzano` dapat digunakan untuk mencari nilai `x` tersebut bukan hanya saat persamaannya `sederhana` melainkan juga dapat digunakan saat persamaannya dianggap `kompleks`.

Untuk menentukan akar-akar dari persamaan `f(x)` menggunakan metode ini, diperlukan dua variabel, yaitu Xu dan Xl

> X Upper (Xu)  = Nilai x batas atas\
X Lower (Xl)    = Nilai x batas bawah

Dari kedua variabel tersebut, kita dapat menaksir nilai `x` dari persamaannya. `x taksiran` tersebut dinamakan `Xr`.

>`Xr` = (`Xu` + `Xl`) / `2`

Taksiran harus dilakukan berulang kali untuk menemukan nilai `Xr` yang menyebabkan `f(Xr) = 0` atau `f(Xr) mendekati 0` . 

Untuk melakukan taksiran selanjutnya, perlu mengubah batas atas `(Xu)` atau batas bawahnya `(Xl)` dengan ketentuan :

>jika `f(Xl) * f(Xr) > 0` , maka jadikan `Xu = Xr` dan `Xl` tetap\
>jika `f(Xl) * f(Xr) < 0` , maka jadikan `Xl = Xr` dan `Xu` tetap\
>jika `f(Xl) * f(Xr) = 0` , perulangan berhenti dan `akar = Xr`.

hitung kembali taksiran `(Xr)` menggunakan batas atas dan batas bawah terbaru sampai ditemukan kondisi `f(Xr) = 0` atau `f(Xr) mendekati 0` . 


## Implementasi Algoritma Metode Bolzano menjadi Sebuag Program Komputer


Pertama, panggil kelas Bolzano dengan menggunakan parameter seperti `koefList` untuk fungsi (fx), `intervalBawah` (xl) dan `intervalAtas` (xu) sebagai batas nilai x, `ketelitian` untuk jumlah angka di belakang koma, dan `maxiter` sebagai batas iterasi yang akan kita lakukan dimana jika iterasi melebihi batas tersebut maka iterasi akan dihentikan dan akar persamaan tidak bisa ditemukan.
```
BZ = Bolzano(
        koefList=[1, 10, -7, -196],
        intervalBawah=-6,
        intervalAtas=6,
        ketelitian=5,
        maxiter=2000
    )
```



Selanjutnya, yaitu memanggil fungsi `fXToString()` untuk menampilkan f(x), sehingga akan muncul tampilan seperti berikut:
```
print("Function :", end=" ")
BZ.fXToString()
```
![Komnum_P1_fungsi](https://user-images.githubusercontent.com/99221296/197315887-678cc6d9-760e-4867-a168-db2be7dcf763.jpg)

Selanjutnya, memanggil fungsi `findRoot()` untuk mencari apakah f(x) memiliki akar persamaan atau tidak. Jika ada, maka akan menampilkan akar persaamaan tersebut.
```
BZ.findRoot()
print("Root : ", end=" ")
print(BZ.root)
```
![Komnum_P1_root](https://user-images.githubusercontent.com/99221296/197315889-9c2e0770-28bc-44e9-bca2-98669496c7d4.jpg)

Setelah diketahui bahwa f(x) tersebut memiliki akar persamaan, langkah berikutnya yaitu menampilkan proses `Metode Bolzano` yang digunakan untuk mencari akar persamaan yang disajikan dalam bentuk tabel dan diperjelas dengan grafik. Sehingga dalam tampilan akan muncul sebagai berikut:
```
print("Tabel : ")
BZ.tabel()
BZ.grafik()
```
![Komnum_P1_tabel](https://user-images.githubusercontent.com/99221296/197315891-5e3f62bf-9bdf-40a0-93ff-21c8a19699d4.jpg)
![Komnum_P1_grafik](https://user-images.githubusercontent.com/99221296/197315893-c1319b95-b8d2-4d96-852d-d22c80221747.jpg)
