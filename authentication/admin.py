from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_select_related = ('profile',)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'country', 'created_at')
    list_filter = ('gender', 'country', 'notifications_enabled')
    search_fields = ('user__username', 'user__email', 'phone_number', 'city')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'address', 'city', 'state', 'country', 'postal_code')
        }),
        ('Personal Information', {
            'fields': ('profile_picture', 'bio', 'date_of_birth', 'gender')
        }),
        ('Professional Information', {
            'fields': ('occupation', 'organization')
        }),
        ('Preferences', {
            'fields': ('notifications_enabled', 'email_notifications')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
