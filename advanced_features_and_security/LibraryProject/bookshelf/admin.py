from django.contrib import admin
from .models import Book  # import book model
from .models import CustomUser  # import the custom user model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    search_fields = ('title', 'author')

    list_filter = ('publication_year',)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
         'last_name', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

    search_fields = ('username', 'email')
    ordering = ('username',)


# register the book model
admin.site.register(Book, BookAdmin)
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
