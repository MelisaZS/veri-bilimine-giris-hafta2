# -*- coding: utf-8 -*-


# Soru 1 – Sayı Analizi
"""
İstenilen:
Kullanıcıdan bir sayı isteyin.
• Sayı pozitif, negatif ya da sıfır mı kontrol edin.
• Aynı zamanda tek/çift olup olmadığını da belirtin.
• Çıktı örneği: "Pozitif Çift" veya "Negatif Tek" gibi.
"""

n = int(input("Bir tam sayı girin: "))

if n > 0:
    isaret = "Pozitif"
elif n < 0:
    isaret = "Negatif"
else:
    isaret = "Sıfır"

if n % 2 == 0:
    tek_cift = "Çift"
else:
    tek_cift = "Tek"

print(isaret, tek_cift)



































