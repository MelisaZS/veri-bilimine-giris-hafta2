# -*- coding: utf-8 -*-

#Soru 8 – List Comprehension
"""
1’den 100’e kadar olan sayılardan:
• Hem 3’e hem 5’e bölünebilenlerin karelerini içeren bir liste oluşturun.
• Sonucu ekrana yazdırın.
"""

sonuc = [x**2 for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(sonuc)
