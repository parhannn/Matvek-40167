# Dokumentasi Program

Program ini merupakan program yang dibuat untuk memenuhi tugas besar pada mata kulaih "Matriks dan Ruang Vektor" yang dibuat dengan bahasa pemrogramman python.

Program ini dapat mencari solusi dari beberapa persoalan, yaitu:
- SPL yang memiliki solusi unik, dan menampilkan solusinya
- SPL yang memiliki solusi tak terbatas, dan menampilkan solusinya dalam bentuk parameter
- SPL yang tidak memiliki solusi, dengan menampilkan tulisan "Tidak memiliki solusi."

## Persiapan

Program ini membutuhkan sebuah library bernama os. Pastikan module tersebut telah terinstal di komputer anda.

## Menjalankan Program

Untuk menjalankan program, pastikan lokasi anda berada pada directory "/program/". Setelah itu jalankan program dengan mengetikkan perintah ini.

```
main.py
```

## Menu Program

<img src="Main Menu.jpeg">

Setelah program dijalankan, program akan menampilkan sebuah menu utama. Menu-menu tersebut diantaranya:
1. Input Values from Keyboard
2. Input Values from Test Case 1
3. Input Values from Test Case 2
4. Exit

## MENU: Input Values from Keyboard

Saat user memilih menu ini, maka user diharuskan memasukan nilai x1, x2, x3, …,
dst secara manual. Pertama user akan memasukan banyak baris, lalu user akan
memasukkan banyak kolom. Kemudian nilai x1, x2, x3, …, xN akan dimasukan oleh
user, banyaknya nilai x adalah N = Baris x Kolom. Setelah user sudah memasukkan
seluruh nilai x, program akan mengolahnya menjadi matrix augmented dan
ditampilkan ke terminal. Lalu, program akan memproses matriks tersebut menjadi
bentuk matriks eselon baris tereduksi dengan fungsi eliminasi Gauss-Jordan yang telah
kami buat dan ditampilkan bentuk akhir matriksnya. Setelah itu, nilai pada baris dan
kolom yang sama akan membagi bilangan pada ujung baris tiap kolom lalu
ditampilkan solusinya.

## MENU: Input Values from Test Case 1

Saat user memilih menu ini, maka program akan menggunakan value atau nilai dari
file yang sudah diimpor yakni file TestCase1 dan TestCase2, Dengan mengakses nilai
dari Matrix (List matriks) dan ManyRow(Banyak baris) user tak perlu menginputkan
nilai secara manual. Setelah itu, program akan mengolah nilai dari list menjadi sebuah
matrix augmented dan ditampilkan, setelah itu diproses dengan eliminasi Gauss-Jordan
dan ditampilkan bentuk akhir matriksnya dan terakhir dicari solusinya. 

## MENU: Input Values from Test Case 2

Untuk TestCase2 sama saja prosesnya hanya beda value atau nilainya saja.


## MENU: Exit

Saat user memilih menu ini, tentu saja program akan melakukan “break” atau
berhenti.
