from django import forms
from apps.gallery.models import Photography

class PhotographyForms(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published', ]
        labels = {'datetime' : 'Date and time of publication'}

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'caption' : forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'photo' : forms.FileInput(attrs={'class': 'form-control'}),
            'date' : forms.DateInput(
                format='%m-%d-%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
                ),
                'user': forms.Select({'class': 'form-control'}),
        }