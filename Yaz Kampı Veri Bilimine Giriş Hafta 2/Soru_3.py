# -*- coding: utf-8 -*-

#Soru 3 – Şifre Kontrolü (String Metotları)
"""Kullanıcıdan şifre girmesini isteyin. Şifre:
• En az 8 karakter olmalı
• En az 1 büyük harf içermeli
• En az 1 rakam içermeli
Koşulları sağlayıp sağlamadığına göre kullanıcıyı bilgilendirin.
"""

sifre = input("Bir şifre girin: ")

# 1) Uzunluk kontrolü
uzunluk = len(sifre) >= 8

# 2) Büyük harf kontrolü (isupper → harf büyük mü diye bakar)
buyuk_harf_var = any(harf.isupper() for harf in sifre)

# 3) Rakam kontrolü (isdigit → karakter rakam mı diye bakar)
rakam_var = any(harf.isdigit() for harf in sifre)

# Şimdi tüm koşulları kontrol edelim
if uzunluk and buyuk_harf_var and rakam_var:
    print("Şifre geçerli")
else:
    print("Şifre geçersiz")
    if not uzunluk:
        print("Şifre en az 8 karakter olmalı")
    if not buyuk_harf_var:
        print("Şifre en az 1 büyük harf içermeli")
    if not rakam_var:
        print("Şifre en az 1 rakam içermeli")
        
        
        