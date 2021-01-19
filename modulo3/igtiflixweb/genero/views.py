from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from . import forms, models

def cadastro(request):
    form = forms.GeneroForm()

    if request.method == 'POST':
        print('Vou salvar os dados!')
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERROR')

    generos_list = models.Genero.objects.order_by('descricao')
    data_dict = {'form':form, 'generos_records':generos_list}
    return render(request,'genero/genero.html', data_dict)

def delete(request,id):
    try:
        models.Genero.objects.filter(id=id).delete()
        form = forms.GeneroForm()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form':form, 'generos_records':generos_list}
        return render(request, 'genero/genero.html', data_dict)

    except:
        return HttpResponseNotAllowed()

def update(request,id):
    item = models.Genero.objects.get(id=id)
    
    if request.method == 'GET':
        form = forms.GeneroForm(initial={'descricao': item.descricao})
        data_dict = {'form' : form}
        return render(request, 'genero/genero_upd.html', data_dict)
    else:
        form = forms.GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form':form, 'generos_records':generos_list}
        return render(request, 'genero/genero.html', data_dict)
