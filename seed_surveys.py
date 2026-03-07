import os
import django
import random
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Survey, Question, Choice

def seed_data():
    now = timezone.now()
    Survey.objects.all().delete()
    print("Mevcut anketler veritabanından başarıyla temizlendi...")

    # Gerçekçi teknoloji, yazılım ve oyun sektörü anketleri ve mantıklı şıkları
    surveys = [
        {
            "title": "Oyun Motoru Çekişmesi",
            "desc": "2026 itibariyle bağımsız (Indie) ve AAA stüdyolarının en popüler oyun motoru tercihleri.",
            "is_expired": False,
            "questions": [
                {"q": "Bağımsız (Indie) oyun geliştirirken tercihiniz nedir?", "a": ["Unity (C#)", "Godot Engine (GDScript / C#)", "Unreal Engine (Blueprints / C++)", "GameMaker Studio", "Kendi Motorumu Yazıyorum", "Defold Engine", "Cocos2d-x"]},
                {"q": "Unreal Engine 5 hakkındaki görüşünüz nedir?", "a": ["AAA oyunlar için rakipsiz bir teknoloji", "Indie stüdyolar için karmaşık ve ağır", "Nanite/Lumen teknolojileri gerçekten çağ atlatıyor", "Gereksiz sistem gereksinimi istiyor, optimize değil"]},
                {"q": "2D oyunlar için sizce pazarın lideri kim olmalı?", "a": ["Açık ara Godot Engine", "GameMaker Studio 2", "Unity (Hala en iyi cross-platform)", "Phaser veya diğer JS kütüphaneleri"]}
            ]
        },
        {
            "title": "Kariyer Hedefi: Geleceğiniz",
            "desc": "Teknoloji sektöründe önümüzdeki 5 yıl içinde kendinizi kariyer olarak nerede görüyorsunuz?",
            "is_expired": False,
            "questions": [
                {"q": "Gelecek 5 yıl içindeki en büyük hedefiniz nedir?", "a": ["Senior / Lead Developer olmak", "Staff Engineer seviyesine çıkmak", "Engineering Manager (Yönetici) pozisyonu", "Kendi Start-up'ımı (Girişimimi) kurmak", "Danışman / Freelancer olarak devam etmek", "Tamamen alan değiştirmek (Tarım, Ticaret vs)"]},
                {"q": "Mesai saatleri dışında kendi projenizi veya kütüphanenizi geliştiriyor musunuz?", "a": ["Evet, sürekli uğraşıyorum (Günlük 1-2 saat)", "Sadece hafta sonları ayırabiliyorum", "Fikrim çok ama bir türlü vakit bulamıyorum", "Sadece iş saatlerinde kod yazarım, laptopu kapatırım"]}
            ]
        },
        {
            "title": "Front-End Dünyası ve JavaScript",
            "desc": "Hala bitmeyen savaş: Frontend dünyasının lideri kim olacak, Vanilla JS dönecek mi?",
            "is_expired": False,
            "questions": [
                {"q": "Yeni bir UI (Arayüz) kodlarken ilk tercih edeceğiniz kütüphane?", "a": ["React.js", "Next.js (React Framework)", "Vue.js", "Nuxt 3", "Svelte veya SvelteKit", "Angular", "Solid.js", "Sadece Vanilla JS + CSS"]},
                {"q": "Gelecekte pazar payı sizce nasıl şekillenecek?", "a": ["React ekosistemi %80'in üzerinde domine etmeye devam edecek", "Svelte hızından dolayı React'ten büyük bir pay çalacak", "Vue topluluğu Asya dışına taşıp herkesi saracak", "WebAssembly (WASM) gelince hepsi ölecek"]}
            ]
        },
        {
            "title": "Geliştirici İşletim Sistemleri (2026)",
            "desc": "Yazılım geliştiriciler kod yazarken ve debug yaparken hangi ortamı kullanıyor?",
            "is_expired": False,
            "questions": [
                {"q": "Mevcut birinci derece geliştirme donanım/isletim sisteminiz nedir?", "a": ["macOS (Apple Silicon M Serisi)", "Windows 11 (Oyun ve İş bir arada)", "Windows 11 + WSL2 (Terminal için Linux)", "Ubuntu / Mint tabanlı Debian sistem", "Arch / Fedora tabanlı ileri seviye Linux"]},
                {"q": "Geliştirmede favori Shell ve Terminal ortamınız hangisi?", "a": ["iTerm2 + Zsh (Oh-My-Zsh eklentisiyle)", "Windows Terminal + PowerShell 7", "Warp Terminal (Yapay Zeka destekli)", "Alacritty / Kitty (Ekstrem hız için)", "Standart Mac Terminali veya Gnome Bash"]}
            ]
        },
        {
            "title": "Yapay Zeka ve Yazılımcılar",
            "desc": "LLM kod asistanları işimizi elimizden mi alıyor yoksa saatlerimizi mi kurtarıyor?",
            "is_expired": False,
            "questions": [
                {"q": "Yapay zekanın yazılım sektöründeki ana etkisi sizce nedir?", "a": ["Üretkenliği 10 kata çıkaran sıradan bir asistan aracı", "Junior geliştiricilerin iş bulmasını imkansızlaştıran bir tehdit", "Sadece basit kazanımları/boilerplate kodarı yazabiliyor, çok abartılıyor", "Gelecekte yazılım mühendisine gerek bırakmayacak seviyeye gelecek"]},
                {"q": "Kod asistanı kullanırken verilerinizin gizliliğinden ne kadar endişelisiniz?", "a": ["Çok endişeliyim, şirket (Enterprise) repolarını ve dosyaları asla paylaşmam", "Umurumda değil, yeter ki kodumu hızlı ve hatasız yazsın", "Sadece kendi sunucumdaki Open-Source (Mistral/Llama) modelleri kullanıyorum"]},
                {"q": "IDE veya tarayıcıda kullandığınız favori kod LLM'i hangisi?", "a": ["Claude 3.5 Sonnet (Yazılımda en iyisi)", "GPT-4o (Genel ve güvenilir)", "DeepSeek (Açık kaynak efsanesi)", "Mistral tabanlı özelleştirilmiş modeller", "GitHub Copilot (Standart olarak)"]}
            ]
        },
        {
            "title": "Veri Bilimi (Data Science) Modası",
            "desc": "Veri Bilimi ve ML eğitimleri patlarken sahada gerçekten ne kullanılıyor?",
            "is_expired": True,
            "questions": [
                {"q": "Veri manipülasyonu (Data Wrangling) için favori kütüphaneniz?", "a": ["Pandas (Klasik olan)", "Polars (Çok daha hızlı olan)", "Dask / PySpark (Büyük veri için)", "Saf (Raw) SQL yazarak veritabanında çözerim"]},
                {"q": "Model eğitim süreçleri için ana tercihiniz?", "a": ["PyTorch (Akademik + Endüstriyel lider)", "TensorFlow / Keras (Eski dost)", "Sadece Scikit-Learn (Temel regresyonlar)", "XGBoost / LightGBM (Gradient algoritmalar)"]}
            ]
        },
        {
            "title": "Cloud (Bulut) Sağlayıcı Savaşları",
            "desc": "Start-up (Girişim) ve Kurumsalların altyapı barındırma tercih ve maliyetleri.",
            "is_expired": False,
            "questions": [
                {"q": "Girişim (Start-up) projelerinizi yayına alırken ilk tercih edeceğiniz Cloud?", "a": ["Amazon Web Services (AWS - Çok güçlü ama karışık)", "Google Cloud Platform (GCP - Temiz Arayüz)", "Microsoft Azure ('.NET ekosistemi için')", "DigitalOcean / Hetzner (Ucuz ve saf VPS)", "Vercel / Netlify / Heroku (Backend düşünmek istemiyorum)"]},
                {"q": "Bulut maliyetleri hakkındaki düşünceniz?", "a": ["Çok pahalı ve sürekli gizli bant genişliği ücretleri çıkıyor", "Yönetilen hizmetler (Managed Services) için fiyata kesinlikle değer", "Start-up kredi paketleri olmazsa erişilemez ve yakıcı", "Kendi ofisime (On-Premise) fiziksel sunucu almayı tercih ederim"] },
                {"q": "Veritabanını nerede barındırmayı güvenli ve performanslı buluyorsunuz?", "a": ["AWS RDS / GCP Cloud SQL gibi Managed servislerde", "Supabase / Firebase gibi BaaS sistemlerinde", "Kendim kiraladığım ucuz bir VPS içinde Docker veya doğrudan kurarak"]}
            ]
        },
        {
            "title": "E-Spor ve Rekabetçi Takım Oyunları",
            "desc": "İş stresini atmak (ya da artırmak) için akşamları tercih edilen aksiyon dozajı yüksek oyunlar.",
            "is_expired": False,
            "questions": [
                {"q": "Arkadaşlarla düzenli olarak girdiğiniz takım bazlı rekabetçi oyun nedir?", "a": ["Valorant", "Counter-Strike 2", "League of Legends", "Dota 2", "Rocket League", "Rainbow Six Siege", "Vaktim oldukça oyun oynamıyorum"]},
                {"q": "Single-player / Hikaye odaklı oyunlara bakış açınız nedir?", "a": ["Sadece kaliteli RPG ve açık dünya hikaye oyunları oynarım (Witcher 3, RDR2 vb.)", "İndirimde bulunca alır, vakit buldukça 1-2 saat oynarım", "Rekabet hissi vermediği için çok sıkılırım, hiç oynamam", "Sadece bağımsız (Indie) sanatsal tarzı oyunları seviyorum"]}
            ]
        },
        {
            "title": "Web Uygulamaları: SPA vs SSR",
            "desc": "Single Page Application dönemi bitiyor mu? Server Side Rendering yeniden mi doğdu?",
            "is_expired": False,
            "questions": [
                {"q": "Kurduğunuz yeni web uygulamalarında genelde hangi yaklaşımı benimsiyorsunuz?", "a": ["Geleneksel SSR (Django, Laravel, Rails)", "Tam SPA (Sadece React/Vue ve ayrı REST API)", "Modern Meta-Framework (Next.js, Nuxt - SSR + Hydration)"]},
                {"q": "Performans açısından en sancılı metrik (Web Vitals) sizce hangisi?", "a": ["LCP (Largest Contentful Paint - İlk çizim süresi)", "CLS (Cumulative Layout Shift - Ekranın kayması)", "INP (Interaction to Next Paint - Tıklama gecikmesi)"]}
            ]
        },
        {
            "title": "Ekran ve Monitör Düzenleri",
            "desc": "Kod yazarken boyun fıtığı olmamak ve odaklanmak için kullanılan donanımlar.",
            "is_expired": True,
            "questions": [
                {"q": "Günlük çalışmanızda nasıl bir monitör konfigürasyonunuz var?", "a": ["Sadece laptop ekranım, her yere taşıyorum", "1 adet harici 24/27 inç standart monitör", "2 adet harici monitör (Biri dik olabilir)", "34 inç veya daha büyük tek bir UltraWide (Geniş) monitör"]},
                {"q": "Göz sağlığı ve karanlık mod (Dark Mode) hakkında ne düşünüyorsunuz?", "a": ["Her uygulamada karanlık mod şart, beyaz ışık kör ediyor", "Kod yazarken karanlık, web/okuma yaparken aydınlık mod", "Her zaman aydınlık (Light) mod kullanıyorum"]}
            ]
        },
        {
            "title": "No-Code & Low-Code Platformları",
            "desc": "Geleneksel yazılımcıları tehdit eden hazır araçlar kalıcı olacak mı?",
            "is_expired": True,
            "questions": [
                {"q": "İş akışınızda hiç no-code/low-code araç kullandınız mı?", "a": ["Evet, sürekli ve büyük projelerde (Bubble, Webflow vs.)", "Basit admin panelleri veya formlar için kullandım (Retool vs.)", "Hayır, tamamen geleneksel programlama ile kod yazarım", "Asla kullanmam, kontrolü %100 ele almayı seviyorum"]},
                {"q": "Sizce No-Code araçları karmaşık (Complex) iş mantıklarını çözebilir mi?", "a": ["Platform ölçeklenmeye başlayınca kesinlikle tıkanır ve çöker", "Belirli bir sınıra kadar (%80 işi) harika bir şekilde çözebiliyor", "Zamanla her türlü karmaşık kodu görselleştirerek çözebilecek duruma gelecekler"]}
            ]
        },
        {
            "title": "IDE Savaşları: VS Code vs JetBrains",
            "desc": "Terminalden IDE arayüzlerine, yıllardır süregelen kod editörü çekişmesi.",
            "is_expired": False,
            "questions": [
                {"q": "Günlük kullanımda pazar liderliğiniz ve tercihiniz kime ait?", "a": ["Açık ara Visual Studio Code (Ücretsiz ve Eklentileri efsane)", "JetBrains ailesi (IntelliJ IDEA, WebStorm, PyCharm vb.)", "Cursor (AI tabanlı VSCode forku - Yeni nesil)", "Vim / Neovim tabanlı klavye odaklı ortam", "Klasik Visual Studio (C# ve .NET için Enterprise)"]},
                {"q": "IDE seçimindeki en belirleyici ve vazgeçilmez etmen sizin için nedir?", "a": ["Düşük donanım tüketimi, hız ve akışkanlık", "Aklınıza gelebilecek her şey için bir eklenti (Plugin) olması", "Kurar kurmaz (Out-of-the-box) her ayarının tam ve hazır olması", "Mükemmel çalışan ve kodu anlayan AI entegrasyonu (Chat, Tab autocomplete)"]}
            ]
        },
        {
            "title": "Veritabanı Kararı: SQL vs NoSQL",
            "desc": "Sunucu-Veritabanı ilişkilerinde projenin kaderini çizen ilk karar.",
            "is_expired": False,
            "questions": [
                {"q": "Yeni bir girişime / projeye başlarken ana veritabanı (Primary DB) varsayılanınız nedir?", "a": ["PostgreSQL (Relational güç pazarın kralı)", "MySQL / MariaDB (Klasik ve güvenli)", "MongoDB (Doküman tabanlı rahatlık)", "Firebase / Firestore (Baas hızı, kurulumsuz)", "SQLite (Sadece prototip yaparken)"]},
                {"q": "NoSQL (Json tabanlı) veritabanlarını kodlarken hangi noktada pişman veya mutlu oluyorsunuz?", "a": ["Tablo şemaları sürekli değiştiği için esnekliğinden çok mutluyum", "Karmaşık Join'ler (birleştirme) gerektiğinde performans süründürüyor ve pişman ediyor", "Sadece Session / Cache logları için mükemmel", "Sistem daüssü darmadağın oldu, Relation veri her zaman güvenlidir"]}
            ]
        },
        {
            "title": "Component Library vs Tailwind",
            "desc": "CSS yazmak hamallık mı yoksa Tailwind gereksiz bir yığın mı?",
            "is_expired": False,
            "questions": [
                {"q": "Yeni proje hazırlarken UI kütüphanesi olarak ne yüklersiniz?", "a": ["Shadcn UI (Style üzerine Headless tasarım)", "Material UI / Joy UI (Eski ve güvenli Google hissi)", "Chakra UI / Mantine (Geliştirici dostu pre-defined komponentler)", "Ant Design / Bootstrap (Klasik panel devleri)", "Komponent kullanmam, sıfırdan sadece Tailwind CSS ile yazarım", "Hiçbiri, SCSS/CSS Module ile sıfırdan oluştururum"]},
                {"q": "Açık kaynak kütüphane (Component Library) kullanmanın sizce en büyük dezavantajı nedir?", "a": ["Yaptığınız sitenin jenerik, ruhsuz ve 'Herkesin yaptığı diğer template' gibi durması", "Bundle (Paket) boyutunun gereksiz seviyede artarak sitenin ağırlaşması", "Müşteri özel bir tasarım (Custom) istediğinde komponenti eğip bükmenin ölümcül zorluğu", "Bence hiçbir dezavantajı yok, ciddi hız ve efor kazandırıyor"]}
            ]
        },
        {
            "title": "Version Control Kültürü (GitHub/Git)",
            "desc": "Dağınık kodları toparlama ve iş arkadaşlarını çıldırtmama sanatı.",
            "is_expired": True,
            "questions": [
                {"q": "Git Commit mesajlarını atarken nasıl bir kuralınız var?", "a": ["'fix(auth)', 'feat(ui)' gibi kesin kurallı Conventional Commits", "Kuralsız ama kısa ve anlaşılır bir cümle şeklinde (Added new login button)", "Çok acelem varsa sadece 'update', 'fixed error', 'wip' vb. yazıp geçerim", "Terminalime kurduğum yapay zeka CLI tool'una otomatik yazdırırım"]},
                {"q": "Büyük şirket repolarındaki en büyük kabusunuz nedir?", "a": ["Sistem dosyalarını bozan ve geri alınması zor çaresiz Merge Conflict'ler yaşamak", "Ana (Production) branch'e yanlışlıkla test/hatalı kodu 'force push' veya 'merge' yapmak", "Kimsenin gözden geçirmediği (Review atmadığı) Pull Request'lerin dağ gibi birikmesi", "Eski 'feature-login-2023' vb. branchleri silmeyi unutup projenin branch çöplüğüne dönmesi"]}
            ]
        },
        {
            "title": "Siber Güvenlik Farkındalığı 101",
            "desc": "Normal bir yazılım okyanusunda geliştiriciler güvenlik önlemlerini ne kadar ciddiye alıyor?",
            "is_expired": False,
            "questions": [
                {"q": "Web uygulamalarında 2026 itibariyle en sık karşılaşılan/en tehlikeli açık sizce nedir?", "a": ["Eskimeyen klasikler: SQL, Command ve NoSQL Injection zafiyetleri", "Broken Authentication (MFA eksikliği ve çalınan Session'lar)", "Siteler arası betik çalıştırma: Cross-Site Scripting (XSS)", "Ortasıdaki Adam (MitM) ve zayıf/kırılmış algoritmalar", "Log4j benzeri: Kullanılan npm/pip paketlerinden gelen Supply Chain (Tedarik zinciri) enfeksiyonları"]},
                {"q": "Çok gizli Environment (.env) API şifrelerini nasıl yönetiyorsunuz?", "a": ["Ayrı bir env dosyam var asla git'e atmam, sistem yöneticisi VPS'de manuel sağlar", "Modern ve şifreli kasalar (Doppler / AWS Secrets / HashiCorp Vault) kullanırım", "Sadece local'da çalışır, Vercel/Render vb. panellerine girerim", "Yanlışlıkla github repo'ma Public pushlayıp sonra Commit history temizlemeye uğraşırım :)"]}
            ]
        },
        {
            "title": "Konteyner Mimarileri ve Devops",
            "desc": "Docker ve Kubernetes gibi yük tevzi teknoloijleri.",
            "is_expired": False,
            "questions": [
                {"q": "Docker komutlarına ve ekosistemine ne seviyede hakimsiniz?", "a": ["Sadece github'dan aldığım docker-compose up/down'u çalıştıracak kadar", "Frontend/Backend repom için temiz, güvenli ve distroless image (Dockerfile) yazabilecek uzmanlıkta", "Cluster'lara kadar yük çıkaran Kubernetes master / CKA seviyesinde", "Kullanmaya üşeniyorum, dosyaları rarlayıp cPanel/FTP kullanarak sunucuya atıyorum"]},
                {"q": "Sizce Kubernetes her şirket / startup projesi için gerekli ve kurması şart mıdır?", "a": ["Hayır, büyük bir mühendislik eforu çöpe gidiyor, sadece global ölçekte dev bir trafilke lazımdır", "Evet, yavaştan gelecekte herkesin uygulayacağı basit deployment standardı haline gelecek", "Eski nesilde kalacak, artık her şey Serverless yapılarına evrilecek ve yönetimi devredeceğiz"]}
            ]
        },
        {
            "title": "Geliştiricilerin Kahve & Mola Ritüeli",
            "desc": "Masa başında tüketilen odaklayıcı içecekler ve ekrana molasız bakmak.",
            "is_expired": False,
            "questions": [
                {"q": "Günde ortalama kaç kupa sert kahve veya ek kafeinli içecek (Enerji/Kola) tüketirsiniz?", "a": ["Sıfır. Sadece çay ve bol su bardağı (Kafein kullanmam)", "Sabah ayılmak ve öğlen odaklanmak için 1-2 kupa", "Masanın olmazsa olmazı, 3-4 kupa garanti", "Code yettiği kadar: 5 ve üzeri (Artık hissetmiyorum)"]},
                {"q": "Çalışırken / Kod yazarken konsantrasyon atıştırmalık tercihiniz nedir?", "a": ["Konsantreyi bozar ve klavye/fare berbat olur, hiçbir şey yemem", "Zihin açsın diye kuru yemiş (Ceviz, badem, fıstık tarzı)", "Tatlı/Glukoz ihtiyacından Cips, çikolata, meyveli kraker", "Kesilmiş taze mevsim meyveleri tabakta"]}
            ]
        },
        {
            "title": "Açık Kaynak (Open Source) PR Katkısı",
            "desc": "Her şirket açık kaynak kütüphaneleri sömürüyor, peki kimler geri besliyor?",
            "is_expired": False,
            "questions": [
                {"q": "Kariyeriniz boyunca hiç popüler bir açık kaynak projeye PR (Pull Request) kabul ettirdiniz mi?", "a": ["Evet, sürekli issue çözen aktif bir maintainer/contributor statüsündeyim", "Sadece dokümantasyon imla hatası veya bir-iki ufak bug-fix yaması yolladım", "Hayır, okuyorum ama eklenti yapacak kadar o cesareti hiç içimde hissetmedim", "Hayır, vakit nakittir niye başkasının projesine bedava kod yazayım?"]},
                {"q": "GitHub (vektörel yeşil çimenler) / GitLab profilinizin dolu olması bir mülakatta cidden işe yarar mı?", "a": ["Kesinlikle, referansım olarak IK'dan ziyade Tech Lead'in çok ilgisini çekiyor, avantaj sağlıyor", "Bazen soruluyor, güzel durması fena değil ancak asıl olay algoritmik mülakat çözümünde", "Hiç kimse bakmıyor, tek kıstas size verdikleri PDF test ödevini ne kadar iyi teslim ettiğiniz"]}
            ]
        },
        {
            "title": "API Standartları: REST mi GraphQL mi?",
            "desc": "Backend geliştiricilerin ön yüze veri iletirken kurduğu iletişim protokolleri.",
            "is_expired": False,
            "questions": [
                {"q": "Tarayıcı (Front) ile Sunucu (Backend) iletişimi için ağırlıklı ana mimari tercihiniz nedir?", "a": ["RESTful (JSON standartlarında en oturmuş, HTTP metotlarına tam saygı duyan yaklaşım)", "GraphQL (Sadece ihtiyacın olan alanı çek, limitleri aşan güçlü API)", "gRPC / Protokol Buffers (Mikroservisler arası devasa hız ve binary aktarım)", "tRPC veya sadece SSR içi doğrudan Data fonksiyonları (Aletsiz uçuş)", "Hala SOAP / XML kullanarak eski sistemlere entegre oluyorum"]},
                {"q": "Eğer web uygulamanız devasa bir anlık trafiğe girerse Backend dil performansınız sizce ne kadar kurtarır?", "a": ["Go / Rust yazıyoruz, 100 bin Request atsanız memory 50mb zar zor oynar (Kurtarır)", "C# / Java gibi enterprise ekosistemleri zaten kurumsal, çok güçlü (Kurtarır)", "Node.js (Bun / Express) veya Python (FastAPI/Django) asenkron çalışır ve gayet yeterli olur", "Tasarım/Mimarim (Database sorgularım) o kadar leş ki dil ne olursa olsun sistem felç olurdu"]}
            ]
        },
        {
            "title": "Mobil Mimarileri: Native ve Cross Savaşları",
            "desc": "2026'da hala Swift veya Kotlin yazan var mı? Çapraz platform gücü sınırlarını aştı mı?",
            "is_expired": False,
            "questions": [
                {"q": "Yeni bir unicorn girişiminin mobil uygulamasını projelendireceksiniz. Teknoloji tercihiniz?", "a": ["Flutter (Dart - UI kiti kusursuz ve Google arkasında)", "React Native (Web tabanlı React bilgi birikimini anında telefona çevir)", "Tamamen Native, 2 ayrı ekip: Swift (iOS) ve Kotlin (Android) ayrı ayrı derlenecek", "PWA (Progressive Web App) yeterli, kimse uygulama indirmek istemiyor, tarayıcıda çalışsın"]},
                {"q": "Çapraz platform (Cross-Platform) teknolojileri neden Native'in tahtını sarstı?", "a": ["Eskisi gibi çok yavaş (WebView benzeri) değiller, %90 Native performansındalar", "İki ayrı koda (Kotlin/Swift) ayrı developer maaşı vermek firmalara gereksiz pahalılaştı", "JavaScript / TS bilen web geliştiricilerini kolayca mobil dünyaya aktarabilme lüksü", "Yukarıdakilerin hepsi (Ticari + Performans ikilisinin optimum noktası)"]}
            ]
        },
        {
            "title": "Sistematik Test: TDD ve QA Gerçekleri",
            "desc": "Test-Driven Development kulağa ne kadar harika gelse de gerçekten yapan kimse var mı?",
            "is_expired": False,
            "questions": [
                {"q": "Gerçek şirket (Production) ortamında Code Coverage / Testler nasıl işliyor?", "a": ["Strict TDD Uyguluyoruz (Testi fail ettirmeden kodun bir satırı bile production'a çıkamaz)", "Mantıklı bir Coverage tutulur (%70-80), abartmadan iş yapan fonksiyonlar yazılır", "Sadece login/payment gibi paranın döndüğü aşırı kritik modüllere ara sıra test eklenir", "Start-up / MVP kafası: Kod derleniyorsa tamamdır, test ederek yavaşlayamayız, QA ekibi falan da yok biz deneriz"]},
                {"q": "Hatalı bir sürüme (Deployment) karşı en büyük zırh olarak neye güvenirsiniz?", "a": ["Ayrıntılı Unit ve Modül testlerine (Sırf fonksiyon düzeyinde)", "Front-End E2E Otomatik UI Robotlarına (Cypress, Playwright, Selenium ile fare tıklamalarına)", "Staging (Test) sunucusunda tüm ekibin Cuma günü denemesine :)", "Zırhımız yok, hata çıkarsa hızlıca v1.0.1 hotfix çıkıp yangını patron görmeden söndürüyoruz"]}
            ]
        },
        {
            "title": "Mental Sağlık (Burnout) vs Yazılımcılık",
            "desc": "Hiç durmadan değişen 40 javascript kütüphanesine, yapay zekaya ve yetişmeyen deadline'lara olan dayanıklılığımız.",
            "is_expired": True,
            "questions": [
                {"q": "Kariyeriniz boyunca hiç ciddi bi Burnout (Mesleki Tükenmişlik Sentromu) yaşadınız mı?", "a": ["Evet, hastanelik edecek kadar yoğun stresti, sektör değiştirmeyi veya uzun mola vermeyi bile düşündüm", "Şu an tam o evredeyim, hiçbir şeye motive olamıyorum, kod görmek istemiyorum", "Bazen o çizgide hissedip 1 hafta tatil/kafa dağıtmayla kolay toparlıyorum", "Hayır, hiç yaşamadım. Oyun oynar gibi puzzle çözüyorum bence bu dünya muazzam"]},
                {"q": "Klavyeden uzaklaşıp deşarj olmak için haftasonu kaçışınız genelde ne tarafa?", "a": ["Doğa / Kamp Ateşi / Bisiklet / Motorsiklet vs", "Deşarj vs hikaye; Bilgisayar/Konsol oyunlarıyla başka sanal dünyalara dalmak", "Ağırlık kaldırmak (Fitness), Yoga veya koşu", "Ahzap veren kodlarımı silip, o akşam 'yeni' muazzam bir side-project'e (iş dışı) sıfırdan mimari başlamak"]}
            ]
        },
        {
            "title": "Sıfır Gün Zafiyetleri / Olay Yönetimi",
            "desc": "Production (Canlı sistem) çöktüğünde panik odasında (War Room) davranışlar.",
            "is_expired": False,
            "questions": [
                {"q": "Uygulamanız (Server) gece saat 03:00'te çöktü. Alarm cihazınıza geldi. İlk kural?", "a": ["Log/Traceback araçlarına (Datadog/Sentry) dalıp derhal Bug'ın kök nedenini analiz ederim", "Önce bir önceki sağlıklı Release/Commit'e hızlı Rollback yapar (geri sarar), sistemi ayaklandırır sabah analiz ederim", "Bana giren çıkan yok, CTO'yu veya Nöbetçiyi uyandırırım", "Zaten server çökünce Docker kendi kendine Auto-Restart atarak sorunu sabahlık hallediyor"]},
                {"q": "Devasa bir veri sızıntısı haberi / Data breach farkedildi, yapılması gereken?", "a": ["Suçu başka mikroservise atmaya çalışırım :)", "Hemen veritabanı portlarını internete kapatır ve password reset politikasına sokulur."]}
            ]
        },
         {
            "title": "Toplantı (Meeting) Sendromları",
            "desc": "Geliştiricilerin iş yaptığı süreden fazlasını Zoom toplantılarında harcaması.",
            "is_expired": False,
            "questions": [
                {"q": "Şirket içi Daily Scrum/Stand-up toplantılarınız kaç dakika sürüyor ve ne kadar verimli?", "a": ["Tam 10-15 dakika içinde harika bir koordinasyonla bitiyor (Scrum guide gibi)", "30 Düşünülen ama 1 saat süren, Product Owner'in destan anlattığı anlamsız toplantı", "Toplantıya girip kamerayı kapatıp mikrofon kapalıyken yanda kod yazmaya devam ediyorum", "Toplantı yok. Slack/Discord üzerinden asenkron metinlerle iletişim kuruyoruz (Mükemmel)"]},
                {"q": "Kod yazamama probleminiz %x oranda saptırıcılar; Toplantı ve Slack mesajları kaynaklı mı?", "a": ["Kesinlikle %80 bu yüzden. Biri dürtünce Context-switch yapıp asıl kod aklımdan uçuyor", "Planlama (Toplantı) aslında koddan (Uygulamadan) daha değerli, vakit kaybı değil.", "Açık ofis gürültüsü hariç odaklanabildiğimde bir sorun olmuyor"]}
            ]
        }
    ]

    # Herkesin katılım sağladığı ve organik görünen bir anket
    for item in surveys:
        pub_date = now - timedelta(days=random.randint(5, 60))
        
        if item["is_expired"]:
            # Süresi 1 ila 25 gün önce geçmiş
            end_date = now - timedelta(days=random.randint(1, 25))
        else:
            # Süresi 1 ila 4 yıl sonra geçecek
            end_date = now + timedelta(days=random.randint(365, 4*365))
            
        survey = Survey.objects.create(
            title=item["title"],
            description=item["desc"],
            pub_date=pub_date,
            end_date=end_date
        )

        for q_data in item["questions"]:
            question = Question.objects.create(
                survey=survey,
                question_text=q_data["q"],
                pub_date=pub_date
            )
            
            for option in q_data["a"]:
                # Etkileşim oyları çok az (Mantıklı ve kısıtlı bir topluluk/forum havası): 5 - 120 arası total
                votes = random.randint(5, 120)
                Choice.objects.create(
                    question=question,
                    choice_text=option,
                    votes=votes
                )

    from django.db.models import Sum
    toplam_oy = Choice.objects.aggregate(s=Sum("votes"))["s"] or 0
    aktif_anket = Survey.objects.filter(end_date__gt=now).count()
    
    print(f"✓ Toplam {len(surveys)} adet zengin, mantıklı sektörel ve donanım anketleri başarıyla oluşturuldu!")
    print(f"✓ Aktif Anket Sayısı: {aktif_anket} | Kapalı Anket Sayısı: {len(surveys) - aktif_anket}")
    print(f"✓ Toplam Gerçekçi Sistem Oyu (İnteraktip Oylama Toplamı): {toplam_oy:,} oy.")

if __name__ == "__main__":
    seed_data()
