from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя пользователя",
                           min_length=2,
                           max_length=20)
    age = forms.IntegerField(label="Возраст пользователя",
                             min_value=1,
                             max_value=120)
    email = forms.EmailField(label="Электронный адрес")
    advert = forms.BooleanField(
        label="Согласны получать рекламу",
        required=False)
