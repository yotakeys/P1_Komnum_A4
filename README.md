# BOLZANO METHOD WITH PYTHON

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


