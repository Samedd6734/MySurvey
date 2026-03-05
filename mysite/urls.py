from django.contrib import admin
from django.urls import include, path
from django.contrib.admin.models import LogEntry
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


@csrf_protect
@staff_member_required
def clear_all_actions(request):
    if request.method == "POST":
        LogEntry.objects.filter(user=request.user).delete()
    return HttpResponseRedirect("/admin/")


@csrf_protect
@staff_member_required
def delete_action(request, pk):
    if request.method == "POST":
        LogEntry.objects.filter(pk=pk, user=request.user).delete()
    return HttpResponseRedirect("/admin/")


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("nested_admin/", include("nested_admin.urls")),
    path("admin-actions/clear-all/", clear_all_actions, name="clear_all_actions"),
    path("admin-actions/delete/<int:pk>/", delete_action, name="delete_action"),
]
