from refeitorioapp.models import Aluno, Evento
from django import forms

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        #fields = ['nome_aluno','matricula_aluno','matricula','foto_aluno']
        fields = '__all__'
class EventoForms(forms.ModelForm):
    class Meta:
        model = Evento
        #fields = ['nome_aluno','matricula_aluno','matricula','foto_aluno']
        fields = '__all__'
