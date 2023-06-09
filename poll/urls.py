"""
URL configuration for poll project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from questions.views import question_detail,save_question_result, login_view, register_view, dashboard, create_poll, see_answers  

urlpatterns = [
    path('' , login_view , name="login"),
    path('register/' , register_view , name="register_view"),
    path('dashboard/' , dashboard , name="dashboard"),
     path('create_poll/' , create_poll , name="create_poll"),
     path('see_answers/' , see_answers , name="see_answers"),
    path('question/<question_uid>/' , question_detail , name="question_detail"),
    path('api/save_question_result/' , save_question_result),
    path('admin/', admin.site.urls),
]
