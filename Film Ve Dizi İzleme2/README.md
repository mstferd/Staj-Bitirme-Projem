# Film ve Dizi İzleme Servisi

Bu proje, kullanıcıların film ve dizileri izleyebilecekleri, listeler oluşturabilecekleri ve içerikleri yönetebilecekleri bir web uygulamasıdır.

## Özellikler

- Kullanıcı kaydı ve girişi
- Film ve dizi ekleme
- İzleme listeleri oluşturma
- İçerik arama ve filtreleme
- İzleme geçmişi takibi
- Kullanıcı profili yönetimi

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Veritabanını oluşturun:
```bash
python init_db.py
```

3. Uygulamayı başlatın:
```bash
python app.py
```

## Kullanım

1. Tarayıcınızda `http://localhost:8080` adresine gidin
2. Yeni bir hesap oluşturun veya mevcut hesabınızla giriş yapın
3. Film ve dizileri keşfedin, izleme listeleri oluşturun

## Teknik Detaylar

- Flask web framework'ü kullanılmıştır
- SQLite veritabanı ile veri depolama
- Flask-Login ile kullanıcı yönetimi
- Flask-WTF ile form işlemleri 