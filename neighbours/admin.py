from django.contrib import admin
from .models import Neighbour,Profile
# Register your models here.
class NeigborAdmin(admin.ModelAdmin):
    filter_horizontal=('Neighbour',)
admin.site.register(Neighbour)
admin.site.register(Profile)
