from .models import Messages1, Messages2, Messages3, Messages4, Messages5
from django.forms import ModelForm, TextInput, Textarea


class MessagesForm1(ModelForm):
    class Meta:
        model = Messages1
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите своё имя'
        }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }


class MessagesForm2(ModelForm):
    class Meta:
        model = Messages2
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите своё имя'
        }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }


class MessagesForm3(ModelForm):
    class Meta:
        model = Messages3
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите своё имя'
        }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }


class MessagesForm4(ModelForm):
    class Meta:
        model = Messages4
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите своё имя'
        }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }


class MessagesForm5(ModelForm):
    class Meta:
        model = Messages5
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите своё имя'
        }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }