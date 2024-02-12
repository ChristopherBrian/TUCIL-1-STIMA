# Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force
> Tugas Kecil 1 IF 2211 Strategi Algoritma Semester II Tahun 2023/2024

## Daftar Isi
* [Deskripsi Singkat](#deskripsi-singkat)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Cara Setup](#cara-setup)
* [Cara Penggunaan](#cara-penggunaan)
* [Kontak](#kontak)

## Deskripsi Singkat
Breach Protocol adalah sebuah minigame yang terdapat pada video game Cyberpunk 2077. . Komponen pada permainan ini antara lain adalah:
1. Token – terdiri dari dua karakter alfanumerik seperti E9, BD, dan 55.
2. Matriks – terdiri atas token-token yang akan dipilih untuk menyusun urutan kode.
3. Sekuens – sebuah rangkaian token (dua atau lebih) yang harus dicocokkan.
4. Buffer – jumlah maksimal token yang dapat disusun secara sekuensial.

Aturan permainan Breach Protocol antara lain:
1. Pemain bergerak dengan pola horizontal, vertikal, horizontal, vertikal (bergantian) hingga
semua sekuens berhasil dicocokkan atau buffer penuh.
2. Pemain memulai dengan memilih satu token pada posisi baris paling atas dari matriks.
3. Sekuens dicocokkan pada token-token yang berada di buffer.
4. Satu token pada buffer dapat digunakan pada lebih dari satu sekuens.
5. Setiap sekuens memiliki bobot hadiah atau reward yang variatif.
6. Sekuens memiliki panjang minimal berupa dua token.

Program diminta untuk mencari solusi buffer terbaik, yaitu komposisi buffer dengan skor tertinggi.

## Teknologi yang Digunakan
- Python 3.12.2
- random
- tkinter
- time

## Cara Setup
1. Clone repository ini ke local repository
2. Jalankan file main.py pada folder src dalam terminal atau menggunakan ekstensi seperti Code Runner pada Visual Studio Code.

## Cara Penggunaan
1. Pilih opsi input, baik melalui file .txt ataupun CLI
2. Untuk opsi pertama, pilih file .txt sebagai input. Untuk opsi kedua, masukkan input sesuai perintah dalam CLI.
3. Program akan langsung memberikan solusi setelah pemrosesan selesai, terdapat opsi untuk menyimpan hasil dalam file .txt.


## Kontak
Dibuat oleh:
[Christopher Brian](https://github.com/ChristopherBrian) - 13522106

Feel free to contact me!