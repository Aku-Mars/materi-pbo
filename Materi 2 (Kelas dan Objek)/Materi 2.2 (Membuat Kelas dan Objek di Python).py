# definisi kelas
class Mahasiswa:
    # atribut
    nama = ""
    nim = ""
    jurusan = ""

    # metode
    def mendaftar(self):
        print("Saya mendaftar mata kuliah.")

    def mengambil_mata_kuliah(self, mata_kuliah):
        print("Saya mengambil mata kuliah " + mata_kuliah)
    
    def melihat_nilai(self):
        print("Saya melihat nilai mata kuliah.")

# membuat objek
mahasiswa1 = Mahasiswa()
mahasiswa1.nama = "Ari"
mahasiswa1.nim = "12345"
mahasiswa1.jurusan = "Informatika"

# memanggil metode objek
mahasiswa1.mendaftar()
mahasiswa1.mengambil_mata_kuliah("Pemrograman Berorientasi Objek")
mahasiswa1.melihat_nilai()

# membuat objek lainnya
mahasiswa2 = Mahasiswa()
mahasiswa2.nama = "Budi"
mahasiswa2.nim = "67890"
mahasiswa2.jurusan = "Teknik Sipil"

# memanggil metode objek lainnya
mahasiswa2.mendaftar()
mahasiswa2.mengambil_mata_kuliah("Konstruksi Bangunan")
mahasiswa2.melihat_nilai()
