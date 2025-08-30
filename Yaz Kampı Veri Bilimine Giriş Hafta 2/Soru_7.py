# -*- coding: utf-8 -*-

#Soru 7 – Palindrom Kontrolü
"""
Kullanıcıdan bir kelime isteyin.
• Kelimenin palindrom olup olmadığını kontrol edin.
• Örnek: "kayak" → Palindrom, "python" → Değil
"""

kelime = input("Bir kelime girin: ")

# Kelimenin tersten yazılışı [::-1] ile elde edilir
if kelime == kelime[::-1]:
    print("Palindrom")
else:
    print("Palindrom değil")
