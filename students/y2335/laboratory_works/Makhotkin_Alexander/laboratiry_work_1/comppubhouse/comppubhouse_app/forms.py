from django import forms


class FeedbackForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

    text = forms.CharField(
        label='Текст',
        widget=forms.TextInput,
        min_length=5,
        max_length=300,
    )
    score = forms.DecimalField(
        label='Оценка (из 10)',
        widget=forms.NumberInput,
        max_digits=2,
        decimal_places=0,
        min_value=1,
        max_value=10,
    )


class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

    phone = forms.DecimalField(
        label='Телефон',
        widget=forms.NumberInput,
        max_digits=11,
        decimal_places=0,
        min_value=0,
        max_value=99999999999,
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput,
        max_length=80,
    )


class RegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput,
        max_length=30
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput,
        max_length=30
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput,
        max_length=30
    )
    email = forms.CharField(
        label='Эл. почта',
        widget=forms.TextInput
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        max_length=128
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput,
        max_length=128
    )


class PasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput,
        max_length=128
    )
    new_password = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput,
        max_length=128
    )
    new_password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput,
        max_length=128
    )


class ProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput,
        max_length=30
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput,
        max_length=30
    )
    email = forms.CharField(
        label='Эл. почта',
        widget=forms.TextInput
    )
    phone = forms.DecimalField(
        label='Телефон',
        widget=forms.NumberInput,
        max_digits=11,
        decimal_places=0,
        min_value=0,
        max_value=99999999999,
        required=False
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput,
        max_length=80,
        required=False
    )
