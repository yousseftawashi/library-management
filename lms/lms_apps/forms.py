
from django import forms
from . models import book, category




class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name_category']

        widgets = {
            'name_category' :forms.TextInput(attrs={'class':'form-control'}),
         }
         
class bookform(forms.ModelForm):
    class Meta:
        model = book
        fields = [
            'name_book',
            'author',
            'potho_book',
            'potho_author',
            'pages',
            'price',
            'rentel_price_day',
            'rental_period',
            'total_rental',
            'status',
            'category',
        ]
        widgets = {
             'name_book':forms.TextInput(attrs={'class':'form-control'}),
             'author':forms.TextInput(attrs={'class':'form-control'}),
             'potho_book':forms.FileInput(attrs={'class':'form-control'}),
             'potho_author':forms.FileInput(attrs={'class':'form-control'}),
             'pages':forms.NumberInput(attrs={'class':'form-control'}),
             'price':forms.NumberInput(attrs={'class':'form-control'}),
             'rentel_price_day':forms.NumberInput(attrs={'class':'form-control', 'id':'rentelprice'}),
             'rental_period':forms.NumberInput(attrs={'class':'form-control', 'id':'rentaldays'}),
             'total_rental':forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
             'status':forms.Select(attrs={'class':'form-control'}),
             'category':forms.Select(attrs={'class':'form-control'}),
        }