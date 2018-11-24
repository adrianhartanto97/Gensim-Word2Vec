"""gensim_word2vec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello_world),
    path('submit_model_path', views.submit_model_path, name= 'submit_model_path'),
    path('submit_most_similar', views.submit_most_similar, name= 'submit_most_similar'),
    path('submit_similarity', views.submit_similarity, name= 'submit_similarity'),
    path('submit_dmatch', views.submit_dmatch, name= 'submit_dmatch'),
    path('submit_analogy', views.submit_analogy, name= 'submit_analogy'),
    path('submit_training', views.submit_training, name= 'submit_training')
]
