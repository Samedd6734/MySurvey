# 📊 MySurvey - Modern & Interactive Django Survey Application

**MySurvey**, standart bir anket uygulamasından çok daha fazlasıdır. Django'nun klasik "Polls" öğretisini temel alarak, üzerine **modern mimari prensiplerini**, **ileri seviye veritabanı optimizasyonlarını** ve **2025'in en güncel tasarım trendlerini** inşa eden profesyonel bir çalışmadır.

Bu projede, anketlerin sadece tek bir sorudan ibaret olduğu kısıtlı yapı yıkılmış; soruların **Anket (Survey)** grupları altında toplandığı, çok aşamalı ve akıcı bir kullanıcı deneyimi hedeflenmiştir.

---

## 🔥 Geliştirmeler & Fark Yaratan Özellikler

Bu proje, standart "Django Polls" uygulamasından şu yönleriyle ayrılır:

### 1. Survey (Anket) Mimarisi
*   **Çoklu Soru Desteği:** Artık her soru bağımsız değildir; sorular belirli bir "Survey" çatısı altında toplanır. Kullanıcı bir ankete başladığında tüm soruları sırayla yanıtlayarak ilerler.
*   **Navigasyon Mantığı:** Sorular arasında "İleri" ve "Geri" butonları ile dinamik geçiş imkanı sunulur.

### 2. İleri Seviye Veri Güvenliği & Performans
*   **Yarış Koşullarına (Race Condition) Karşı Koruma:** Oy verme işlemi sırasında oluşabilecek veri kayıplarını engellemek için Django'nun `F()` ifadeleri ve `transaction.atomic()` özelliği kullanılmıştır.
*   **Optimize Sorgular:** `SelectRelated` ve `PrefetchRelated` mantığı ile veritabanı yükü minimize edilmiş, `Exists` ve `OuterRef` gibi ileri seviye ORM teknikleri ile kullanıcı bazlı filtrelemeler (anketi tamamlayanları ayıklama vb.) SQL seviyesinde optimize edilmiştir.

### 3. Modern Glassmorphism UI (Tailwind v4)
*   **Tasarım Dili:** Tamamen **Tailwind CSS v4**'ün yeni özellikleri kullanılarak modern bir "Glassmorphism" (Cam efekti) deneyimi oluşturuldu.
*   **Bento Grid:** Home sayfasında anketler, şık ve okunaklı bir Bento Grid yapısıyla sunulur.
*   **Dinamik Animasyonlar:** Sonuç çubuklarının dolma animasyonları, "Önde" (Leading) olan cevabın parlayan rozeti gibi mikro etkileşimler geliştirilmiştir.

### 4. Akıllı Oturum & Katılım Takibi
*   **Katılım Kontrolü:** `UserSurveyParticipation` modeli ile bir kullanıcının hangi anketi bitirdiği takip edilir. Tamamlanan anketler ana sayfada görsel olarak ayırt edilir ve tekrar oy kullanımı engellenir.

---

## 🛠️ Teknolojik Altyapı

*   **Çekirdek:** Python 3.10+ & Django 6.0.3
*   **Stil:** Tailwind CSS v4 (Glassmorphism Effects & Bento Grid Layout)
*   **Logic:** Vanilla JavaScript & Django Template Engine
*   **Yönetim:** `django-nested-admin` (Tek ekranda tüm anket, soru ve seçenekleri yönetme yeteneği)
*   **I18n:** Türkçe ve İngilizce dinamik dil desteği.

---

## 🚀 Kurulum ve Çalıştırma (Step-by-Step)

Projeyi GitHub'dan indiren birinin tüm özelliklerle birlikte çalıştırması için şu adımları takip etmesi yeterlidir:

### 1. Repoyu Yerel Ortamınıza Çekin
```bash
git clone https://github.com/Samedd6734/MySurvey.git
cd MySurvey/mysite
```

### 2. İzole Bir Geliştirme Ortamı Oluşturun (Venv)
Bağımlılıkların sisteminizle çakışmaması için mutlaka bir sanal ortam kullanın:
```powershell
python -m venv venv
# Aktifleştirme (Windows):
.\venv\Scripts\Activate
# Aktifleştirme (Mac/Linux):
source venv/bin/activate
```

### 3. Gereksinimleri Yükleyin
Proje için gerekli olan tüm kütüphaneleri tek komutla kurun:
```bash
pip install -r requirements.txt
```

### 4. Veritabanını Hazırlayın
Modelleri veritabanı tablolarına dönüştürün:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Yönetici Hesabı Oluşturun
Anket ve soru girişi yapabilmek için kendi admin profilinizi oluşturun:
```bash
python manage.py createsuperuser
```

### 6. Uygulamayı Başlatın
```bash
python manage.py runserver
```
🚀 Uygulama hazır! Tarayıcınızdan **[http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)** adresine giderek deneyimlemeye başlayın.

---

## 📁 Proje Yapısı Hakkında Notlar

*   `mysite/`: Genel ayarlar ve projenin kalbi.
*   `polls/`: Asıl iş mantığının, modellerin ve şık tasarımların bulunduğu uygulama klasörü.
*   `locale/`: Uygulamanın Türkçe ve İngilizce dilleri arasındaki köprüsü.

---

💡 *Geliştirmelerimle ilgili sorularınız veya önerileriniz için Issue açmaktan veya bana ulaşmaktan çekinmeyin.*
