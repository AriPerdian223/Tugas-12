#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Bangun Ruang

def vol_kubus(sisi):
    volume = sisi**3 
    return volume

def vol_balok(panjang, lebar, tinggi):
    vol = panjang * lebar * tinggi
    return vol

def prisma_segitiga(alas, tSegitiga, tPrisma):
    pris = (1/2*alas*tSegitiga)*tPrisma
    return pris

def limas_segiempat(alas, tinggi):
    limas = 1/3*(alas**2)*18
    return limas

def vol_tabung(jari, tinggi):
    phi = 22/7
    vTabung = phi*(jari**2)*tinggi
    return vTabung

def vol_kerucut(jari, tinggi):
    phi2 = 22/7
    vKerucut = 1/3*phi2*jari*jari*tinggi
    return vKerucut

