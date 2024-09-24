from django import forms
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class ContactForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
        )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email

class LoginForm(forms.Form):
    nome = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirm senha', widget=forms.PasswordInput)

    def clean_username(self):
        nome = self.cleaned_data.get('nome')
        qs = Usuario.objects.filter(nome=nome)
        if qs.exists():
            raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
        return nome
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Usuario.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse email já existe, tente outro!")
        return email

    def clean(self):
        data = self.cleaned_data
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')  # Correção aqui
        if senha != senha2:
            raise forms.ValidationError("As senhas informadas devem ser iguais!")
        return data