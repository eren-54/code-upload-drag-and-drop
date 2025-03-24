from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

# Istasyon sınıfı her metro istasyonunu temsil eder
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyonun kimliği
        self.ad = ad  # İstasyonun adı
        self.hat = hat  # İstasyonun ait olduğu hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # Komşu istasyonlar ve geçiş süreleri

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        """Bir istasyonu komşu olarak ekler."""
        self.komsular.append((istasyon, sure))

# Metro ağı sınıfı, tüm istasyonları ve bağlantıları yönetir
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # Tüm istasyonlar
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hatlara göre istasyon listesi

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        """Yeni bir istasyon ekler."""
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        """İki istasyon arasında bağlantı oluşturur."""
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """En az aktarma yapan rotayı bulur (BFS kullanarak)."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        kuyruk = deque([(self.istasyonlar[baslangic_id], [])])
        ziyaret_edilen = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()

            if mevcut.idx in ziyaret_edilen:
                continue

            ziyaret_edilen.add(mevcut.idx)
            yeni_yol = yol + [mevcut]

            if mevcut.idx == hedef_id:
                return yeni_yol  # Hedef istasyona ulaşıldı

            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edilen:
                    kuyruk.append((komsu, yeni_yol))

        return None  # Ulaşılabilir yol yoksa None döner

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """En hızlı rotayı bulur (Dijkstra algoritması kullanarak)."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        pq = [(0, self.istasyonlar[baslangic_id], [])]  # Öncelikli kuyruk (toplam süre, istasyon, yol)
        ziyaret_edilen = {}

        while pq:
            toplam_sure, mevcut, yol = heapq.heappop(pq)

            if mevcut.idx in ziyaret_edilen and ziyaret_edilen[mevcut.idx] <= toplam_sure:
                continue

            ziyaret_edilen[mevcut.idx] = toplam_sure
            yeni_yol = yol + [mevcut]

            if mevcut.idx == hedef_id:
                return yeni_yol, toplam_sure  # Hedef istasyona ulaşıldı

            for komsu, sure in mevcut.komsular:
                heapq.heappush(pq, (toplam_sure + sure, komsu, yeni_yol))

        return None  # Ulaşılabilir yol yoksa None döner

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonları ekleyelim
    metro.istasyon_ekle("A1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("A2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("A3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("A4", "Gar", "Mavi Hat")
    metro.istasyon_ekle("B1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("B2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("B3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("B4", "Keçiören", "Turuncu Hat")

    # İstasyonlar arasındaki bağlantıları oluşturalım
    metro.baglanti_ekle("A1", "A2", 5)
    metro.baglanti_ekle("A2", "A3", 3)
    metro.baglanti_ekle("A3", "A4", 4)
    metro.baglanti_ekle("B1", "B2", 7)
    metro.baglanti_ekle("B2", "B3", 9)
    metro.baglanti_ekle("B3", "B4", 5)
    metro.baglanti_ekle("A4", "B3", 2)
    metro.baglanti_ekle("A2", "B2", 3)

    print("\n=== Test Senaryoları ===")

    print("\n1. AŞTİ'den Keçiören'e:")
    rota = metro.en_az_aktarma_bul("A1", "B4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("A1", "B4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
