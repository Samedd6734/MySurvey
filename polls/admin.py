import nested_admin
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.utils.translation import gettext_lazy as _

from .models import Choice, Question, Survey


# ─── Nested Inlines: Choice → Question → Survey ───────────────────────────

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 3  # Varsayılan 3 şık textboxı aç
    exclude = ["votes"]  # Admin oy sayısını değiştiremesin

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1  # Sayfa açıldığında 1 soru textboxı hazır gelsin
    fields = ["question_text"]
    inlines = [ChoiceInline]
    show_change_link = False

# ─── Survey Admin ──────────────────────────────────────────────────────────

class SurveyAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "description"]}),
        ("Tarih Ayarları (Zamanlama)", {
            "fields": [("pub_date", "end_date")],
            "description": "Anketin başlangıç tarihini seçin. Bitiş tarihi zorunlu değildir, eğer boş bırakırsanız anket süresiz olarak açık kalır."
        }),
    ]
    inlines = [QuestionInline]
    list_display = ["title", "pub_date", "end_date", "question_count", "was_published_recently"]
    list_filter = ["pub_date", "end_date"]
    search_fields = ["title"]

    class Media:
        js = ("polls/js/admin_override.js",)
        css = {
            "all": ("polls/css/admin_override.css",)
        }

    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = _("question count")

    def was_published_recently(self, obj):
        return obj.was_published_recently()
    was_published_recently.short_description = _("published recently?")
    was_published_recently.boolean = True


# ─── LogEntry (Recent Actions) Admin ──────────────────────────────────────

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user", "action_time", "content_type"]
    list_filter = ["user"]
    readonly_fields = [
        "user", "content_type", "object_id", "object_repr",
        "action_flag", "change_message",
    ]

    def has_add_permission(self, request):
        return False

    def log_deletion(self, request, obj, object_repr):
        # Logları silerken tekrar silindi diye log atılmasını engeller
        pass

    def log_change(self, request, object, message):
        pass

    def log_addition(self, request, object, message):
        pass


# ─── Register ─────────────────────────────────────────────────────────────
# Only Survey and LogEntry shown in sidebar — Questions accessed via Survey inline

admin.site.register(Survey, SurveyAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
