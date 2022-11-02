from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Bisha Theru Admin Site"
admin.site.index_title = "Design-Print-Fabricate"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("customerportal.urls")),
    
    
    path("glatexportal/", include("managementportal.urls")),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),

    path('orders/', include('orders.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)