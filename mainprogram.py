# Sistem Pengelolaan Data Mahasiswa Sistem Informasi 2024
"""
Materi yang digunakan:
1. Variabel
2. String manipulation
3. Conditional Statement
4. Function
5. Type data (list, dict)
6. Looping
"""

# Variabel utama untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi validasi dan manipulasi string untuk nama
def validasi_nama():
    """
    Fungsi untuk validasi nama mahasiswa.
    Input:
        - Nama mahasiswa (string)
    Validasi:
        - Tidak boleh kosong
        - Hanya boleh berisi huruf dan spasi
    Output:
        - Nama mahasiswa dengan format huruf kapital di awal setiap kata.
    """
    while True:
        nama = input("Masukkan Nama Mahasiswa: ").strip()
        if nama and all(c.isalpha() or c.isspace() for c in nama):
            return " ".join(word.capitalize() for word in nama.split())
        print("Nama harus berupa huruf dan spasi, tidak boleh kosong!")

# Fungsi validasi untuk NIM
def validasi_nim():
    """
    Fungsi untuk validasi NIM mahasiswa.
    Input:
        - NIM mahasiswa (integer)
    Validasi:
        - NIM harus berupa angka
        - Harus dalam rentang 1-94
    Output:
        - NIM mahasiswa yang valid (integer).
    """
    while True:
        try:
            nim = int(input("Masukkan NIM Mahasiswa (1-94): "))
            if 1 <= nim <= 94:
                return nim
        except ValueError:
            pass
        print("NIM harus berupa angka dalam rentang 1-94!")

# Fungsi untuk menentukan kelas berdasarkan NIM
def tentukan_kelas(nim):
    """
    Fungsi untuk menentukan kelas mahasiswa berdasarkan NIM.
    Input:
        - NIM mahasiswa (integer)
    Proses:
        - Jika NIM <= 55, kelas = "A"
        - Jika NIM > 55, kelas = "B"
    Output:
        - Kelas mahasiswa (string).
    """
    return "A" if nim <= 55 else "B"

# Fungsi untuk menambahkan data mahasiswa
def tambah_mahasiswa():
    """
    Fungsi untuk menambahkan data mahasiswa ke dalam daftar.
    Proses:
        - Memvalidasi nama menggunakan `validasi_nama`
        - Memvalidasi NIM menggunakan `validasi_nim`
        - Menentukan kelas menggunakan `tentukan_kelas`
        - Menambahkan data mahasiswa (nama, NIM, kelas) ke daftar `data_mahasiswa`
    Output:
        - Data mahasiswa ditambahkan ke daftar.
    """
    print("\n=== Tambah Data Mahasiswa ===")
    nama = validasi_nama()
    nim = validasi_nim()
    kelas = tentukan_kelas(nim)
    data_mahasiswa.append({"nim": nim, "nama": nama, "kelas": kelas})
    print(f"Mahasiswa {nama} dengan NIM {nim} berhasil ditambahkan ke Kelas {kelas}!\n")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_mahasiswa():
    """
    Fungsi untuk menampilkan seluruh data mahasiswa.
    Proses:
        - Mengurutkan data mahasiswa berdasarkan NIM
        - Menampilkan data dalam format tabel (No, Nama, NIM, Kelas)
    Output:
        - Tabel data mahasiswa, atau pesan jika daftar kosong.
    """
    print("\n=== Data Mahasiswa Sistem Informasi 2024 ===")
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    data_mahasiswa.sort(key=lambda m: m['nim'])
    print(f"{'No':<4} {'Nama':<25} {'NIM':<10} {'Kelas':<5}")
    print("=" * 45)
    for i, m in enumerate(data_mahasiswa, start=1):
        print(f"{i:<4} {m['nama']:<25} {m['nim']:<10} {m['kelas']:<5}")
    print()

# Fungsi untuk menampilkan data berdasarkan kelas
def tampilkan_per_kelas():
    """
    Fungsi untuk menampilkan data mahasiswa berdasarkan kelas.
    Proses:
        - Meminta pengguna memilih kelas (A atau B)
        - Memfilter data mahasiswa berdasarkan kelas yang dipilih
        - Mengurutkan data berdasarkan NIM
        - Menampilkan data dalam format tabel
    Output:
        - Tabel data mahasiswa untuk kelas tertentu, atau pesan jika kelas kosong.
    """
    kelas = input("\nPilih kelas (A/B): ").strip().upper()
    if kelas not in ["A", "B"]:
        print("Pilihan tidak valid!")
        return
    data_kelas = [m for m in data_mahasiswa if m['kelas'] == kelas]
    if not data_kelas:
        print(f"Belum ada data mahasiswa di Kelas {kelas}.")
        return
    data_kelas.sort(key=lambda m: m['nim'])
    print(f"\n=== Data Mahasiswa Kelas {kelas} ===")
    print(f"{'No':<4} {'Nama':<25} {'NIM':<10}")
    print("=" * 40)
    for i, m in enumerate(data_kelas, start=1):
        print(f"{i:<4} {m['nama']:<25} {m['nim']:<10}")
    print()

# Menu utama
def menu_utama():
    """
    Fungsi untuk menampilkan dan mengelola menu utama program.
    Proses:
        - Menampilkan pilihan menu (tambah data, tampilkan semua data, tampilkan per kelas, keluar)
        - Memproses input pengguna dan memanggil fungsi yang sesuai
        - Memberikan opsi untuk keluar dari program
    """
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Tampilkan Mahasiswa per Kelas")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            tampilkan_per_kelas()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi!")

# Menjalankan program
menu_utama()
