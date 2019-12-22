from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from example import views

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = [
                  path('search_form', view=views.search_form, name='search_form'),
                  path('admin/lookups/', include(ajax_select_urls)),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
