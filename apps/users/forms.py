from django import forms

"""
Forms for user authentication, including login and registration.

This module defines the forms used for user login and registration,
including field validation and custom error messages.
"""

class LoginForm(forms.Form):
    """
    Form for user login.

    This form collects the username and password for user authentication.

    Attributes:
        name_login: A CharField for the username.
        password: A CharField for the password.
    """
    name_login = forms.CharField(
        label='Username', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: John Wallace'
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
                'placeholder': 'Type your password'
            }
        )
    )


class RegisterForm(forms.Form):
    """
    Form for user registration.

    This form collects the username, email, and password for user registration,
    with validation to ensure the passwords match and the username is valid.

    Attributes:
        name_register: A CharField for the username.
        email: An EmailField for the user's email address.
        password1: A CharField for the password.
        password2: A CharField for confirming the password.
    """
    name_register = forms.CharField(
        label='Username', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: John Wallace'
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
                'placeholder': 'johnwallace@example.com'
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
                'placeholder': 'Type your password'
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
                'placeholder': 'Type your password again'
            }
        )
    )  

    def clean_name_register(self):
        """
        Validates the username.

        Checks that the username does not contain spaces.

        Returns:
            str: The cleaned username.

        Raises:
            ValidationError: If the username contains spaces.
        """
        name = self.cleaned_data.get('name_register', '').strip()

        if ' ' in name:
            raise forms.ValidationError('Can\'t have spaces inside username')
        else:
            return name
        
    def clean_password2(self):
        """
        Validates that the two password fields match.

        Compares password1 and password2 fields to ensure they match.

        Returns:
            str: The cleaned second password field.

        Raises:
            ValidationError: If the passwords do not match.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Passwords do not match')
            else:
                return password2