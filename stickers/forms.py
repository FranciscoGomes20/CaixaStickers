from django import forms
from .models import CaixaStickers

class StickerForm(forms.ModelForm):
    class Meta:
        model = CaixaStickers
        fields = ('data_venda', 'quantidade_vendidos', 'valor_unidade')
        widgets = {
            'quantidade_vendidos': forms.NumberInput(
                attrs={'type': 'number', 'name': 'amount', 'id': 'description', 'placeholder': 'Quantidade vendidos'}),
            'valor_unidade': forms.NumberInput(
                attrs={ 'type':'number', 'id': 'amount', 'name': 'amount', 'placeholder': '0,00' }),
            'data_venda': forms.DateInput( 
                attrs={ 'type':'date', 'id':'date', 'name':'date' }),
        }
