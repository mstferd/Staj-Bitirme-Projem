# Flask ve gerekli modülleri içe aktar
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Flask uygulamasını oluştur
app = Flask(__name__)

# Uygulama ayarları
app.config['SECRET_KEY'] = os.urandom(24)  # Güvenlik için önemli bir gizli anahtar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watchlist.db'  # Veritabanı dosyasının konumu

# SQLAlchemy veritabanı bağlantısını başlat
db = SQLAlchemy(app)

# Kullanıcı giriş yönetimi için LoginManager'ı başlat
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Giriş gerektiren sayfalara erişimde yönlendirilecek sayfa

# Models
# Kullanıcı modeli
class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Veritabanındaki tablo adı
    
    # Sütunlar
    id = db.Column(db.Integer, primary_key=True)  # Benzersiz kullanıcı ID'si
    username = db.Column(db.String(80), unique=True, nullable=False)  # Kullanıcı adı (benzersiz)
    password_hash = db.Column(db.String(120), nullable=False)  # Şifrenin hash'lenmiş hali
    
    # İlişkiler
    watchlists = db.relationship('Watchlist', backref='user', lazy=True)  # Kullanıcının izleme listesi öğeleri

# İçerik modeli (Filmler ve Diziler)
class Content(db.Model):
    __tablename__ = 'contents'  # Veritabanındaki tablo adı
    
    # Sütunlar
    id = db.Column(db.Integer, primary_key=True)  # Benzersiz içerik ID'si
    title = db.Column(db.String(100), nullable=False)  # İçerik başlığı
    type = db.Column(db.String(20), nullable=False)  # İçerik türü: 'movie' (film) veya 'series' (dizi)
    genre = db.Column(db.String(50))  # Tür (örneğin: Aksiyon, Komedi, Dram)
    director = db.Column(db.String(100))  # Yönetmen
    duration = db.Column(db.Integer)  # Süre (dakika cinsinden)
    description = db.Column(db.Text)  # İçerik açıklaması
    image_url = db.Column(db.String(255))  # Kapak resmi URL'si
    
    # İlişkiler
    watchlists = db.relationship('Watchlist', backref='content', lazy=True)  # Bu içeriği izleme listesine ekleyen kullanıcılar

# İzleme listesi modeli
class Watchlist(db.Model):
    __tablename__ = 'watchlists'  # Veritabanındaki tablo adı
    
    # Sütunlar
    id = db.Column(db.Integer, primary_key=True)  # Benzersiz izleme listesi öğe ID'si
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Kullanıcı ID'si (yabancı anahtar)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)  # İçerik ID'si (yabancı anahtar)
    watched = db.Column(db.Boolean, default=False)  # Bu satır önemli!
    added_date = db.Column(db.DateTime, default=db.func.current_timestamp())  # Ekleme tarihi (otomatik)

# Kullanıcı yükleyici - Flask-Login için gerekli
@login_manager.user_loader
def load_user(user_id):
    # Kullanıcı ID'sine göre kullanıcıyı veritabanından yükle
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    # Ana sayfada tüm içerikleri listele
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

# Kullanıcı kayıt işlemi için route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Eğer form gönderildiyse (POST isteği)
    if request.method == 'POST':
        # Formdan kullanıcı adı ve şifreyi al
        username = request.form['username']
        password = request.form['password']
        
        # Kullanıcı adının zaten alınmış olup olmadığını kontrol et
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            # Eğer kullanıcı adı alınmışsa hata mesajı göster
            flash('Bu kullanıcı adı zaten alınmış', 'danger')
            return redirect(url_for('register'))
        
        # Yeni kullanıcı oluştur ve şifreyi güvenli bir şekilde hash'le
        hashed_password = generate_password_hash(password)
        user = User(username=username, password_hash=hashed_password)
        
        # Kullanıcıyı veritabanına kaydet
        db.session.add(user)
        db.session.commit()
        
        # Başarılı kayıt mesajı göster ve giriş sayfasına yönlendir
        flash('Kayıt başarılı. Giriş yapabilirsiniz.', 'success')
        return redirect(url_for('login'))
    
    # GET isteği için kayıt formunu göster
    return render_template('register.html')

