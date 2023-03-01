from django.contrib import admin
from . models import Gst_app

class Gst_appAdmin(admin.ModelAdmin):
  list_display = ("customer_name", "user_id", "password",)

admin.site.register(Gst_app, Gst_appAdmin)
