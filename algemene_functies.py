def mijn_functie_1():
   kolom_1 = 2 ** 2
   kolom_2 = 4 ** 2
   kolom_3 = 10 ** 2
   kolom_4 = 12 ** 2
   return kolom_1, kolom_2, kolom_3, kolom_4

def mijn_functie_2 (a,b):
   kolom_1 = a + b
   kolom_2 = a - b
   kolom_3 = a * b
   kolom_4 = a / b
   return kolom_1, kolom_2, kolom_3, kolom_4

print (mijn_functie_1())
print (mijn_functie_2(12,3))
print (mijn_functie_2(12,2))
print (mijn_functie_2(10,5))
print (mijn_functie_2(100,20))