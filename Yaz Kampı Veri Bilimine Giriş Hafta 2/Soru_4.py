# -*- coding: utf-8 -*-

#Soru 4 – Liste İşlemleri
"""
[12, 4, 9, 25, 30, 7, 18] listesini kullanın.
• Listenin ortalamasını bulun.
• Ortalamadan büyük sayıları ayrı bir listeye atın.
• Sonucu ekrana yazdırın
"""

sayilar = [12, 4, 9, 25, 30, 7, 18]

# 1) Ortalama
ortalama = sum(sayilar) / len(sayilar)
print("Ortalama:", ortalama)

# 2) Ortalamadan büyük olan sayıları filtrele
buyukler = []  # boş liste
for s in sayilar:
    if s > ortalama:
        buyukler.append(s)

# 3) Sonuçları yazdır
print("Ortalamadan büyük sayılar:", buyukler)