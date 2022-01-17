from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.forms import UserChangeForm, UserCreationForm
from account.models import User, aws_account


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'major_type', 'phone', 'is_admin')
    list_filter = ('major_type', 'is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'major_type', 'phone')}),
        ('Permissions', {'fields': ('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'major_type', 'phone')
        }),
    )
    search_fields = ('email', 'name', 'phone')
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(aws_account)
