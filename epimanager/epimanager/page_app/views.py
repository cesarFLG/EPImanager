from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import EPI, Colaborador, Emprestimo
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ValidationError

def home (request):
    return render (request, "home.html")

def cadastrar_epi(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        lote = request.POST['lote']

        epi = EPI(nome=nome, lote=lote)
        epi.save()
        messages.success(request, 'EPI cadastrado com sucesso!')

    return render(request, 'cadastrar_epi.html')

def colaboradores(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        numero = request.POST['numero']

        # Verificar se já existe um colaborador com o mesmo nome ou número
        if Colaborador.objects.filter(nome=nome).exists():
            messages.error(request, 'Já existe um colaborador cadastrado com este nome.')
        elif Colaborador.objects.filter(numero=numero).exists():
            messages.error(request, 'Já existe um colaborador cadastrado com este número.')
        else:
            colaborador = Colaborador(nome=nome, numero=numero)
            colaborador.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
        
    return render(request, 'colaboradores.html')

def colaboradores_cadastrados(request):
    colaboradores = Colaborador.objects.all()  # Busca todos os colaboradores cadastrados
    return render(request, 'colaboradores_cadastrados.html', {'colaboradores': colaboradores})

def cadastrar_emprestimos(request):
    colaboradores = Colaborador.objects.all()
    epis = EPI.objects.all()

    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador')
        epi_id = request.POST.get('epi')
        data_devolucao = request.POST.get('data_devolucao')

        colaborador = Colaborador.objects.get(id=colaborador_id)
        epi = EPI.objects.get(id=epi_id)
        
        emprestimo = Emprestimo(
            colaborador=colaborador,
            epi=epi,
            data_devolucao=data_devolucao if data_devolucao else None
        )
        emprestimo.save()

        messages.success(request, 'Empréstimo cadastrado com sucesso!')
        return redirect('cadastrar_emprestimos')

    return render(request, 'cadastrar_emprestimos.html', {
        'colaboradores': colaboradores,
        'epis': epis
    })
    
def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'lista_emprestimos.html', {'emprestimos': emprestimos})

def epi_cadastrados(request):
    epis = EPI.objects.all()
    return render(request, 'epi_cadastrados.html', {'epis': epis})

def login(request):
    return render(request, 'login.html')

def editar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if request.method == 'POST':
        colaborador.nome = request.POST['nome']
        colaborador.numero = request.POST['numero']
        colaborador.save()
        return redirect('colaboradores_cadastrados')  # Redirecionar para a lista de colaboradores

    return render(request, 'editar_colaborador.html', {'colaborador': colaborador})

def excluir_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)
    colaborador.delete()
    return redirect('colaboradores_cadastrados')