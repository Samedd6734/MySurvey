import os
import polib

for lang in ['tr', 'en']:
    path = os.path.join('locale', lang, 'LC_MESSAGES')
    os.makedirs(path, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────
#  KURAL: İlk harf büyük, geri kalanı küçük (Sentence case)
#  Django verbose_name için msgid hâlâ küçük (convention),
#  ancak msgstr (Türkçe görünen metin) sentence case olacak.
# ─────────────────────────────────────────────────────────────────────────
translations = [

    # ── Özel Header ─────────────────────────────────────────────────────
    ("MySurvey Admin",                          "MySurvey Admin"),
    ("Welcome",                                 "Hoş geldin"),
    ("View Site",                               "Siteyi gör"),
    ("Change Password",                         "Şifre değiştir"),
    ("Log out",                                 "Çıkış yap"),
    ("Are you sure you want to delete all recent actions?",
                                                "Tüm son işlemler silinsin mi?"),
    ("Clear All",                               "Tümünü temizle"),
    ("Delete",                                  "Sil"),

    # ── Model verbose_name (msgid küçük = Django convention) ────────────
    ("survey",                                  "Anket"),
    ("surveys",                                 "Anketler"),
    ("polls",                                   "Anketler"),
    ("question",                                "Soru"),
    ("questions",                               "Sorular"),
    ("choice",                                  "Seçenek"),
    ("choices",                                 "Seçenekler"),
    ("user",                                    "Kullanıcı"),
    ("users",                                   "Kullanıcılar"),
    ("group",                                   "Grup"),
    ("groups",                                  "Gruplar"),
    ("log entry",                               "Günlük kaydı"),
    ("log entries",                             "Günlük kayıtları"),

    # ── Model field verbose_name ─────────────────────────────────────────
    ("title",                                   "Başlık"),
    ("description",                             "Açıklama"),
    ("publication date",                        "Yayın tarihi"),
    ("date published",                          "Yayın tarihi"),
    ("question text",                           "Soru metni"),
    ("question count",                          "Soru sayısı"),
    ("published recently?",                     "Yakın zamanda yayınlandı mı?"),
    ("choice text",                             "Seçenek metni"),
    ("votes",                                   "Oy sayısı"),

    # ── İşlem Butonları ──────────────────────────────────────────────────
    ("Add",                                     "Ekle"),
    ("View",                                    "Görüntüle"),
    ("Change",                                  "Düzenle"),
    ("Save",                                    "Kaydet"),
    ("Save and add another",                    "Kaydet ve yeni ekle"),
    ("Save and continue editing",               "Kaydet ve düzenlemeye devam et"),
    ("Cancel",                                  "İptal"),
    ("Search",                                  "Ara"),
    ("Filter",                                  "Filtrele"),
    ("Reset",                                   "Sıfırla"),
    ("Actions",                                 "İşlemler"),
    ("Go",                                      "Uygula"),
    ("Delete selected",                         "Seçilenleri sil"),
    ("Select all",                              "Tümünü seç"),
    ("Clear selection",                         "Seçimi temizle"),
    ("Remove",                                  "Kaldır"),

    # ── Ana Sayfa / Navigasyon ───────────────────────────────────────────
    ("Site administration",                     "Site yönetimi"),
    ("Recent actions",                          "Son işlemler"),
    ("My actions",                              "İşlemlerim"),
    ("None available",                          "Mevcut değil"),
    ("Unknown content",                         "Bilinmeyen içerik"),
    ("You don't have permission to view or edit anything.",
                                                "Bu içeriği görüntüleme veya düzenleme yetkiniz yok."),
    ("Models in the %(name)s application",      "%(name)s uygulamasındaki modeller"),
    ("Home",                                    "Ana sayfa"),
    ("Administration",                          "Yönetim"),
    ("Toggle navigation",                       "Navigasyonu aç/kapat"),

    # ── Sayfa Başlıkları ─────────────────────────────────────────────────
    ("Add %s",                                  "%s ekle"),
    ("Change %s",                               "%s düzenle"),
    ("Select %s to change",                     "Düzenlenecek %s seç"),
    ("Select %s to view",                       "Görüntülenecek %s seç"),
    ("Add another %s",                          "Başka %s ekle"),
    ("Are you sure?",                           "Emin misiniz?"),
    ("Yes, I'm sure",                           "Evet, eminim"),
    ("No, take me back",                        "Hayır, geri dön"),
    ("Please correct the error below.",         "Lütfen aşağıdaki hatayı düzeltin."),
    ("Please correct the errors below.",        "Lütfen aşağıdaki hataları düzeltin."),
    ("The %(name)s \"%(obj)s\" was added successfully.",
                                                "%(name)s \"%(obj)s\" başarıyla eklendi."),
    ("The %(name)s \"%(obj)s\" was changed successfully.",
                                                "%(name)s \"%(obj)s\" başarıyla güncellendi."),
    ("The %(name)s \"%(obj)s\" was deleted successfully.",
                                                "%(name)s \"%(obj)s\" başarıyla silindi."),

    # ── Tarih & Filtreler ────────────────────────────────────────────────
    ("Any date",                                "Herhangi bir tarih"),
    ("Today",                                   "Bugün"),
    ("Past 7 days",                             "Son 7 gün"),
    ("This month",                              "Bu ay"),
    ("This year",                               "Bu yıl"),
    ("All",                                     "Tümü"),
    ("Date hierarchy",                          "Tarih hiyerarşisi"),
    ("All dates",                               "Tüm tarihler"),
    ("By %s",                                   "%s'e göre"),

    # ── Geçmiş / History ─────────────────────────────────────────────────
    ("History",                                 "Geçmiş"),
    ("View on site",                            "Sitede görüntüle"),
    ("Date/time",                               "Tarih/saat"),
    ("Action",                                  "Eylem"),
    ("object history",                          "Nesne geçmişi"),
    ("This object doesn't have a change history.",
                                                "Bu nesnenin değişiklik geçmişi yok."),

    # ── Giriş / Auth ─────────────────────────────────────────────────────
    ("Log in",                                  "Giriş yap"),
    ("Log in again",                            "Tekrar giriş yap"),
    ("Username",                                "Kullanıcı adı"),
    ("Password",                                "Şifre"),
    ("Forgotten your password or username?",    "Şifrenizi veya kullanıcı adınızı mı unuttunuz?"),
    ("Password change",                         "Şifre değiştir"),
    ("Password change successful",              "Şifre başarıyla değiştirildi"),
    ("Documentation",                           "Belgeler"),

    # ── Boolean ─────────────────────────────────────────────────────────
    ("True",                                    "Evet"),
    ("False",                                   "Hayır"),
    ("Yes",                                     "Evet"),
    ("No",                                      "Hayır"),
    ("Unknown",                                 "Bilinmiyor"),
    ("N/A",                                     "Yok"),

    # ── Diğer ────────────────────────────────────────────────────────────
    ("(None)",                                  "(Yok)"),
    ("Empty",                                   "Boş"),
    ("Required.",                               "Zorunlu alan."),
    ("Enter a valid value.",                    "Geçerli bir değer girin."),
    ("This field is required.",                 "Bu alan zorunludur."),
    ("Please enter a correct %(username)s and password.",
                                                "Lütfen doğru %(username)s ve şifre giriniz."),
    ("Select",                                  "Seç"),
    ("Object ID",                               "Nesne kimliği"),
    ("Content type",                            "İçerik türü"),
    ("Action time",                             "İşlem zamanı"),
    ("Change message",                          "Değişiklik mesajı"),
    ("Action flag",                             "İşlem türü"),
    ("%(count)d selected",                      "%(count)d seçildi"),
]

# ─── Turkish .po / .mo ────────────────────────────────────────────────────
tr_po = polib.POFile()
tr_po.metadata = {
    'Project-Id-Version': '1.0',
    'Language': 'tr',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
    'Plural-Forms': 'nplurals=2; plural=(n != 1);',
}
seen = set()
for msgid, msgstr in translations:
    if msgid not in seen:
        tr_po.append(polib.POEntry(msgid=msgid, msgstr=msgstr))
        seen.add(msgid)

tr_po.save('locale/tr/LC_MESSAGES/django.po')
tr_po.save_as_mofile('locale/tr/LC_MESSAGES/django.mo')
print(f"TR: {len(seen)} giriş derlendi.")

# ─── English .po / .mo ────────────────────────────────────────────────────
en_po = polib.POFile()
en_po.metadata = {
    'Project-Id-Version': '1.0',
    'Language': 'en',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
    'Plural-Forms': 'nplurals=2; plural=(n != 1);',
}
for msgid, _ in translations:
    en_po.append(polib.POEntry(msgid=msgid, msgstr=msgid))

en_po.save('locale/en/LC_MESSAGES/django.po')
en_po.save_as_mofile('locale/en/LC_MESSAGES/django.mo')
print(f"EN: {len(translations)} giriş derlendi.")

print("\n✅ Tüm çeviri dosyaları başarıyla derlendi!")
