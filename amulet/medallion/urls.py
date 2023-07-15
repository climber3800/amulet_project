from django.urls import path, include
from medallion import views
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static

app_name = 'amulet'

urlpatterns = [
    path('runes/rune_creation', views.rune_create_design, name='rune_create_design'),
    path('runes/rune_creation_two', views.rune_create_name, name='rune_create_name'),
    path('runes/rune_creation_three', views.rune_qualities, name='rune_qualities'),
    path('runes/rune_creation_four', views.rune_goals, name='rune_goals'),
    path('runes/rune_result', views.rune_result, name='rune_result'),
    path('runes/rune_matter', views.rune_material, name='rune_material'),
    path('runes/rune_stone', views.rune_final, name='sorry_page'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path("__debug__/", include("debug_toolbar.urls"))
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
