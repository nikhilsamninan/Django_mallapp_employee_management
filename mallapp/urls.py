"""malldatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path,include
from .import views as v

urlpatterns = [
    path('',v.home,name='homepage'),
    path('userhome/',v.userhome,name='userhome'),
    path('modelinsert/',v.modelform,name='modelform'),
    path('userregform/',v.registrationfn,name='regform'),
    path('userlogin/',v.loginfn,name='login'),
    path('userlogout/',v.logoutfn,name='logout'),
    path('update/<int:id>/',v.update,name='update'),
    path('delete/<int:id>/',v.delete,name='delete'),
    path('imageupload/',v.uploading,name='imageupload')
]
