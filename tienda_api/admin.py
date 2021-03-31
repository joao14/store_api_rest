from django.contrib import admin
from tienda_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Client)
admin.site.register(models.Store)
admin.site.register(models.Product)
admin.site.register(models.Album)
admin.site.register(models.Track)