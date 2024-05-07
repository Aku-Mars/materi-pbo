class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
    
    def info(self):
        print(f"Kendaraan: {self.merk} ({self.tahun})")
        
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, warna):
        super().__init__(merk, tahun)
        self.warna = warna
        
    def info(self):
        super().info()
        print(f"Warna: {self.warna}")
