from django.urls import path

from iscae_app.views import list_item, say_hello_json,html_page


urlpatterns = [

    path('say_hello/', say_hello_json),
    path('html_page/',html_page),
    path('list_item/',list_item)
]