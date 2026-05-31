
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from datetime import datetime
from .models import Funcionario

def employee_list(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'funcionario/list.html', {'funcionario': funcionario})

def employee_create(request):
    if request.method == 'POST':
        try:
            salario = float(request.POST.get('salario'))
            data_admissao = datetime.strptime(request.POST.get('data_admissao'), '%Y-%m-%d').date()
            
            Funcionario(
                nome=request.POST['nome'].strip(),
                cargo=request.POST['cargo'].strip(),
                salario=salario,
                data_admissao=data_admissao
            ).save()
            return redirect('funcionario_list')
        except (ValueError, KeyError) as e:
            return HttpResponseBadRequest(f"Dados inválidos: {e}")
    return render(request, 'funcionario/form.html', {'action': 'create'})

def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario, id=pk)
    if request.method == 'POST':
        try:
            funcionario.name = request.POST['nome'].strip()
            funcionario.position = request.POST['cargo'].strip()
            funcionario.salary = float(request.POST['salario'])
            funcionario.admission_date = datetime.strptime(request.POST['data_admissao'], '%Y-%m-%d').date()
            funcionario.save()
            return redirect('funcionario_list')
        except (ValueError, KeyError) as e:
            return HttpResponseBadRequest(f"Erro ao atualizar: {e}")
    return render(request, 'funcionario/form.html', {'action': 'update', 'funcionario': funcionario})

def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, id=pk)
    funcionario.delete()
    return redirect('funcionario_list')