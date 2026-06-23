# 🗞️ Basında Bugün - Haber Sitesi

Türkiye'den en güncel haberler için Flask ve **MediaStack API** kullanan modern, responsive bir haber sitesi.

## 🎯 Özellikler

- ✅ **Real-time Haberler**: MediaStack API entegrasyonu ile Türkiye'deki son dakika haberler
- 🎨 **Modern Tasarım**: Responsive grid layout ve smooth animations
- 🔍 **Arama ve Filtreleme**: Başlığa göre haberler arasında hızlı arama
- 📱 **Mobil Uyumlu**: Tüm cihazlarda perfect görüntü
- 🌙 **Dark Mode**: Gece modu (hazır - kullanıma açık)
- ⚡ **Performant**: Optimize edilmiş CSS ve JavaScript
- 🛡️ **Güvenli**: API anahtarını .env dosyasında saklı

## 🚀 Başlangıç

### Gereksinimler
- Python 3.8+
- pip (Python package manager)

### Kurulum Adımları

1. **Depoyu klonla** (veya dosyaları indir)
```bash
git clone https://github.com/pekyamaner/basinda-bugun.git
cd basinda-bugun
```

2. **Sanal ortam oluştur** (önerilir)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Bağımlılıkları yükle**
```bash
pip install -r requirements.txt
```

4. **.env dosyası oluştur**
```bash
# .env.example dosyasını kopyala
cp .env.example .env
```

5. **MediaStack API Anahtarı**
   - Zaten entegre edilmiş: `ec437a7b7d79b819ef753263eba87c2d`
   - Veya [mediastack.com](https://mediastack.com) adresinden kendin alabilirsin
   - `.env` dosyasındaki `MEDIASTACK_API_KEY` değerini güncelle

6. **Uygulamayı çalıştır**
```bash
python app.py
```

7. **Tarayıcıda aç**
   - `http://localhost:5000` adresine git

## 📁 Proje Yapısı

```
basinda-bugun/
├── app.py                 # Flask ana uygulaması (MediaStack API)
├── requirements.txt       # Python bağımlılıkları
├── .env.example          # Ortam değişkenleri örneği
├── .env                  # Ortam değişkenleri (git'de yok)
├── README.md             # Bu dosya
└── templates/
    └── index.html        # Ana sayfa HTML şablonu
└── static/
    ├── style.css         # Stil ve tasarım
    └── script.js         # İnteraktif özellikleri
```

## 📡 Kullanılan API: MediaStack

**MediaStack** Türkiye ve 80+ ülkeden haberleri getiren güçlü bir haberler API'sidir.

### API Özellikleri:
- ✅ Türkiye haberleri
- ✅ 80+ ülkeden haber kaynakları
- ✅ Gerçek zamanlı güncelleme
- ✅ Ücretsiz plan mevcut
- ✅ Güvenilir ve hızlı

### Örnek API Çağrısı:
```python
url = "http://api.mediastack.com/v1/news"
params = {
    "access_key": "YOUR_API_KEY",
    "countries": "tr",
    "limit": 20,
    "sort": "published_desc"
}
response = requests.get(url, params=params)
```

## 🎨 Tasarım Özellikleri

### Renk Paleti
- **Ana Renk**: #2563eb (Mavi)
- **İkincil Renk**: #1e40af (Koyu Mavi)
- **Vurgu Rengi**: #f59e0b (Sarı)

### Responsive Breakpoints
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobil: < 768px

## 🔧 Özelleştirme

### API Parametrelerini Değiştir
`app.py` dosyasında parametreleri düzenle:
```python
params = {
    "access_key": MEDIASTACK_API_KEY,
    "countries": "tr",           # Ülke kodu
    "limit": 20,                 # Kaç haber alınacak
    "sort": "published_desc",    # Sıralama (published_desc, popularity)
    "keywords": "spor"           # İsteğe bağlı: anahtar kelime
}
```

### Stil Değiştir
`static/style.css` dosyasındaki CSS değişkenlerini edit et:
```css
:root {
    --primary-color: #2563eb;    /* Ana renk */
    --secondary-color: #1e40af;  /* İkincil renk */
    --accent-color: #f59e0b;     /* Vurgu rengi */
    /* ... */
}
```

## 🔐 Güvenlik

- API anahtarı `.env` dosyasında saklanır
- `.env` dosyası `.gitignore`'a eklendi (git'e yüklenmez)
- HTML çıktısında XSS saldırısından korunma
- Güvenli HTTP isteği (timeout ve error handling)

## 📦 Kullanılan Teknolojiler

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: MediaStack.com
- **İkonlar**: Font Awesome 6.4.0
- **Görseller**: Unsplash & API

## 🐛 Sorun Giderme

### "MediaStack API Hatası" 
- API anahtarı yanlış veya geçersiz
- `.env` dosyasındaki anahtarı kontrol et
- [mediastack.com](https://mediastack.com) adresinden yeni anahtar al

### Haberler Yüklenmiyorsa
- İnternet bağlantısını kontrol et
- MediaStack'in website'i açık mı kontrol et
- Tarayıcınızın konsol (F12) bölümünde hata mesajına bak

### Timeout Hatası
- API'ye bağlanmada zaman aşımı
- İnternet bağlantısını kontrol et
- Birkaç saniye sonra tekrar deneyin

## 🚀 İleri Özellikler (Gelecek Güncellemeler)

- [ ] Kategori filtrelemesi
- [ ] Kaynak filtrelemesi
- [ ] Haber detay sayfası
- [ ] Favoriler/Kaydedilmiş haberler
- [ ] Arama geçmişi
- [ ] Pagination (sayfalama)
- [ ] Database entegrasyonu
- [ ] Admin paneli
- [ ] Dark mode switch

## 📝 Lisans

Bu proje açık kaynak kodludur. Özgürce kullanabilirsiniz.

## 👤 Yazar

**Pek Yamaner**
- GitHub: [@pekyamaner](https://github.com/pekyamaner)

## 💬 İletişim

Sorularınız, önerileriniz veya hata bildirimleri için:
- GitHub Issues'i kullan
- [GitHub Discussions](https://github.com/pekyamaner/basinda-bugun/discussions) açık

---

**Keyifli kodlamalar!** 🎉

**API Kaynağı:** [MediaStack.com](https://mediastack.com)
