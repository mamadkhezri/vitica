from django import forms

class CapsuleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)