# Kullanıcı giriş işlemi için route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Eğer form gönderildiyse (POST isteği)
    if request.method == 'POST':
        # Formdan kullanıcı adı ve şifreyi al
        username = request.form['username']
        password = request.form['password']
        # 'Beni Hatırla' seçeneğinin işaretli olup olmadığını kontrol et
        remember = request.form.get('remember') == 'on'
        
        # Kullanıcıyı veritabanında ara
        user = User.query.filter_by(username=username).first()
        
        # Kullanıcı varsa ve şifre doğruysa
        if user and check_password_hash(user.password_hash, password):
            # Kullanıcıyı giriş yaptır ve 'Beni Hatırla' seçeneğini uygula
            login_user(user, remember=remember)
            # Eğer önceki bir sayfadan yönlendirildiysek oraya, değilse ana sayfaya git
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        
        # Giriş başarısızsa hata mesajı göster
        flash('Geçersiz kullanıcı adı veya şifre', 'danger')
    
    # GET isteği için giriş formunu göster
    return render_template('login.html')

# Kullanıcı çıkış işlemi için route
# Sadece giriş yapmış kullanıcılar erişebilir
@app.route('/logout')
@login_required
def logout():
    # Kullanıcıyı sistemden çıkar
    logout_user()
    # Ana sayfaya yönlendir
    return redirect(url_for('index'))

# Kullanıcının izleme listesini gösteren route
# Sadece giriş yapmış kullanıcılar erişebilir
@app.route('/watchlist')
@login_required
def watchlist():
    # Kullanıcının izleme listesini veritabanından çek
    # İlişkili içerik bilgilerini de yükle (N+1 sorgu sorununu önlemek için)
    user_watchlist = Watchlist.query.options(
        db.joinedload(Watchlist.content)
    ).filter_by(user_id=current_user.id).all()
    
    # İzleme listesi sayfasını göster
    return render_template('watchlist.html', watchlist=user_watchlist)

# İçeriği izleme listesine eklemek için route
# Sadece giriş yapmış kullanıcılar erişebilir
@app.route('/add_to_watchlist/<int:content_id>')
@login_required
def add_to_watchlist(content_id):
    # İçeriğin zaten kullanıcının izleme listesinde olup olmadığını kontrol et
    existing = Watchlist.query.filter_by(
        user_id=current_user.id, content_id=content_id
    ).first()
    
    # Eğer içerik izleme listesinde yoksa ekle
    if not existing:
        watchlist_item = Watchlist(user_id=current_user.id, content_id=content_id)
        db.session.add(watchlist_item)
        db.session.commit()
        flash('İçerik izleme listenize eklendi', 'success')
    else:
        # İçerik zaten listedeyse bilgi mesajı göster
        flash('Bu içerik zaten izleme listenizde', 'info')
        
    # Kullanıcıyı izleme listesi sayfasına yönlendir
    return redirect(url_for('watchlist'))

# İçeriği izlendi olarak işaretlemek için route
# Sadece giriş yapmış kullanıcılar erişebilir
@app.route('/mark_watched/<int:watchlist_id>', methods=['POST', 'GET'])
@login_required
def mark_watched(watchlist_id):
    item = Watchlist.query.get_or_404(watchlist_id)
    if item.user_id != current_user.id:
        abort(403)
    item.watched = True
    db.session.commit()
    if request.method == 'POST':
        return '', 204  # AJAX için boş cevap
    flash('İçerik izlendi olarak işaretlendi.', 'success')
    return redirect(url_for('watchlist'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Veritabanı tablolarını oluşturur  # Veritabanı tablolarını oluşturur
    app.run(debug=True, port=8080)
