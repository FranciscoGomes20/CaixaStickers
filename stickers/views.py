from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum
from .models import CaixaStickers, TotalStickers
from .forms import StickerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    stickers = CaixaStickers.objects.filter().order_by("-pk")
    valor_total = CaixaStickers.objects.all().aggregate(valor_total = Sum('valor_total')).get('valor_total')
    total_vendidos = CaixaStickers.objects.all().aggregate(quantidade_vendidos = Sum('quantidade_vendidos')).get('quantidade_vendidos')

    try:
        total_estoque = TotalStickers.objects.latest("pk")
    except TypeError:
        total_estoque = 0

    try:
        total_estoque = total_estoque.stickers_total - total_vendidos
    except TypeError:
        total_estoque = total_estoque.stickers_total

    if request.method == "POST" and "venda" in request.POST:
        form = StickerForm(request.POST)
        if form.is_valid():
            form_data_venda = form.cleaned_data['data_venda']
            form_quantidade_vendidos = form.cleaned_data['quantidade_vendidos']
            form_valor_unidade = form.cleaned_data['valor_unidade']
            form_valor_total=form_quantidade_vendidos * form_valor_unidade
            newform = CaixaStickers(data_venda=form_data_venda, quantidade_vendidos=form_quantidade_vendidos, valor_unidade=form_valor_unidade,valor_total=form_valor_total)
            newform.save()
            return redirect('index')
    else:
        form = StickerForm()

    if request.method == "POST" and "estoque" in request.POST:
        estoque_add = int(request.POST.get("estoque-quantidade"))
        form = TotalStickers(stickers_total=estoque_add)
        form.save()
        return redirect('index')

    return render(request, 'index.html', {
        'stickers': stickers, 
        'form':form, 
        'valor_total':valor_total, 
        'quantidade_vendidos':total_vendidos, 
        'total_estoque':total_estoque
    })

@login_required
def excluir_venda(request, id_sticker):
    venda_stickers = CaixaStickers.objects.get(pk=id_sticker)
    venda_stickers.delete()
    return redirect('index')

def login(request):
    return render(request, 'login.html')
