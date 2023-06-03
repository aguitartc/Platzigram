from django.contrib import admin
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('user', 'phone_number', 'website', 'picture')
    #editant aquest atribut, fem que en clicar user i phone_number ens porti al detaLL del user
    list_display_links = ('user', 'website')

    list_editable = ('phone_number','picture')
    search_fields = ('phone_number','picture')
    list_filter = ('user__is_active','user__is_staff')
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                ),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'biography')),
        })
    )