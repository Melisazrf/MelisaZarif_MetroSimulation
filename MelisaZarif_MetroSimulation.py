from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional


class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """
        AMAÇ: En az aktarmalı rotayı bulmak (BFS seviye seviye arama yapar).

        NASIL ÇALIŞIR?
        1. Başlangıç istasyonundan başlar, tüm komşularını tek tek tarar.
        2. Kuyruk (deque) kullanır çünkü FIFO mantığıyla ilk bulduğu çözüm en kısadır.
        3. Ziyaret edilenleri set() ile takip ederek döngüyü önler.

        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Geçersiz istasyon kontrolü

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # Kuyruk: (mevcut_istasyon, rota)
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set([baslangic])  # Tekrar ziyareti engelle

        while kuyruk:
            current, rota = kuyruk.popleft()  # Kuyruğun BAŞINDAN al (FIFO)

            if current == hedef:
                return rota  # Hedefe ulaşıldı!

            for komsu, _ in current.komsular:  # Tüm komşuları gez
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, rota + [komsu]))  # Yeni rotayı kuyruğa ekle

        return None  # Rota yoksa

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """
        AMAÇ: En kısa süreli rotayı bulmak (A* tahmini maliyet kullanır).

        NASIL ÇALIŞIR?
        1. Öncelik kuyruğu (min-heap) kullanır. En düşük maliyetli rotayı önce çeker.
        2. Her adımda toplam süreyi hesaplar: g(n) = mevcut süre, h(n) = 0 (basit versiyon).
        3. Ziyaret edilenleri set() ile takip eder.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Geçersiz istasyon kontrolü

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # Min-Heap: (toplam_sure, id(current), current, rota)
        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = set()

        while pq:
            toplam_sure, _, current, rota = heapq.heappop(pq)  # En düşük süreli rotayı al

            if current == hedef:
                return (rota, toplam_sure)  # Hedefe ulaşıldı!

            if current in ziyaret_edildi:
                continue  # Zaten ziyaret edildiyse atla

            ziyaret_edildi.add(current)

            for komsu, sure in current.komsular:
                if komsu not in ziyaret_edildi:
                    yeni_toplam = toplam_sure + sure
                    heapq.heappush(pq, (yeni_toplam, id(komsu), komsu, rota + [komsu]))  # Kuyruğa ekle

        return None  # Rota yoksa


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    print("\n=== Gelişmiş Test Senaryoları ===")

    # Senaryo 4: Aynı hat üzerinde komşu istasyonlar
    print("\n4. Kızılay -> Ulus (Kırmızı Hat üzerinde direkt bağlantı):")
    sonuc = metro.en_hizli_rota_bul("K1", "K2")
    if sonuc:
        rota, sure = sonuc
        print(f"Direkt rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 5: Uzak istasyonlar
    print("\n6. OSB -> Keçiören (Şehir karşı uçları):")
    sonuc = metro.en_hizli_rota_bul("K4", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 6: Aynı istasyon (Edge case)
    print("\n7. Kızılay -> Kızılay (Aynı istasyon):")
    sonuc = metro.en_hizli_rota_bul("K1", "K1")
    if sonuc:
        rota, sure = sonuc
        print(f"Sonuç: {sure} dakika", " -> ".join(i.ad for i in rota) if rota else "Başlangıç noktası")
    else:
        print("Hata: Aynı istasyon seçildi")

   # Senaryo 7: Sıhhiye'den Keçiören'e
    print("\n7. Sıhhiye'den Keçiören'e:")
    rota = metro.en_az_aktarma_bul("M3", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M3", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
