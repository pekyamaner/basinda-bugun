from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

app = Flask(__name__)

# Güvenlik: API anahtarını .env dosyasından al
MEDIASTACK_API_KEY = os.getenv("MEDIASTACK_API_KEY", "ec437a7b7d79b819ef753263eba87c2d")

def haberleri_getir():
    """
    MediaStack API'den Türkiye'deki en güncel haberler bilgisini çek.
    Başarısız olursa yedek test verilerini döndür.
    """
    # Türkiye'deki haberler için MediaStack URL
    url = "http://api.mediastack.com/v1/news"
    
    params = {
        "access_key": MEDIASTACK_API_KEY,
        "countries": "tr",
        "limit": 20,
        "sort": "published_desc"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Eğer API başarılı bir cevap döndüyse
        if data.get("data"):
            articles = data.get("data", [])
            temiz_haberler = []
            
            for article in articles:
                if article.get("title") and article.get("url"):
                    temiz_haberler.append({
                        "baslik": article["title"],
                        "ozet": article.get("description") or "Bu haber için kısa özet bulunmuyor.",
                        "kaynak": article.get("source", "Haber Merkezi"),
                        "link": article["url"],
                        "resim": article.get("image") or "https://via.placeholder.com/600x400?text=Haber+Gorseli+Yok",
                        "tarih": article.get("published_at", "Bilinmiyor")
                    })
            
            if temiz_haberler:
                print(f"✅ {len(temiz_haberler)} haber başarıyla yüklendi (MediaStack)!")
                return temiz_haberler
        
        # Eğer API hata verdiyse
        error_message = data.get("error", {}).get("info", "Bilinmeyen hata")
        print(f"❌ MediaStack API Hatası: {error_message}")
        
    except requests.exceptions.Timeout:
        print("⚠️ Zaman Aşımı Hatası: API'ye bağlanırken zaman aşımı oluştu.")
    except requests.exceptions.ConnectionError:
        print("⚠️ Bağlantı Hatası: İnternet bağlantısını kontrol edin.")
    except Exception as e:
        print(f"⚠️ Bir hata oluştu: {e}")
    
    # 🚨 B PLANI (YEDEK VERİ): API anahtarın aktifleşene kadar sitenin 
    # boş kalmaması ve tasarımı görebilmen için simüle edilmiş haberler:
    print("⚠️ MediaStack aktif değil veya hata verdi. Yedek test verileri yükleniyor...")
    return [
        {
            "baslik": "Teknoloji Dünyasında Büyük Gelişme: Yerli Yapay Zeka Modeli Tanıtıldı",
            "ozet": "Türkiye merkezli yazılım şirketi, Türkçe dil yapısını mükemmel şekilde çözen yeni nesil yapay zeka modelini canlı yayında duyurdu. Uzmanlar bu gelişmenin sektörde devrim yaratacağını belirtiyorlar.",
            "kaynak": "TechTürk",
            "link": "https://mediastack.com",
            "resim": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600",
            "tarih": "2024-06-23"
        },
        {
            "baslik": "Merkez Bankası Yılın Son Faiz Kararını Açıkladı",
            "ozet": "Ekonomistlerin merakla beklediği faiz kararı bugün saat 14:00'te açıklandı. Karar sonrası piyasalarda hareketlilik başladı ve yatırımcılar düşünüp taşımaya başladı.",
            "kaynak": "Finans Haber",
            "link": "https://mediastack.com",
            "resim": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600",
            "tarih": "2024-06-23"
        },
        {
            "baslik": "Milli Takım Kritik Mücadeleden Galibiyetle Ayrıldı",
            "ozet": "Deplasmanda oynanan zorlu maçta millilerimiz son dakika golüyle 3 puanı hanesine yazdırmayı başardı. Teknik direktör maç sonrası oyuncuların gösterdiği çabadan dolayı övgüde bulundu.",
            "kaynak": "Spor Arena",
            "link": "https://mediastack.com",
            "resim": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=600",
            "tarih": "2024-06-23"
        },
        {
            "baslik": "Eğitim Sisteminde Yeni Reformlar Açıklandı",
            "ozet": "Eğitim Bakanlığı tarafından yapılan açıklamada, eğitim sistemine getirilen yeni reformlar detaylı olarak açıklandı. Değişikliklerin eğitim kalitesini artıracağı düşünülüyor.",
            "kaynak": "Eğitim Haberleri",
            "link": "https://mediastack.com",
            "resim": "https://images.unsplash.com/photo-1427504494785-a7b06b8b5f49?w=600",
            "tarih": "2024-06-23"
        },
        {
            "baslik": "Çevre Koruma Projesi Başarı Gösterdi",
            "ozet": "Geçen yıl başlatılan çevre koruma projesi, çevre kirliliğini azaltmada başarı gösterdi. Bilim insanları bu trendinin devamının çok önemli olduğunu vurguluyorlar.",
            "kaynak": "Çevre Perspektifi",
            "link": "https://mediastack.com",
            "resim": "https://images.unsplash.com/photo-1495567720989-cebfdc6d9053?w=600",
            "tarih": "2024-06-23"
        },
        {
            "baslik": "Sağlık Sektöründe Yeni Hastanesinin Açılışı Yapıldı",
            "ozet": "Modern tesislerle donatılmış yeni hastane, bölge halkına hizmet vermeye başladı. Açılışta yetkili kişiler tesislerin Türkiye standartlarında olduğunu belirtttiler.",
            "kaynak": "Sağlık Bilgisi",
            "link": "https://mediastack.com",
            "resim": "https://images.unsplash.com/photo-1631217314831-e13b39d6ce1e?w=600",
            "tarih": "2024-06-23"
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
    print("📰 API: MediaStack")
    app.run(debug=True, port=5000)
