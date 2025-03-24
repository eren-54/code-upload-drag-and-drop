SÜRÜCÜSÜZ METRO SİMÜLASYONU (ROTA OPTİMİZASYONU)

Bu proje, bir metro ağında iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı bulan bir simülasyon geliştirmeyi amaçlamaktadır. Breadth-First Search (BFS) algoritması kullanarak en az aktarmalı rotayı, A* algoritması kullanarak en hızlı rotayı belirleyebiliriz.

KULLANILAN TEKNOLOJİLER VE KÜTÜPHANELER

Projede Python programlama dili kullanılmıştır. Aşağıdaki kütüphaneler kullanılmıştır:

collections.deque: BFS algoritmasında kuyruk yapısını kullanarak istasyonlar arasında en az aktarmalı rotayı bulmak için kullanıldı.
heapq: A* algoritmasında öncelikli kuyruk yapısı ile en hızlı rotayı hesaplamak için kullanıldı.
defaultdict: Metro ağı yapısının daha esnek tanımlanması için kullanıldı.

ALGORİTMALARIN ÇALIŞMA MANTIĞI

1. BFS ALGORİTMASI (EN AZ AKTARMALI ROTA BULMA)

BFS (Breadth-First Search), graflarda en kısa yolu bulmak için kullanılan bir algoritmadır. Bu projede en az aktarmalı rotayı bulmak için kullanılmıştır.

Nasıl çalışır?

Bir kuyruk (queue) yapısı oluşturulur.
Başlangıç istasyonu kuyruğa eklenir ve ziyaret edilmiş olarak işaretlenir.
Kuyrukta eleman olduğu sürece döngü devam eder: çıkarılan istasyonun komşularına gidilir.
Komşu istasyon daha önce ziyaret edilmemişse kuyruğa eklenir.
Gidecek istasyon hedef istasyonla eşleşirse, rota bulunmuş olur.

Neden BFS kullanıyoruz?

Ağaç veya graf yapılarında en az adımda ulaşmayı garanti eder.
Metro ağı gibi düğümlerin (istasyonlar) az olduğu yapılarda verimli çalışır.

2. A* ALGORİTMASI (EN HIZLI ROTA BULMA)

A* (A-Star) algoritması, en hızlı rotayı bulmak için kullanılır. A*, Dijkstra algoritması gibi tüm yolları değerlendirmek yerine bir hedefe doğru ilerleme stratejisini kullanarak en iyi yolu bulur.

Nasıl çalışır?

Öncelikli kuyruk (heapq) oluşturulur.
Başlangıç istasyonu kuyruğa eklenir.
Her iterasyonda en az toplam maliyeti olan istasyon seçilir: bu istasyon hedefe ulaştıysa rota tamamlanmış olur.
Değilse komşuları öncelikli kuyruğa eklenir.
En iyi yolu bulmak için her adımda toplam süre değerlendirilir.

Neden A* kullanıyoruz?

Metro ağında en hızlı rotayı bulmak için uygun bir algoritmadır.
Heuristik (yaklaşık) bir maliyet fonksiyonu kullanarak gereksiz yolları eleme şansımız olur.
A* algoritması, optimum ve verimli bir çözüm sunar.

ÖRNEK KULLANIM VE TEST SONUÇLARI

Projeyi test etmek için metro ağı oluşturuldu ve farklı senaryolarla çalışması test edildi.

TEST SENARYOLARI VE BEKLENEN SONUÇLAR

1. AŞTİ'DEN OSB'YE

En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

2. BATIKENT'TEN KEÇİÖREN'E

En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. KEÇİÖREN'DEN AŞTİ'YE

En az aktarmalı rota: Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (19 dakika): Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

PROJEYİ GELİŞTİRME FİKİRLERİ

Bu proje, daha geliştirilebilir ve genişletilebilir bir yapıya sahiptir. İşte bazı geliştirme fikirleri:

Gerçek zamanlı veri ekleme: trafik yoğunluğu ve tren sıklığına göre anlık en iyi rota hesaplamaları.
Daha detaylı metro ağı: farklı metro hatları ve çok daha geniş bir istasyon ağı ekleme.
Görselleştirme: metro ağını grafiksel olarak görüntüleme (Matplotlib, NetworkX vb.).
Mobil veya web uygulaması: kullanıcıların metro ağında en iyi rotayı bulmaları için arayüz geliştirme.

Bu proje, algoritmik düşünme, graf veri yapıları ve rota optimizasyonu gibi konuları kapsayan güçlü bir simülasyon sunmaktadır.
