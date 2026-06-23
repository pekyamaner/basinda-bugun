# 🗞️ Basında Bugün - Haber Sitesi

Türkiye'den en güncel haberler için Flask ve NewsAPI kullanan modern, responsive bir haber sitesi.

## 🎯 Özellikler

- ✅ **Real-time Haberler**: NewsAPI entegrasyonu ile Türkiye'deki son dakika haberler
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

5. **NewsAPI Anahtarı Al**
   - [newsapi.org](https://newsapi.org) adresine git
   - Ücretsiz anahtar al
   - `.env` dosyasındaki `NEWSAPI_KEY` değerini güncelle

6. **Uygulamayı çalıştır**
```bash
python app.py
```

7. **Tarayıcıda aç**
   - `http://localhost:5000` adresine git

## 📁 Proje Yapısı

```
basinda-bugun/
├── app.py                 # Flask ana uygulaması
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

### Haberler Kategorisini Değiştir
`app.py` dosyasında URL'i değiştir:
```python
# Şu anda: country=tr (Türkiye)
url = f"https://newsapi.org/v2/top-headlines?country=tr&apiKey={API_KEY}"

# Kategori eklemek için:
url = f"https://newsapi.org/v2/top-headlines?country=tr&category=business&apiKey={API_KEY}"
```

**Mevcut Kategoriler**: business, entertainment, general, health, science, sports, technology

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

## 📦 Kullanılan Teknolojiler

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: NewsAPI.org
- **İkonlar**: Font Awesome 6.4.0
- **Görseller**: Unsplash

## 🐛 Sorun Giderme

### "API Durumu: 401" Hatası
- NewsAPI anahtarı yanlış veya geçersiz
- `.env` dosyasındaki anahtarı kontrol et
- [newsapi.org](https://newsapi.org) adresinden yeni anahtar al

### Haberler Yüklenmiyorsa
- İnternet bağlantısını kontrol et
- NewsAPI'nin website'i açık mı kontrol et
- Tarayıcınızın konsol (F12) bölümünde hata mesajına bak

### CORS Hatası
- Frontend ve backend aynı domain'de çalışmalı
- `localhost:5000`'de çalıştığından emin ol

## 🚀 İleri Özellikler (Gelecek Güncellemeler)

- [ ] Kategori filtrelemesi
- [ ] Kaynak filtrelemesi
- [ ] Haber detay sayfası
- [ ] Favoriler/Kaydedilmiş haberler
- [ ] Arama geçmişi
- [ ] Pagination (sayfalama)
- [ ] Database entegrasyonu
- [ ] Admin paneli

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