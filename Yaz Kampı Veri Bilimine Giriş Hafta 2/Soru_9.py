# -*- coding: utf-8 -*-

#Soru 9 – String İşlemleri
"""
Bir cümle alın.
• Cümledeki kelimeleri split() ile ayırın.
• Her kelimenin ilk harfini büyük yaparak yeni bir string oluşturun.
• Örnek: "python veri bilimi" -> "Python Veri Bilimi"
"""

cumle = input("Bir cümle girin: ")

# 1) split() ile kelimelere ayır
kelimeler = cumle.split()

# 2) Her kelimenin ilk harfini büyük yap (capitalize())
yeni_kelimeler = [kelime.capitalize() for kelime in kelimeler]

# 3) join() ile tekrar birleştir
yeni_cumle = " ".join(yeni_kelimeler)

print("Sonuç:", yeni_cumle)


#%%
# Soru 9 – Kısayol Çözüm(Title ile)

cumle = input("Bir cümle girin: ")
yeni_cumle = cumle.title()
print("Sonuç:", yeni_cumle)

