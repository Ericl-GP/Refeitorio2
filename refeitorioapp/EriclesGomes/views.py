from django.shortcuts import render, get_object_or_404, redirect
from refeitorioapp.forms import AlunoForms , EventoForms,Aluno,Evento
# Create your views here.
def home(request):

    form = AlunoForms()
    context = {'form':form}
    return render(request, 'refeitorio/home.html',context)

def mostrar_evento(request):
    eventos =Evento.objects.all()
    context={'eventos':eventos}
    return render(request,'refeitorio/evento.html',context)

def eventos(request):
    eventos=Evento.objects.all()
    form = EventoForms(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            evento=form.save()
            evento.save()
            form=EventoForms()
    context = {'form':form,'eventos':eventos}
    return render(request, 'refeitorio/evento.html',context)


def new_aluno(request):
    alunos =Aluno.objects.all()
    form = AlunoForms(request.POST, request.FILES)
    if request.method == "POST":

        if form.is_valid():
            aluno = form.save()
            aluno.save()
            form = AlunoForms()

    context = {'form':form,'alunos':alunos}
    return render(request , 'refeitorio/new_aluno.html', context)

def mostrar_aluno(request):
    alunos =Aluno.objects.all()
    context={'alunos':alunos}
    return render(request,'refeitorio/new_aluno.html',context)

def editar_aluno(request,id):
    alunos=Aluno.objects.all()
    aluno = get_object_or_404(Aluno,pk=id)
    form = AlunoForms(instance=aluno)
    if (request.method=='POST'):
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('new_aluno')
        else:
            return render(request,'refeitorio/editar_aluno.html',{'form':form,'alunos':alunos})
    else:
        return render(request,'refeitorio/editar_aluno.html',{'form':form,'alunos':alunos})
    
def excluir_aluno(request,id):
    aluno=get_object_or_404(Aluno,pk=id)
    form=AlunoForms(instance=aluno)
    alunos=Aluno.objects.all()
    if (request.method == 'POST'):
        aluno.delete()
        return redirect('new_aluno')
    return render(request,'refeitorio/excluir_aluno.html',{'aluno':aluno,'alunos':alunos,'form':form})