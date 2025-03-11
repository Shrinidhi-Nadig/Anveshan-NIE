"""
URL configuration for ANVESHAN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ANVESHAN import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('anveshan/', views.anveshan),
    # path('course/<int:courseid>', views.course),
    path('', views.HomePage,name="home"),
    path('about/',views.About,name="about"),
    path('projects/',views.Projects,name="projects"),
    path('research/',views.Research,name="research"),
    path('events/',views.Events,name="events"),
    path('resourse/',views.Resourse,name="resourse"),
    path('blogs/',views.Blogs,name="blogs"),
    path('members/',views.Members,name="members"),
    path('contacts/',views.Contacts,name="contacts"),
    path('newsletter/',views.Newsletter,name="newsletter"),
    path('thankyou/',views.Thankyou),
    path('submitform/',views.Submitform,name="submitform"),
    path('calculator/',views.Calculator),
    path('newsdetails/<slug>',views.NewsDetails),
    path('subscribers/',views.Subscribers,name="subscribers"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)