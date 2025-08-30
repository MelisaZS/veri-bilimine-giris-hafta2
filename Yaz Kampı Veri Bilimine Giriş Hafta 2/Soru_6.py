# -*- coding: utf-8 -*-

#Soru 6 – While Döngüsü
"""
Kullanıcıdan sürekli sayı isteyin.
• Kullanıcı 0 girdiğinde program dursun.
• Girilen tüm sayıların toplamını ve ortalamasını yazdırın.
"""

toplam = 0   # sayıların toplamını tutacak
adet = 0     # kaç sayı girildiğini tutacak

while True:
    n = int(input("Bir sayı girin (çıkmak için 0): "))
    
    if n == 0:   #çıkış koşulu
        break
    
    toplam += n  #toplamı artır
    adet += 1    #sayı adedini artır

# Ortalama hesapla (sıfıra bölünmeyi önlemek için kontrol ekliyoruz)
if adet > 0:
    ortalama = toplam / adet
    print("Toplam:", toplam)
    print("Ortalama:", ortalama)
else:
    print("Hiç sayı girilmedi.")





