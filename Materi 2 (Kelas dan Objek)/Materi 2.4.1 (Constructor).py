class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

p = Manusia("John Doe", 25)
p.info() # Output: Nama: John Doe, Umur: 25
