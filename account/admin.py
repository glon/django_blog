from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserPorfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('phone',)

admin.site.register(UserProfile, UserPorfileAdmin)


