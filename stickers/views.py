from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum
from .models import CaixaSticker, TotalSticker
from .forms import StickerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required
def index(request):
    stickers = CaixaSticker.objects.filter().order_by("-pk")
    valor_total = CaixaSticker.objects.all().aggregate(valor_total = Sum('valor_total')).get('valor_total')
    total_vendidos = CaixaSticker.objects.all().aggregate(quantidade_vendidos = Sum('quantidade_vendidos')).get('quantidade_vendidos')
    total_estoque = TotalSticker.objects.latest("pk")

    try:
        total_estoque = total_estoque.stickers_total - total_vendidos
        if total_estoque < 0:
            total_estoque = "Inválido"
            messages.add_message(request, messages.INFO, 'Você vendeu mais do que tinha, altere o valor do estoque ou delete a última venda!')
    except TypeError:
        total_estoque = total_estoque.stickers_total

    if request.method == "POST" and "venda" in request.POST:
        form = StickerForm(request.POST)
        if form.is_valid():
            form_data_venda = form.cleaned_data['data_venda']
            form_quantidade_vendidos = form.cleaned_data['quantidade_vendidos']
            form_valor_unidade = form.cleaned_data['valor_unidade']
            form_valor_total=form_quantidade_vendidos * form_valor_unidade
            newform = CaixaSticker(data_venda=form_data_venda, quantidade_vendidos=form_quantidade_vendidos, valor_unidade=form_valor_unidade,valor_total=form_valor_total)
            newform.save()
            return redirect('index')
    else:
        form = StickerForm()

    if request.method == "POST" and "estoque" in request.POST:
        estoque_novo = int(request.POST.get("estoque-quantidade"))
        form = TotalSticker(stickers_total=estoque_novo)
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
    venda_stickers = CaixaSticker.objects.get(pk=id_sticker)
    venda_stickers.delete()
    return redirect('index')

def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        messages.info(request, 'Usuario ou senha invalidos!')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
