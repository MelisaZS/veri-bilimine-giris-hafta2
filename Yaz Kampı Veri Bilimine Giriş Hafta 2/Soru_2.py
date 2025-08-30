# -*- coding: utf-8 -*-

#Soru 2 – Harf Frekansı (String)
""" 
Kullanıcıdan bir kelime alın.
• Hangi harften kaç tane geçtiğini bulun.
• Sonucu dictionary olarak gösterin.
Örnek: "data" → {'d': 1, 'a': 2, 't': 1}
"""

kelime = input("Bir kelime girin: ")

x = {}  # boş sözlük oluşturuyoruz

for harf in kelime:  # kelimedeki her harfi sırayla dolaş
    if harf in x:       # harf zaten sözlükte varsa
        x[harf] += 1    # sayacını 1 artır
    else:               # yoksa
        x[harf] = 1     # o harfi sözlüğe ekle ve 1 yap

print(x)
