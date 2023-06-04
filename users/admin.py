#django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#models
from django.contrib.auth.models import User
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
    readonly_fields = ('created','modified')
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                ),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
                ),
        }),
        ('Metadata',{
            'fields': (
                ('created','modified'),
            )})
    )

class ProfileInline(admin.StackedInline):
    """Profile inline admin for users"""
    model = Profile
    can_delete = False 
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""    

    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)