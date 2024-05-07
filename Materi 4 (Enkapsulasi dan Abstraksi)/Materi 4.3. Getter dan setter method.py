# Getter dan setter method adalah method khusus dalam pemrograman berorientasi objek 
# yang digunakan untuk mengakses dan mengubah nilai variabel dalam suatu class.
class Mobil:
    def __init__(self, merek, tahun):
        self._merek = merek
        self._tahun = tahun
        
    def get_merek(self):
        return self._merek
    
    def set_merek(self, merek):
        self._merek = merek
        
    def get_tahun(self):
        return self._tahun
    
    def set_tahun(self, tahun):
        self._tahun = tahun
        
mobil1 = Mobil("Toyota", 2020)
print(mobil1.get_merek())  # output: Toyota
mobil1.set_merek("Honda")
print(mobil1.get_merek())  # output: Honda
print(mobil1.get_tahun())  # output: 2020
mobil1.set_tahun(2022)
print(mobil1.get_tahun())  # output: 2022
