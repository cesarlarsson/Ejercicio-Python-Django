from django.http import HttpResponseRedirect,HttpResponse
from forms  import CategoriaForms,ProductosForms
from django.shortcuts import render_to_response
from django.template import RequestContext



def index(request):
    return render_to_response('index.html', {'nombre':'Andres Ospina', 'blah':'producto'})


def categoriaform(request):
    if request.method == 'POST':
        form = CategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:    
        form = CategoriaForms()
    return render_to_response('productos/template.html', {'form': form}, RequestContext(request, {}))

def productoform(request):
    if request.method == 'POST':
        form = ProductosForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductosForms()
    return render_to_response('productos/template.html', {'form': form}, RequestContext(request, {}))
    