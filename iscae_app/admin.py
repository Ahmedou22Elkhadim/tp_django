from django.contrib import admin

from iscae_app.models import CustomUser , Item

admin.site.register(CustomUser),
admin.site.register(Item)
