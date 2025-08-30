# -*- coding: utf-8 -*-

"""
Mini Proje – Film Yorumu Analizi
Proje Tanımı:
Kullanıcıdan birkaç film yorumu alın (örneğin 5–6 yorum).
- Yorumları bir listeye atın.
- Her yorumun uzunluğunu (karakter sayısı) bulun.
- Kaç yorumda "iyi" kelimesi geçtiğini sayın.
- En uzun yorumu ve en kısa yorumu ekrana yazdırın.
- Tüm yorumların ortalama uzunluğunu hesaplayın.

Beklenen Çıktı Örneği
Girdi (yorumlar):
["Film çok güzeldi", "Kötüydü", "Ortalama bir filmdi", "Gerçekten çok iyi!", "İyi ama daha iyi
olabilirdi"]
Çıktı:
Toplam yorum sayısı: 5
"iyi" geçen yorum sayısı: 2
En uzun yorum: İyi ama daha iyi olabilirdi
En kısa yorum: Kötüydü
Ortalama uzunluk: 17.4 karakter
"""

yorumlar = ["Film çok güzeldi", "Kötüydü", "Ortalama bir filmdi", "Gerçekten çok iyi!", "İyi ama daha iyi olabilirdi"]

print("Toplam yorum sayısı:", len(yorumlar))
print('"iyi" geçen yorum sayısı:', sum("iyi" in y.lower() for y in yorumlar))
print("En uzun yorum:", max(yorumlar, key=len))
print("En kısa yorum:", min(yorumlar, key=len))
print("Ortalama uzunluk:", sum(len(y) for y in yorumlar) / len(yorumlar))


























