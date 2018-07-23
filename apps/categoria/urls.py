# from django.conf.urls import url, include
# from apps.categoria.views import index
#
# urlpatterns = [
#     url(r'^$', index, name="index"),
# ]

from django.urls import path
from apps.categoria.views import index

urlpatterns = [
    path('', index),
]
