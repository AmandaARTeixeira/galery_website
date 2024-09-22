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

    def clean_name_register(self):
        name = self.cleaned_data.get('name_register', '').strip()

        if ' ' in name:
            raise forms.ValidationError('Can\'t have spaces inside username')
        else:
            return name
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Passwords do not match')
            else:
                return password2