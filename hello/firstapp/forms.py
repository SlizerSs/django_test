from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя пользователя",
                           min_length=3,
                           max_length=20,
                           widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст пользователя",
                             min_value=1,
                             max_value=100,
                             widget=forms.NumberInput(attrs={
                                 "class": "myfield"}))
