from django.contrib import admin

#models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts admin."""

    list_display = ('user' , 'title', 'photo', 'created', 'modified', 'profile')
    #editant aquest atribut, fem que en clicar user i phone_number ens porti al detaLL del user
    list_display_links = ('user',)

    list_editable = ('title', 'photo', 'profile')
    search_fields = ('user__username', 'user__email', 'title')
    
    readonly_fields = ('created','modified')
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user'), 'profile',
                ),
        }),
        ('Info post', {
            'fields': (
                ('title', 'photo'),
                ),
        }),
        ('Metadata',{
            'fields': (
                ('created','modified'),
            )})
    )
