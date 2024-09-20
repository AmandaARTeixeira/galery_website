from django import forms

class LoginForm(forms.Form):
    name_login=forms.CharField(
        label='Username', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder' : 'Ex: John Wallace'
            }
        )
    )
    
    password = forms.CharField(
        label='Password', 
        required=True, 
        max_length=100, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Type your password'
            }
        )
    )
    
class RegisterForm(forms.Form):
    name_register = forms.CharField(
        label='Username', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder' : 'Ex: John Wallace'
            }
        )
    )

    email = forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
               'class': 'form-control',
               'placeholder' : 'johnwallace@example.com'
            }
        )
    ) 

    password1 = forms.CharField(
        label='Password', 
        required=True, 
        max_length=100, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Type your password'
            }
        )
    )  
    
    password2 = forms.CharField(
        label='Confirm your password', 
        required=True, 
        max_length=100, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Type your password again'
            }
        )
    )  