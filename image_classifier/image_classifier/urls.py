from django.contrib import admin
from django.urls import path, include  # Certifique-se de ter importado include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('classifier.urls')),  # Inclua as URLs do aplicativo 'classifier'
]
