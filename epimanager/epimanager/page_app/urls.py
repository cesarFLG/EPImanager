from django import views
from django.urls import path
from page_app.views import cadastrar_emprestimos, cadastrar_epi, colaboradores, colaboradores_cadastrados, editar_colaborador, epi_cadastrados, excluir_colaborador, home, lista_emprestimos, login

urlpatterns = [

    path('', home),
    path('epi/cadastrar/', cadastrar_epi, name='cadastrar_epi'), # acessa a tela de cadastro de epi
    path('colaboradores/cadastrar/',colaboradores, name='colaboradores'), # acessa a tela de cadastro de colaboradores
    path('', home, name='home'),  # retorno home
    path('colaboradores/cadastrados/', colaboradores_cadastrados, name='colaboradores_cadastrados'),
    path('emprestimo/', cadastrar_emprestimos, name='cadastrar_emprestimos'),
    path('emprestimos/', lista_emprestimos, name='lista_emprestimos'),
    path('epi/cadastrdos/', epi_cadastrados, name='epi_cadastrados'),
    path('login/', login, name='login'),
     path('colaboradores/editar/<int:colaborador_id>/', editar_colaborador, name='editar_colaborador'),
     path('colaboradores/excluir/<int:colaborador_id>/', excluir_colaborador, name='excluir_colaborador'),
]

