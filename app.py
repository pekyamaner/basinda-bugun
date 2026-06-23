from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

app = Flask(__name__)

# Güvenlik: API anahtarını .env dosyasından al
API_KEY = os.getenv("NEWSAPI_KEY", "d46733e2289149699b7789522b4507a7")

def haberleri_getir():
    """
    NewsAPI'den Türkiye'deki en güncel haberler bilgisini çek.
    Başarısız olursa yedek test verilerini döndür.
    """
    # Türkiye'deki en güncel manşetleri çeken NewsAPI adresi
    url = f"https://newsapi.org/v2/top-headlines?country=tr&apiKey={API_KEY}"
    
    try:
        cevap = requests.get(url, timeout=10)
        veri = cevap.json()
        
        # Eğer API anahtarı aktifse ve başarıyla veri döndüyse
        if veri.get("status") == "ok":
            makaleler = veri.get("articles", [])
            temiz_haberler = []
            
            for makale in makaleler:
                if makale.get("title") and makale.get("url"):
                    temiz_haberler.append({
                        "baslik": makale["title"],
                        "ozet": makale.get("description") or "Bu haber için kısa özet bulunmuyor.",
                        "kaynak": makale["source"].get("name", "Haber Merkezi"),
                        "link": makale["url"],
                        "resim": makale.get("urlToImage") or "https://via.placeholder.com/600x400?text=Haber+Gorseli+Yok"
                    })
            
            if temiz_haberler:
                print(f"✅ {len(temiz_haberler)} haber başarıyla yüklendi!")
                return temiz_haberler

        # Eğer API hata verdiyse (Örn: 401 Hatası), konsola hatayı yazdır
        print(f"❌ API Durumu: {veri.get('status')} - {veri.get('message', 'Bilinmeyen Hata')}")
        
    except requests.exceptions.Timeout:
        print("⚠️ Zaman Aşımı Hatası: API'ye bağlanırken zaman aşımı oluştu.")
    except requests.exceptions.ConnectionError:
        print("⚠️ Bağlantı Hatası: İnternet bağlantısını kontrol edin.")
    except Exception as e:
        print(f"⚠️ Bir hata oluştu: {e}")
    
    # 🚨 B PLANI (YEDEK VERİ): API anahtarın aktifleşene kadar sitenin 
    # boş kalmaması ve tasarımı görebilmen için simüle edilmiş haberler:
    print("⚠️ NewsAPI aktif değil veya hata verdi. Yedek test verileri yükleniyor...")
    return [
        {
            "baslik": "Teknoloji Dünyasında Büyük Gelişme: Yerli Yapay Zeka Modeli Tanıtıldı",
            "ozet": "Türkiye merkezli yazılım şirketi, Türkçe dil yapısını mükemmel şekilde çözen yeni nesil yapay zeka modelini canlı yayında duyurdu. Uzmanlar bu gelişmenin sektörde devrim yaratacağını belirtiyorlar.",
            "kaynak": "TechTürk",
            "link": "https://newsapi.org",
            "resim": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600"
        },
        {
            "baslik": "Merkez Bankası Yılın Son Faiz Kararını Açıkladı",
            "ozet": "Ekonomistlerin merakla beklediği faiz kararı bugün saat 14:00'te açıklandı. Karar sonrası piyasalarda hareketlilik başladı ve yatırımcılar düş��nüp taşımaya başladı.",
            "kaynak": "Finans Haber",
            "link": "https://newsapi.org",
            "resim": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600"
        },
        {
            "baslik": "Milli Takım Kritik Mücadeleden Galibiyetle Ayrıldı",
            "ozet": "Deplasmanda oynanan zorlu maçta millilerimiz son dakika golüyle 3 puanı hanesine yazdırmayı başardı. Teknik direktör maç sonrası oyuncuların gösterdiği çabadan dolayı övgüde bulundu.",
            "kaynak": "Spor Arena",
            "link": "https://newsapi.org",
            "resim": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=600"
        },
        {
            "baslik": "Eğitim Sisteminde Yeni Reformlar Açıklandı",
            "ozet": "Eğitim Bakanlığı tarafından yapılan açıklamada, eğitim sistemine getirilen yeni reformlar detaylı olarak açıklandı. Değişikliklerin eğitim kalitesini artıracağı düşünülüyor.",
            "kaynak": "Eğitim Haberleri",
            "link": "https://newsapi.org",
            "resim": "https://images.unsplash.com/photo-1427504494785-a7b06b8b5f49?w=600"
        },
        {
            "baslik": "Çevre Koruma Projesi Başarı Gösterdi",
            "ozet": "Geçen yıl başlatılan çevre koruma projesi, çevre kirliliğini azaltmada başarı gösterdi. Bilim insanları bu trendinin devamının çok önemli olduğunu vurguluyorlar.",
            "kaynak": "Çevre Perspektifi",
            "link": "https://newsapi.org",
            "resim": "https://images.unsplash.com/photo-1495567720989-cebfdc6d9053?w=600"
        },
        {
            "baslik": "Sağlık Sektöründe Yeni Hastanesinin Açılışı Yapıldı",
            "ozet": "Modern tesislerle donatılmış yeni hastane, bölge halkına hizmet vermeye başladı. Açılışta yetkili kişiler tesislerin Türkiye standartlarında olduğunu belirtttiler.",
            "kaynak": "Sağlık Bilgisi",
            "link": "https://newsapi.org",
            "resim": "https://images.unsplash.com/photo-1631217314831-e13b39d6ce1e?w=600"
        }
    ]

@app.route("/")
def ana_sayfa():
    """Ana sayfa - Haberler listesini göster"""
    canli_haberler = haberleri_getir()
    return render_template("index.html", haberler=canli_haberler)

if __name__ == "__main__":
    print("🚀 Flask sunucusu başlatılıyor...")
    print("📍 Adres: http://localhost:5000")
    print("💡 Tarayıcınızda açmak için yukarıdaki adrese gidin.")
    app.run(debug=True, port=5000)