from django.contrib import admin
from .models import Book  # import book model
from .models import CustomUser  # import the custom user model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    search_fields = ('title', 'author')

    list_filter = ('publication_year',)


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name',
         'phone_number', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number',
                       'date_of_birth', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


# register the book model
admin.site.register(Book, BookAdmin)
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
