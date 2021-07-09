from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum
from .models import CaixaStickers
from .forms import StickerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    stickers = CaixaStickers.objects.all()
    valor_total = CaixaStickers.objects.all().aggregate(valor_total = Sum('valor_total')).get('valor_total')
    quantidade_vendidos = CaixaStickers.objects.all().aggregate(quantidade_vendidos = Sum('quantidade_vendidos')).get('quantidade_vendidos')
    total_estoque = 468 - quantidade_vendidos
    stickers = reversed(stickers)

    if request.method == "POST":
        form = StickerForm(request.POST)
        if form.is_valid():
            form_data_venda = form.cleaned_data['data_venda']
            form_quantidade_vendidos = form.cleaned_data['quantidade_vendidos']
            form_valor_unidade = form.cleaned_data['valor_unidade']
            form_valor_total=form_quantidade_vendidos * form_valor_unidade
            newform = CaixaStickers(data_venda=form_data_venda ,quantidade_vendidos=form_quantidade_vendidos, valor_unidade=form_valor_unidade,valor_total=form_valor_total)
            newform.save()
            return redirect('index')
    else:
        form = StickerForm()

    return render(request, 'index.html', {
        'stickers': stickers, 
        'form':form, 
        'valor_total':valor_total, 
        'quantidade_vendidos':quantidade_vendidos, 
        'total_estoque':total_estoque
    })

@login_required
def excluir_venda(id_sticker):
    venda_stickers = CaixaStickers.objects.get(pk=id_sticker)
    venda_stickers.delete()
    return redirect('index')

def login(request):
    return render(request, 'login.html')
