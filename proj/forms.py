from django import forms

from .models import URL

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ('searchWord1', 'searchWord2', 'searchWord3', 'WordAndOR1', 'WordAndOR2', 'Country', 'Status', 'searchInventor1', 'searchInventor2', 
    'searchInventor3','InvAndOR1','InvAndOR2',)