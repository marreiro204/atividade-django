from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico

# Lista de médicos
def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/medico.html', {'medicos': medicos})


def medico_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        especialidade = request.POST.get('especialidade')
        crm = request.POST.get('crm')

        Medico.objects.create(nome=nome, especialidade=especialidade, crm=crm)
        return redirect('medico_list')

    return render(request, 'clinica/medicoForm.html')

def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    
    if request.method == 'POST':
        medico.nome = request.POST.get('nome')
        medico.especialidade = request.POST.get('especialidade')
        medico.crm = request.POST.get('crm')
        medico.save()
        return redirect('medico_list')

    return render(request, 'clinica/medicoForm.html', {'medico': medico})

def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)

    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')

    return render(request, 'clinica/medicoConfirmDelete.html', {'medico': medico})

# Filtrar médicos por especialidade
def especialidade_view(request):
    especialidade = request.GET.get('especialidade', '')
    medicos = []

    if especialidade:
        medicos = Medico.objects.filter(especialidade__icontains=especialidade)

    return render(request, 'clinica/especialidade.html', {
        'medicos': medicos,
        'especialidade': especialidade
    })



