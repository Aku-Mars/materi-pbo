class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def __del__(self):
        print(f"{self.merek} {self.warna} dihapus")

mobil1 = Mobil("Toyota", "Merah")
del mobil1
