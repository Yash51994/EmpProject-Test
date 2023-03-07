from django import forms
from.models import *

# class CustomerForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     address = forms.CharField(max_length=100)
#     products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)


class CustomerForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Customer
        fields = '__all__'
        