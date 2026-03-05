# MySurvey Admin Panel i18n & Localization Plan

## 1. Objective
Fully translate the Django Admin panel (both standard and custom parts) into English and Turkish, and provide a seamless language switcher (EN/TR) adjacent to the theme toggle button.

## 2. Technical Strategy
- **Django Built-ins**: Utilize Django's native `i18n` framework (`settings.USE_I18N`, `LocaleMiddleware`, `django.conf.urls.i18n`). Django's admin is inherently translated; we only need to activate the engine and adapt our overwritten strings.
- **Template Adaptation**: Ensure all custom strings in `base_site.html` (like "Siteyi Gör", "Çıkış Yap") use `{% trans %}` tags instead of hardcoded text.
- **UI Language Switcher**: Embed a Django-compliant language selection form/button into the custom header, styled identically to the recent transparent flex/Lucide-based theme button.

## 3. Step-by-Step Orchestration

### Step 1: Backend Configuration (`backend-specialist`)
- **Action**: Modify `settings.py` and `urls.py`.
- **Details**: 
  - Define `LANGUAGES = [('en', 'English'), ('tr', 'Türkçe')]`.
  - Insert `'django.middleware.locale.LocaleMiddleware'` into `MIDDLEWARE` to persist the selected language in session/cookie.
  - Add `path('i18n/', include('django.conf.urls.i18n'))` in `mysite/urls.py` to handle language switching endpoints.

### Step 2: Frontend & UI Adaptation (`frontend-specialist`)
- **Action**: Update `templates/admin/base_site.html`.
- **Details**:
  - Replace hardcoded localized strings with `{% trans 'View site' %}`, `{% trans 'Log out' %}`, etc.
  - Integrate a Language Switcher button (similar to the Theme toggle) with an intuitive icon (e.g., Globe or flag/text) next to the theme switcher. 
  - Ensure styles do not break our new alignment.

### Step 3: Custom Translations (`database-architect` / `backend-specialist`)
- **Action**: Extract and compile messages.
- **Details**:
  - Configure `LOCALE_PATHS = [BASE_DIR / 'locale']`.
  - Execute `makemessages` for both Turkish and English languages.
  - Populate the `.po` files with any missing custom strings (like "MySurvey Admin", "Siteyi Gör").
  - Execute `compilemessages`.

### Step 4: Verification (`test-engineer`)
- **Action**: Confirm end-to-end functionality.
- **Details**:
  - Ensure changing languages translates both the admin menu (which is default Django) and our custom header.
  - Check UI boundaries (German length vs English length differences, RTL rules if any, though TR/EN is LTR).
