#Sistem Pengelolaan Data Mahasiswa Sistem Informasi 2024

data_mahasiswa = []

# Fungsi untuk menambahkan data mahasiswa
def tambah_mahasiswa():
    print("\n=== Tambah Data Mahasiswa ===")
    
    # Validasi input nama
    while True:
        nama = input("Masukkan Nama Mahasiswa: ").strip()
        if nama:  # Cek jika nama tidak kosong
            break
        print("Nama tidak boleh kosong. Silakan masukkan nama dengan benar.")
    
    # Validasi input NIM
    while True:
        try:
            nim = int(input("Masukkan NIM Mahasiswa (1-94): "))
            if 1 <= nim <= 94:
                break
            else:
                print("NIM harus dalam rentang 1-94.")
        except ValueError:
            print("NIM harus berupa angka. Silakan coba lagi.")
    
    # Tentukan kelas berdasarkan NIM
    if 1 <= nim <= 55:
        kelas = "A"
    elif 56 <= nim <= 94:
        kelas = "B"
    
    mahasiswa = {"nim": nim, "nama": nama, "kelas": kelas}
    data_mahasiswa.append(mahasiswa)
    print(f"Mahasiswa {nama} dengan NIM {nim} berhasil ditambahkan ke Kelas {kelas}!\n")

# Fungsi untuk mengurutkan data mahasiswa berdasarkan NIM
def urutkan_berdasarkan_nim(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j]['nim'] > data[j + 1]['nim']:
                data[j], data[j + 1] = data[j + 1], data[j]

# Fungsi untuk menampilkan semua data mahasiswa
def tampilkan_mahasiswa():
    print("\n=== Data Mahasiswa Sistem Informasi 2024 ===")
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        # Urutkan data mahasiswa berdasarkan NIM
        urutkan_berdasarkan_nim(data_mahasiswa)
        for i, mahasiswa in enumerate(data_mahasiswa, start=1):
            print(f"{i}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Kelas: {mahasiswa['kelas']}")
    print()

# Fungsi untuk menampilkan mahasiswa berdasarkan kelas
def tampilkan_per_kelas():
    print("\n=== Pilih Kelas ===")
    print("1. Kelas A")
    print("2. Kelas B")
    pilihan = input("Pilih kelas (1/2): ")

    if pilihan == "1":
        kelas = "A"
    elif pilihan == "2":
        kelas = "B"
    else:
        print("Pilihan tidak valid!")
        return

    print(f"\n=== Data Mahasiswa Kelas {kelas} ===")
    data_kelas = [m for m in data_mahasiswa if m['kelas'] == kelas]
    
    if len(data_kelas) == 0:
        print(f"Belum ada data mahasiswa di Kelas {kelas}.")
    else:
        # Urutkan data mahasiswa berdasarkan NIM
        urutkan_berdasarkan_nim(data_kelas)
        for i, mahasiswa in enumerate(data_kelas, start=1):
            print(f"{i}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}")
    print()

# Menu utama
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
        print("Pilihan tidak valid, silakan coba lagi.")
