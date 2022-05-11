from django.urls import path
from django.contrib import admin
from API.views import detect
from django.http import HttpResponse


def home(request):
    return HttpResponse("Use Link --> http://127.0.0.1:8000/API/detect/{image1}/{image2}</br>Output Type --> {'verified': True, 'distance': 0.050999357752677166, 'threshold': 0.07, 'model': 'Dlib', 'detector_backend': 'mtcnn', 'similarity_metric': 'cosine', 'Confidance': 0.9328678344934921}")

urlpatterns = [
    # Examples:
    path(r'API/detect/', detect),
    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path(r'admin/', admin.site.urls),
    path('', home)
]