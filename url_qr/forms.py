from django import forms
from django.db import models
from .models import Url_QR


class UrlForm(forms.ModelForm):
    class Select(models.TextChoices):
        A = 'A', 'A'
        B = 'B', 'B'
        C = 'C', 'C'
        D = 'D', 'D'
        E = 'E', 'E'
        F = 'F', 'F'
        G = 'G', 'G'
        H = 'H', 'H'
        I = 'I', 'I'
        J = 'J', 'J'
        K = 'K', 'K'
        L = 'L', 'L'
        M = 'M', 'M'
        N = 'N', 'N'
        O = 'O', 'O'
        P = 'P', 'P'
        Q = 'Q', 'Q'
        R = 'R', 'R'
        S = 'S', 'S'
        T = 'T', 'T'
        U = 'U', 'U'
        V = 'V', 'V'
        W = 'W', 'W'
        X = 'X', 'X'
        Y = 'Y', 'Y'
        Z = 'Z', 'Z'
        
    generate = forms.BooleanField(initial=True, required=False)
    select_1 = forms.ChoiceField(choices=Select.choices)
    select_2 = forms.ChoiceField(choices=Select.choices)
    
    class Meta:
        model = Url_QR  # Correcting the attribute name to 'model'
        fields = ('url_long', 'url_short')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.fields:
            for fieldname in self.fields:
                if fieldname == 'generate':
                    self.fields[fieldname].widget.attrs = {'class': 'form-check-input'}
                    
                if fieldname == 'select_1' or fieldname == 'select_2':
                    self.fields[fieldname].widget.attrs = {'class': 'form-select1'}
                    
                if fieldname == 'url_long' or fieldname == 'url_short':
                    self.fields[fieldname].widget.attrs = {'class': 'form-control p-0'}
        else:
            raise ValueError('The field_names must be set')