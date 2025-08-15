# Staj-Bitirme-Projem
1. Hafta – Proje Planlama ve Altyapı Hazırlığı

Gün 1:

Staj başlangıcı.

Firma/proje tanıtımı yapıldı.

Film ve dizi izleme platformu fikri belirlendi.

Kullanıcı girişi, içerik listesi ve detay sayfası gibi temel özellikler belirlendi.

Kullanılacak teknolojiler üzerine araştırma yapıldı (Flask, SQLAlchemy, HTML/CSS).

Gün 2:

Flask framework’ünün kurulumu yapıldı.

requirements.txt dosyası oluşturuldu.

Flask uygulaması için temel proje klasör yapısı (app.py, templates, static) oluşturuldu.

Gün 3:

SQLite veritabanı ile çalışma yöntemleri incelendi.

SQLAlchemy ORM yapısı öğrenildi.

Veritabanı şeması taslağı çıkarıldı:

Kullanıcı tablosu

Film/Dizi tablosu

Yorumlar tablosu

Gün 4:

init_db.py ile veritabanı başlatma scripti yazıldı.

Kullanıcı modeli ve içerik modeli kodlandı.

İlk veritabanı oluşturma testi yapıldı.

Gün 5:

Flask-WTF ile form oluşturma yöntemleri denendi.

Kullanıcı kayıt formu ve giriş formu tasarlandı.

Form doğrulama kuralları eklendi (e-posta, şifre uzunluğu vb.).

2. Hafta – Kullanıcı Yönetimi ve Temel Sayfalar

Gün 6:

Flask-Login ile oturum yönetimi entegre edildi.

Kullanıcı giriş/çıkış fonksiyonları yazıldı.

login_required dekoratörü ile sayfa koruma eklendi.

Gün 7:

HTML şablon yapısına giriş yapıldı.

templates klasöründe base.html oluşturuldu.

Bootstrap ile temel responsive tasarım eklendi.

Gün 8:

Ana sayfa (index.html) tasarlandı.

Film ve dizi listelerinin veritabanından çekilip dinamik olarak listelenmesi sağlandı.

Gün 9:

İçerik detay sayfası (detail.html) oluşturuldu.

İçerik açıklaması, afiş görseli, kategori ve izlenme sayısı gösterildi.

Gün 10:

Kullanıcıların içerik ekleyebilmesi için form geliştirildi.

Resim yükleme ve dosya yolu yönetimi (fix_image_paths.py) eklendi.

3. Hafta – İçerik Yönetimi ve İyileştirmeler

Gün 11:

Yorum ekleme özelliği geliştirildi.

Yorumlar veritabanına kaydedildi ve içerik detay sayfasında listelendi.

Gün 12:

İçerik düzenleme ve silme fonksiyonları eklendi.

Yetkilendirme kontrolleri yapıldı (sadece admin içerik silebilir).

Gün 13:

static klasöründe CSS dosyaları düzenlendi.

Mobil uyumluluk iyileştirmeleri yapıldı.

Gün 14:

update_db.py ile toplu veri ekleme işlemleri geliştirildi.

Test verileri eklenerek platformun içerik sayısı artırıldı.

Gün 15:

Oturum açmamış kullanıcıların sadece içerik listeleme ve detay sayfalarına erişebilmesi sağlandı.

Hata sayfaları (404.html, 500.html) oluşturuldu.

4. Hafta – Test, Optimizasyon ve Son Hazırlıklar

Gün 16:

Kod düzenlemesi ve gereksiz dosyaların temizliği yapıldı.

check_db.py ile veritabanı kontrol scripti çalıştırıldı.

Gün 17:

Görsel optimizasyon yapıldı (afiş boyutları küçültüldü).

fix_delibal_image.py ile hatalı resim yolları düzeltildi.

Gün 18:

JavaScript ile arama fonksiyonu geliştirildi.

Kullanıcılar başlık üzerinden içerik arayabiliyor.

Gün 19:

Kategori bazlı filtreleme özelliği eklendi.

Kullanıcı deneyimi testleri yapıldı.

Gün 20:

Admin paneli temel fonksiyonları yazıldı.

İçerik ekleme/düzenleme işlemleri admin panelinden yapılabilir hale geldi.

5. Hafta – Yayın Öncesi Test ve Raporlama

Gün 21:

Form hataları ve giriş/çıkış işlemleri test edildi.

Tüm sayfalarda giriş kontrolü doğrulandı.

Gün 22:

SQL sorgu optimizasyonu yapıldı.

Gereksiz veri tekrarları giderildi.

Gün 23:

Site performans testi yapıldı.

Tarayıcı uyumluluk testleri gerçekleştirildi.

Gün 24:

Kullanıcı deneyimi (UX) testi yapıldı, geri bildirimler alındı.

Navigasyon menüsü iyileştirildi.

Gün 25:

Proje dokümantasyonu hazırlandı.

Kod yorum satırları eklendi.

6. Hafta – Final Düzenlemeler ve Sunum

Gün 26:

Küçük hata düzeltmeleri yapıldı.

Veritabanı yedekleme scripti eklendi.

Gün 27:

Mobil cihazlarda test edildi, tasarım bozulmaları giderildi.

Gün 28:

Proje sunumu için slaytlar hazırlandı.

Ekran görüntüleri alındı.

Gün 29:

Projenin canlı ortamda çalıştırılması test edildi.

Ortam değişkenleri .env dosyası ile düzenlendi.

Gün 30:

Proje sunumu yapıldı.

Staj raporu hazırlandı ve teslim edildi.
