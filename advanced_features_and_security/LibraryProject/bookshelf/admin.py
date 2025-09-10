from django.contrib import admin
from .models import Book  # import book model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# custom admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    search_fields = ('title', 'author')

    list_filter = ('publication_year',)


# register the book model
admin.site.register(Book, BookAdmin)
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_dispaly = ['email', 'username', 'date_of_birth', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
         'fields': ('username', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        # Added date_joined here
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
