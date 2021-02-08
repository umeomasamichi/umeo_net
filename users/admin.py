from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User
  
  
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
  
  
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
  
  
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'bairitsu', 'umeop', 'stock', 'running_days')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'date_mylogin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'umeop', 'bairitsu', 'stock', 'running_days')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)
  
  
admin.site.register(User, MyUserAdmin)