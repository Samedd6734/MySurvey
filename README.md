# 📊 MySurvey - Modern Django Polls App

Modern, şık tasarımlı ve interaktif bir anket/oylama uygulamasıdır. Klasik Django Polls uygulamasının **Glassmorphism** (cam efekti), **Bento Grid** tasarımı, özel animasyonlar, gelişmiş yüzdelik hesaplama çubukları ve uluslararasılaştırma (TR/EN dil desteği) ile baştan aşağı yeniden tasarlanmış halidir.

## 🌟 Öne Çıkan Özellikler & İşlevler
- **Modern UI / UX:** Tailwind CSS v4 ile geliştirilmiş tamamen özel Glassmorphism odaklı estetik arayüz.
- **Kusursuz Animasyonlar:** Anlık sonuç hesaplama çubukları, interaktif (sayarken dolan) barlar, canlı yayını betimleyen "Pulse Dot" geçiş efektleri.
- **Gelişmiş Anket Sonuçları:** Ankette en çok oyu alan seçenek için otomatik belirlenen **"⭐ Önde" (Leading)** rozetleri ile sonuçları analiz etmek oldukça keyifli.
- **Çoklu Dil Desteği:** Tek tıkla tamamen kesintisiz olarak Türkçe ve İngilizce (TR/EN) arası sayfa dil çevirisi.
- **Veri Tutarlılığı & Güvenlik:** Yarış koşulları (Race Condition) engellemek amaçlı yazılan backend mantığı ile aynı saniyede oy eklendiğinde dahi asla oy verisi kaybetmeyen asenkron sistem.
- **Güçlü Yetkilendirme:** Kayıt, giriş yap sayfaları ve kullanıcı dostu session mekanizmaları. Kullanıcıların güvenle anket kullanımları sağlanır.

## 🚀 Teknolojiler
- **Backend:** Python, Django
- **Frontend:** HTML5, Tailwind CSS, Vanilla JS
- **Veritabanı:** SQLite (Geliştirme Ortamı İçin)

---

## 💻 Kurulum (Local Development)

### 1- Repoyu Bilgisayarınıza İndirin (Clone)
Aşağıdaki git komutunu kullanarak veya üst kısımda bulunan **"Code" > "Download ZIP"** butonuna tıklayarak repoyu indirebilirsiniz.

```bash
git clone https://github.com/Samedd6734/MySurvey.git
cd MySurvey
```

### 2- Bağımlılıkları (Dependencies) Kurun
Django kurulu değilse, terminal / komut istemi üzerinden sanal bir ortama ya da doğrudan cihazınıza Django'yu kurun:
```bash
pip install django
```

*(İsteğe bağlı)* Projeniz için `virtualenv` kullanmanız daha iyi bir pratik olabilir:
```bash
python -m venv env
env\Scripts\activate
pip install django
```

### 3- Veritabanını Oluşturun (Migrations)
Projedeki veritabanı tablolarını (Kullanıcılar, Anketler) oluşturmak için aşağıdaki scriptleri sırasıyla çalıştırın:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4- Projeyi Çalıştırın
Tüm kurulumları tamamladıktan sonra server'ı başlatabilirsiniz:
```bash
python manage.py runserver
```
Ekranda herhangi bir hata yoksa, tarayıcınızdan şu adrese giderek uygulamayı açın: **[http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)**

## 🛡️ Admin Paneli & Yeni Anket Ekleme
Sisteme veritabanı arayüzü olan "Admin" paneline kendi anketlerinizi oluşturmak için bir (Geliştirici) hesabı yani `superuser` açmanız gerekir:

```bash
python manage.py createsuperuser
```

Komuttan sonra istenen **Kullanıcı adı**, **E-posta** ve **Şifre** bilgilerini belirleyin.
Ardından sistem paneline şuradan erişin: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

Buraya giriş yaptıktan sonra:
1. "Questions" (Sorular) sekmesinden yeni bir soru ekleyin.
2. Formda soru tarihini de dilediğiniz gibi ayarlayın.
3. Yine aynı form içinden o anket/soru için Seçenekleri (Choices) ekleyip kaydedin. Ekranınızdaki değişiklikler otomatik olarak uygulamanıza yansıyacaktır!

---

💡 *Eğer projeyi inceler veya geliştirirken bir hata bulursanız 'Issue' paneline ulaşmaktan çekinmeyin.*
