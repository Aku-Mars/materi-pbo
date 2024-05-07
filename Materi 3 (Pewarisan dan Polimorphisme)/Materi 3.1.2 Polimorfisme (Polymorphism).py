class Hewan:
    def bersuara(self):
        pass

class Kucing(Hewan):
    def bersuara(self):
        print("Meow!")
        
class Anjing(Hewan):
    def bersuara(self):
        print("Guk Guk!")

hewan1 = Kucing()
hewan2 = Anjing()

for hewan in [hewan1, hewan2]:
    hewan.bersuara()
