from django.shortcuts import redirect, render
from .models import crypto
# Create your views here.

def home(request):
    return render(request, 'cryptoConfigs/home.html')

def add_crypto(request):
    if request.method == 'POST':
        crypto_name = request.POST.get('crypto')
        valor = float(request.POST.get('valor'))

        # Aqui você pode salvar os dados no banco de dados ou fazer outras operações
        crypto.objects.create(crypto=crypto_name, valor=valor)

        return redirect('listagem_crypto')  # Redirecionar para a terceira view

def cryptos(request):
    #Exibir todas as cryptos cadastradas em uma nova página
    context = {
        'cryptos': crypto.objects.all()
    }

    #Retornando os dados para a página de listagem de cryptos
    return render(request, 'cryptoConfigs/cryptos.html', context)
