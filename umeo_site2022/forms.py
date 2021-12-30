from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from users.models import User
#from .models import Message, Music, Good
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError

#https://blog.mtb-production.info/entry/2018/12/20/201057
#formsの役割

User = get_user_model()

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    
    error_messages = {
        'password_mismatch': _('入力した2つのパスワードが一致しません'),
    }
    password1 = forms.CharField(
        label=_("パスワード"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        #help_text=password_validation.password_validators_help_text_html(),
        help_text = _("<br>最低でも，8文字以上の長さ<br>数字のみのパスワードは禁止<br>他のサイトのパスワードや，個人情報に関係するパスワードにしないでください<br>")
    )
    password2 = forms.CharField(
        label=_("パスワード確認"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("<br>上と同じパスワードをもう一度記入してください"),
    )

    class Meta:
        model = User
        fields = ("username",)
        #field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

'''

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('body', )
        widgets = {
              'body': forms.Textarea(attrs={
              'class': 'form-control'
            }),
        }
        labels = {
            'body': 'メッセージ',
        }

class GoodForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = ('body', )
        widgets = {
              'body': forms.Textarea(attrs={
              'class': 'form-control'
            }),
        }
        labels = {
            'body': 'メッセージ',
        }


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('music', )

    
class GreetForm(forms.Form):
    name = forms.CharField(label='あなたの名前は？')

class StockForm(forms.Form):
    number = forms.IntegerField(label="個数")


'''