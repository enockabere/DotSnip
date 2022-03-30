from  django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("post", views.post,name="post"),
    path("product/<int:pk>/", views.product,name="product"),
    path("entry/<int:pk>/", views.Entry,name="entry"),
    path("ViewPDF/<int:pk>/", views.ViewPDF,name="pdfs"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)