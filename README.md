# MelisaZarif_MetroSimulation  
###### Akbank Python Bootcamp Projesi - Metro Rota Optimizasyonu  

Bu proje, Python'da graf veri yapısı kullanılarak metro istasyonları arasında:  
✔ **En az aktarmalı rotayı** (BFS algoritması)  
✔ **En hızlı rotayı** (A* algoritması) bulan bir simülasyondur.  

---

## 📋 Proje Gereklilikleri Karşılama Durumu  
| Gereklilik | Durum |  
|------------|-------|  
| Graf veri yapısı ile metro ağı modelleme | ✅ Tamamlandı |  
| BFS ile en az aktarmalı rota | ✅ Tamamlandı |  
| A* ile en hızlı rota | ✅ Tamamlandı |  
| Dokümantasyon (README.md) | ⚠️ Bu dosya |  

---

## 🛠️ Teknik Detaylar  
### Kullanılan Algoritmalar  
#### 1. BFS (Breadth-First Search)  
- **Mantık**: Her istasyonu seviye seviye tarar, ilk bulduğu çözüm en az aktarmalı olandır.  
- **Kodda Kullanım**: `deque` ile kuyruk yapısı oluşturuldu.  
```  
def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:  
    # BFS implementasyonu...  
2. A* Algoritması
Mantık: Tahmini maliyet (heuristic) ile en kısa süreli rotayı bulur.

Kodda Kullanım: heapq ile öncelik kuyruğu kullanıldı.


def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:  
    # A* implementasyonu...  
Kütüphaneler
Kütüphane	Amaç
collections	defaultdict ve deque için
heapq	A*'da öncelik kuyruğu için
🚀 Nasıl Çalıştırılır?
Terminali açın:

python MelisaZarif_MetroSimulation.py

Test senaryoları otomatik çalışacaktır:

=== Test Senaryoları ===  
1. AŞTİ'den OSB'ye:  
   En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB  
📊 Test Sonuçları
Senaryo	Sonuç
AŞTİ → OSB	25 dakika
Batıkent → Keçiören	21 dakika
Keçiören → AŞTİ	19 dakika
✨ Projeyi Geliştirme Fikirleri
Rotaları görselleştirmek için matplotlib eklenebilir.

Gerçek dünya metro ağları için JSON veri girişi yapılabilir.

📜 Lisans
MIT Lisansı ile lisanslanmıştır. Proje dokümanında belirtilen kurallara uygun kullanınız.


### ✅ **Gerekliliklerle Tam Uyumlu Hale Getirme**  
1. **Algoritma Açıklamaları**: BFS ve A*'ın çalışma mantığı eklendi.  
2. **Kütüphane Detayları**: `collections` ve `heapq` kullanım amaçları belirtildi.  
3. **Test Sonuçları**: Tablo formatında gösterildi.  
4. **Proje Geliştirme Fikirleri**: Opsiyonel öneriler eklendi.  

---

### 📥 **GitHub'a Yükleme**  
1. Bu içeriği kopyalayıp GitHub'da **README.md** dosyasına yapıştırın.  
2. Veya yerelde `README.md` olarak kaydedip:  
   ```bash  
   git add README.md  
   git commit -m "README proje gerekliliklerine göre güncellendi"  
   git push origin main  
