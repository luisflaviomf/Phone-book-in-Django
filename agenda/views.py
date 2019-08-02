from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
# Create your views here.

def contatos(request):
    contato = Contatos.objects.all()
    return render(request, 'index.html', {'contato':contato})

def contatocriar(request):
    form = ContatoForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'contatocriar.html', {'form':form})

def contatoupdate(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = ContatoForm(request.POST or None, instance=contato)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'contatocriar.html', {'form':form})

def contatodelete(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = ContatoForm(request.POST or None, instance=contato)

    if request.method == 'POST':
        contato.delete()
        return redirect('index')

    return render(request, 'contatodelete.html', {'contato':contato})