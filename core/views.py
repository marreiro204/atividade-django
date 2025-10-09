from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Medico, Especialidade

# ✅ View de listagem (qualquer usuário autenticado pode ver)
@permission_required('core.view_medico', raise_exception=True)
def lista_medicos(request):
    medicos = Medico.objects.select_related('especialidade').all()
    return render(request, 'core/lista_medicos.html', {'medicos': medicos})


# ✅ View de cadastro (somente quem tem permissão de adicionar)
@permission_required('core.add_medico', raise_exception=True)
def cadastrar_medico(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        crm = request.POST.get('crm')
        especialidade_id = request.POST.get('especialidade')

        especialidade = Especialidade.objects.get(id=especialidade_id)
        Medico.objects.create(nome=nome, crm=crm, especialidade=especialidade)

        return redirect('lista_medicos')

    especialidades = Especialidade.objects.all()
    return render(request, 'core/form_medico.html', {'especialidades': especialidades})

