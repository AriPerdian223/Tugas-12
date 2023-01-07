#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nama : Ari Perdian
#NIM : 20220040072

import bangunRuang
import bangunDatar

print ("="*30)
print ("BANGUN RUANG")
print ("="*30)

#Kubus
volume = bangunRuang.vol_kubus(5)
print(f"Volume bangun ruang Kubus : {volume}")

#Balok
volume2 = bangunRuang.vol_balok(10, 5, 7)
print(f"Volume bangun ruang Balok : {volume2}")

#Prisma Segitiga
volume3 = bangunRuang.prisma_segitiga(5, 2, 10)
print (f"Volume bangun ruang Prisma Segitia : {volume3}")

#Limas Segiempat
volume4 = bangunRuang.limas_segiempat(6, 5)
print(f"Volume bangun ruang limas segiempat : {volume4}")

#Tabung
volume5 = bangunRuang.limas_segiempat(14, 5)
print(f"Volume bangun ruang tabung : {volume5}")

#Kerucut
volume6 = bangunRuang.limas_segiempat(21, 10)
print(f"Volume bangun ruang Kerucut : {volume6}")

print ("="*30)
print ("BANGUN DATAR")
print ("="*30)

#Persegi
luas = bangunDatar.luas_persegi(5)
print(f"Luas bangun datar persegi : {luas}")

#Persegi panjang
luas2 = bangunDatar.persegi_panjang(5, 10)
print(f"Luas bangun datar persegi panjang : {luas2}")

#Jajar Genjang
luas3 = bangunDatar.jajar_genjang(10, 15)
print(f"Luas bangun datar jajar genjang : {luas3}")

#Segitiga
luas4 = bangunDatar.luas_segitiga(8, 12)
print(f"Luas bangun datar segitiga : {luas4}")

#Belah Ketupat
luas5 = bangunDatar.belah_ketupat(10, 5)
print(f"Luas bangun datar belah ketupat : {luas5}")

#lingkaran
luas6 = bangunDatar.ling_karan(21)
print(f"Luas bangun datar lingkaran : {luas6}")


# In[ ]:




