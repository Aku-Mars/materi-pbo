class Car:
    # class attribute (Mendeklarasikan Value Dari Atribut)
    brand = "Toyota"

    def __init__(self, model, year):
        self.model = model
        self.year = year

    # class method (Fungsi Yang Digunakan Untuk Memasukan Value)
    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand

# create objects
car1 = Car("Corolla", 2022)
car2 = Car("Camry", 2021)

# access class attribute
print(car1.brand)  # output: Toyota
print(car2.brand)  # output: Toyota

# access and change class attribute
print(Car.brand)  # output: Toyota
Car.change_brand("Honda")
print(Car.brand)  # output: Honda
print(car1.brand)  # output: Honda
print(car2.brand)  # output: Honda

class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

mobil1 = Mobil('Toyota', 'Merah')
mobil2 = Mobil('Honda', 'Hitam')

print(mobil1.merek) # Output: Toyota
print(mobil2.warna) # Output: Hitam


# Contoh Class Atribute & Class Method
class Lingkaran:

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
    
    def keliling(self):
        return 2 * 3.14 * self.jari_jari

lingkaran1 = Lingkaran(7)
lingkaran2 = Lingkaran(14)

print(lingkaran1.luas()) # Output: 153.86
print(lingkaran2.keliling()) # Output: 87.92
