# Pizza Ordering Program

### Algoritma Pemrograman - Sistem Pemesanan Pizza

Ini adalah proyek pemrograman yang dibuat sebagai bagian dari tugas Algoritma dan Pemrograman. Proyek ini adalah program pemesanan pizza interaktif yang memungkinkan pengguna untuk memilih pizza, jenis crust, ukuran pizza, dan tambahan keju. Setelah semua pilihan dibuat, program akan menampilkan ringkasan pesanan dan total tagihan.

## Features
- **User Input**: Pengguna memasukkan nama mereka dan memilih pizza dari menu.
- **Multiple Choices**: Program menyediakan pilihan untuk berbagai jenis pizza, crust, dan ukuran.
- **Extra Cheese**: Tersedia opsi tambahan keju dengan biaya ekstra.
- **Order Summary**: Setelah semua pilihan diambil, program akan menampilkan ringkasan pesanan lengkap dengan total harga.

## Flowchart
Berikut adalah penjelasan alur kerja program yang digambarkan melalui flowchart:

1. **Mulai**: Program dimulai dengan menampilkan sambutan "Welcome to AENS Pizza".
2. **Input Nama**: Pengguna diminta memasukkan nama mereka.
3. **List Menu Pizza**: Pengguna disajikan daftar menu pizza.
4. **Pilih Pizza**: Pengguna memilih pizza berdasarkan nomor.
5. **Pilih Crust**: Pengguna memilih jenis crust yang diinginkan.
6. **Pilih Ukuran Pizza**: Pengguna memilih ukuran pizza.
7. **Tambahan Keju**: Pengguna dapat memilih tambahan keju.
8. **Ringkasan Pesanan**: Program menampilkan ringkasan pesanan yang berisi nama pengguna, pizza, crust, ukuran, dan tambahan keju (jika ada).
9. **Konfirmasi Pesanan**: Pengguna mengonfirmasi pesanan.
10. **Selesai**: Jika pesanan dikonfirmasi, program menampilkan pesan terima kasih dan mengakhiri proses.

## Source Code
Program ditulis dalam bahasa **Python** dan menggunakan struktur logika seperti `while loops` dan `if-else` statements untuk menangani input pengguna serta validasi data.

### Contoh Potongan Kode:
```python
print("-------------------- WELCOME TO AENS PIZZA --------------------\n")
name = input("Please enter your name: ")
print("""List Menu Pizza:
1. Frankfurter BBQ - Rp 85.000
2. Meat Monster - Rp 110.000
3. Super Supreme - Rp 100.000
...
""")
choice_pizza = input("Choose your pizza by number: ")
if choice_pizza == "1":
    total_bill += 85000
    pizza_name = "Frankfurter BBQ (Rp 85.000)"
