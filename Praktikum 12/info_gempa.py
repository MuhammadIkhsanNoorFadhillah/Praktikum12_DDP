from Gempa import *
#Informasi Data
Banten = Gempa ("Banten",1.2)
Palu = Gempa ("Palu", 6.1)
Cianjur = Gempa ("Cianjur", 5.6) 
Jayapura = Gempa ("Jayapura", 3.3)
Garut = Gempa ("Garut", 4.0)

#Memanggil Informasi
print(Banten.Dampak())
print(Palu.Dampak())
print(Cianjur.Dampak())
print(Jayapura.Dampak()) 
print(Garut.Dampak())