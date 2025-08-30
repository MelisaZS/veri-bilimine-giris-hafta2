# -*- coding: utf-8 -*-

#Soru 5 – Nested Loop (Desen)
"""
Aşağıdaki çıktıyı üreten programı yazın (üçgen desen):
*
**
***
****
*****
"""

# 5 satırlık üçgen için dış döngü
for i in range(1, 6):  # 1'den 5'e kadar (6 hariç)
    # Her satırda i tane yıldız yazdır
    for j in range(i):
        print("*", end="")  #end="" -> satır atlamadan yan yana yaz
    print()  # her satır bittiğinde alt satıra geç
