from  django import forms
class SearchFormu(forms.Form):
    query=forms.CharField(label='search',max_length=100)