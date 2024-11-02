"""
URL configuration for core project.

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

"""
from django.contrib import admin

## step1: 匯入return 要用的套件
from django.http import HttpResponse
from django.urls import path


## step2: 定義function (用view), 要帶request 參數
## django 處理邏輯的角色用VIEW
def message_view(request):
    return HttpResponse("Hello World!")


## step3: 定義進入點(user 訪問路徑)及對應的function
urlpatterns = [
    path("admin/", admin.site.urls),
    path("message/", message_view),
]

"""
from django.contrib import admin
from django.urls import path

from first.views import message_view, say_hello, say_hello_template, say_hello_to

urlpatterns = [
    path("admin/", admin.site.urls),
    path("message/", message_view),
    path("say_hello/", say_hello),
    path("say_hello_template/", say_hello_template),
    path("say_hello_to/<str:name>", say_hello_to),
]
