# Metro Rota Simülasyonu

Bu proje, Python kullanarak metro istasyonları arasındaki en kısa ve en hızlı rotaları hesaplar. Akbank Bootcamp projesi olarak geliştirilmiştir.

## Özellikler

- **En az aktarmalı rota** bulma (BFS algoritması)
- **En hızlı rota** hesaplama (A* algoritması)
- Örnek metro ağı ile çalışır


## Nasıl Çalıştırılır?

1. Python'un yüklü olduğundan emin olun (3.6 veya üzeri)
2. Terminali açın ve proje klasörüne gidin
3. Şu komutu çalıştırın:

```bash
python metro_simulation.py
Kullanılan Teknolojiler
Python 3

collections modülü (defaultdict, deque)

heapq modülü

OOP (Nesne Yönelimli Programlama)

 --Örnek Çıktılar--

=== Test Senaryoları ===

1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören
Proje Yapısı
Copy
metro_simulation/
├── metro_simulation.py - Ana proje dosyası
├── README.md - Bu dosya
└── test_sonuclari.txt - Test çıktıları

Katkıda Bulunma

Hata bulursanız veya geliştirme öneriniz varsa:
*Issue açabilirsiniz
*Fork yapıp pull request gönderebilirsiniz
