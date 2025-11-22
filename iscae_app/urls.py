from django.urls import path

from iscae_app.views import list_item, say_hello_json,html_page , edit_item , supprimer_item , create_item


urlpatterns = [
    path('say_hello/', say_hello_json),
    path('html_page/',html_page),
    path('list_item/',list_item , name='list_item'),
    path('edit_item/<int:id>/edit', edit_item , name='edit_item'),
    path('delete_item/<int:id>/delete', supprimer_item  , name='delete_item'),
    path('items/create/', create_item, name='create_item'),
]