// ============================================
// HABER ARAMA VE FİLTRELEME İŞLEVLERİ
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    const searchBox = document.getElementById('searchBox');
    const filterBtn = document.getElementById('filterBtn');
    const newsGrid = document.getElementById('newsGrid');
    const newsCards = document.querySelectorAll('.news-card');

    // Arama kutusunda yazı yazıldığında haberları filtrele
    if (searchBox) {
        searchBox.addEventListener('input', function() {
            filterNews(this.value.toLowerCase());
        });
    }

    // Filtre butonuna tıklanınca
    if (filterBtn) {
        filterBtn.addEventListener('click', function() {
            const searchValue = searchBox.value.toLowerCase();
            if (searchValue.trim()) {
                filterNews(searchValue);
            } else {
                showAllNews();
                alert('Lütfen arama yapmak için bir kelime girin.');
            }
        });
    }

    // Enter tuşu basıldığında arama yap
    if (searchBox) {
        searchBox.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                filterBtn.click();
            }
        });
    }
});

/**
 * Haberları başlığa göre filtrele
 * @param {string} searchTerm - Aranacak kelime
 */
function filterNews(searchTerm) {
    const newsCards = document.querySelectorAll('.news-card');
    let visibleCount = 0;

    newsCards.forEach(card => {
        const title = card.getAttribute('data-title');
        
        if (title && title.includes(searchTerm)) {
            card.style.display = 'flex';
            card.style.animation = 'fadeIn 0.3s ease forwards';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });

    // Eğer sonuç bulunamazsa bildir
    if (visibleCount === 0) {
        showNoResults(searchTerm);
    }
}

/**
 * Tüm haberları göster
 */
function showAllNews() {
    const newsCards = document.querySelectorAll('.news-card');
    newsCards.forEach(card => {
        card.style.display = 'flex';
        card.style.animation = 'fadeIn 0.3s ease forwards';
    });
}

/**
 * Sonuç bulunamadı mesajını göster
 * @param {string} searchTerm - Aranan kelime
 */
function showNoResults(searchTerm) {
    const newsGrid = document.getElementById('newsGrid');
    
    // Eğer zaten bir "no-results" mesajı varsa kaldır
    const existingMessage = newsGrid.querySelector('.no-results-message');
    if (existingMessage) {
        existingMessage.remove();
    }

    // Yeni mesajı oluştur
    const noResultsDiv = document.createElement('div');
    noResultsDiv.className = 'no-news no-results-message';
    noResultsDiv.style.gridColumn = '1 / -1';
    noResultsDiv.innerHTML = `
        <i class="fas fa-search"></i>
        <p>"<strong>${escapeHtml(searchTerm)}</strong>" için sonuç bulunamadı.</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Lütfen farklı bir arama terimi deneyin.</p>
    `;

    // Tüm kartları gizle
    const newsCards = document.querySelectorAll('.news-card');
    newsCards.forEach(card => {
        card.style.display = 'none';
    });

    // Mesajı ekle
    newsGrid.appendChild(noResultsDiv);
}

/**
 * HTML karakterlerini escape et (XSS saldırısından korunmak için)
 * @param {string} text - Escape edilecek metin
 * @returns {string} Escape edilmiş metin
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ============================================
// SMOOTH SCROLL VE HOVER EFEKTLERİ
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================
// BAŞLANG + SAYFA YÜKLENDİĞİNDE EFEKTLER
// ============================================

window.addEventListener('load', function() {
    // Sayfadaki tüm resimlerin yüklenmesini bekle
    const images = document.querySelectorAll('.news-image');
    let loadedCount = 0;

    if (images.length === 0) {
        console.log('📰 Haber sitesi başarıyla yüklendi!');
        return;
    }

    images.forEach(img => {
        img.addEventListener('load', function() {
            loadedCount++;
            if (loadedCount === images.length) {
                console.log('✅ Tüm görseller başarıyla yüklendi!');
            }
        });

        img.addEventListener('error', function() {
            loadedCount++;
            console.warn('⚠️ Bir görsel yüklenemedi:', img.src);
            if (loadedCount === images.length) {
                console.log('✅ Görsel yükleme tamamlandı (bazı görseller yüklenemedi)');
            }
        });
    });
});

// ============================================
// DARKMODE TOGGLE (İSTEĞE BAĞLI)
// ============================================

function initDarkMode() {
    // Kullanıcının önceki tercihini kontrol et
    const savedMode = localStorage.getItem('darkMode');
    
    if (savedMode === 'enabled' || (!savedMode && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        enableDarkMode();
    }
}

function enableDarkMode() {
    document.body.classList.add('dark-mode');
    localStorage.setItem('darkMode', 'enabled');
}

function disableDarkMode() {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('darkMode', 'disabled');
}

// Sayfa yüklendiğinde dark mode ayarlarını kontrol et
document.addEventListener('DOMContentLoaded', function() {
    initDarkMode();
});

// ============================================
// CONSOLE MESAJLARI
// ============================================

console.log('%c🗞️ Basında Bugün - Haber Sitesi', 'color: #2563eb; font-size: 18px; font-weight: bold;');
console.log('%cNewsAPI tarafından desteklenmektedir.', 'color: #6b7280; font-size: 12px;');
console.log('%cFonksiyon: Türkiye\'den en güncel haberler', 'color: #10b981; font-size: 12px;');