from django.shortcuts import render
from django.shortcuts import redirect
from .models import CaixaStickers
from .forms import StickerForm

# Create your views here.
def index(request):
    stickers = CaixaStickers.objects.all()
    stickers = reversed(stickers)
    
    if request.method == "POST":
        form = StickerForm(request.POST)
        if form.is_valid():
            new_data_venda = form.cleaned_data['data_venda']
            new_quantidade_vendidos = form.cleaned_data['quantidade_vendidos']
            new_valor_unidade = form.cleaned_data['valor_unidade']
            new_valor_total = new_quantidade_vendidos * new_valor_unidade
            new_form = CaixaStickers(data_venda=new_data_venda, quantidade_vendidos=new_quantidade_vendidos, valor_unidade=new_valor_unidade, valor_total=new_valor_total)
            new_form.save()
            return redirect('index')
    else:
        form = StickerForm()
    return render(request, 'index.html', {'stickers': stickers, 'form':form })

def excluir_venda(request, id_sticker):
    venda_stickers = CaixaStickers.objects.get(pk=id_sticker)
    venda_stickers.delete()
    return redirect('index')
