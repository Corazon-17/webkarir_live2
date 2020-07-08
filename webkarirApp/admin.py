from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profil)
admin.site.register(Keahlian)
admin.site.register(Lowongan)

class lamaranModel(admin.ModelAdmin):
    list_display = ["__str__", "pelamar"]
    list_filter = ["lowongan"]
    search_fields = ["__str__", "pelamar"]
    list_per_page = 10

    class Meta:
        Model = Lamaran

admin.site.register(Lamaran, lamaranModel)
admin.site.register(Jurusan)

class magangModel(admin.ModelAdmin):
    list_display = ["__str__", "pemohon"]

    class Meta:
    	Model = Magang

admin.site.register(Magang, magangModel)