from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя пользователя")
    age = forms.IntegerField(label="Возраст пользователя")
