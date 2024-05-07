# Overriding method adalah konsep di mana sebuah subclass dapat menimpa (override) metode yang sudah ada di superclass. 
# Dengan kata lain, subclass dapat menulis ulang atau mengganti implementasi dari metode yang sudah ada di superclass.

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
        print(f"Mobil: {self.merek} ({self.tahun}) - Warna: {self.warna}")

mobil1 = Mobil("Toyota", 2020, "Merah")
mobil1.info()  # output: Mobil: Toyota (2020) - Warna: Merah
