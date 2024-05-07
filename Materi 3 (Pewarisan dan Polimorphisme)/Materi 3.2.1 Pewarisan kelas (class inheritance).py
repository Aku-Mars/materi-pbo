class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        print(f"Kendaraan: {self.merek} ({self.tahun})")
        
class Mobil(Kendaraan):
    def __init__(self, merek, tahun, warna):
        super().__init__(merek, tahun)
        self.warna = warna
        
    def info(self):
        super().info()
        print(f"Warna: {self.warna}")

