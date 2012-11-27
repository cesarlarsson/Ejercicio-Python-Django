from django.http import HttpResponseRedirect,HttpResponse

import datetime
from django.db.models import Q
from django.shortcuts import render_to_response
#from django.template.response import TemplateResponse
from books.models import Book, Publisher,Author,Member
from forms import ContactForm,PublisherForm
from django.http import Http404
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from cStringIO import StringIO


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. %s</body></html>" % (now,'estoy jodiendo')
    return HttpResponse(html)


def holamundo(request):
    now = datetime.datetime.now()
    html = "<html><body>hola mundo</body></html>" 
    return HttpResponse(html)


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
                Q(title__icontains=query) |
                Q(authors__first_name__icontains=query) |
                Q(authors__last_name__icontains=query)
                )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
        
    return render_to_response("books/search.html", {"results": results,"query": query})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           topic = form.clean_data['topic']
           message = form.clean_data['message']
           sender = form.clean_data.get('sender', 'noreply@example.com') #se utiliza para validar de que no llego nada poderlo enviar al correo del administrador 
    else:
        form = ContactForm()
    return render_to_response('books/contact2.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_publisher/')
    else:
            form = PublisherForm()
    return render_to_response('books/add_publisher.html', {'form': form})

def new_publisher(request):
        form = PublisherForm()
        return render_to_response('books/add_publisher.html', {'form': form})
    
def books_by_publisher(request, name):
    # Look up the publisher (and raise a 404 if it can't be found).
    try:
        publisher = Publisher.objects.get(name__iexact=name)
    except Publisher.DoesNotExist:
            raise Http404
# Use the object_list view for the heavy lifting.
    return list_detail.object_list(
                                   request,
                                   queryset = Book.objects.filter(publisher=publisher),
                                  # template_name = "books/books_by_publisher.html",
                                   template_object_name = "book",
                                    extra_context = {"publisher" : publisher}
)

def books_by_publisher2(request, name):
      return render_to_response('books/mostrar.html', {'form': name})
  
def author_detail(request, author_id):
# Look up the Author (and raise a 404 if she's not found)
    author = get_object_or_404(Author, pk=author_id)
# Record the last accessed date
    author.last_accessed = datetime.datetime.now()
    author.save()
# Show the detail page
    return list_detail.object_detail(
                                     request,
                                     queryset = Author.objects.all(),
                                      template_object_name = "author",
                                     object_id = author_id,
                                     )  
    
def hello_pdf(request):
# Se crea el objeto HttpResponse con los headers PDF apropiados.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
# Se crea el objeto PDF, usando el objeto de respuesta como si fuese un "archivo".
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello world.")
  
# Se cierra el objeto PDF, y terminamos.
    p.showPage()
    p.save()
    return response

def show_color(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % \
                            request.COOKIES["favorite_color"])
    else:
        return HttpResponse("You don't have a favorite color.")

def set_color(request):
    if "favorite_color" in request.GET:
# Create an HttpResponse object...
        response = HttpResponse("Your favorite color is now %s" % \
                                request.GET["favorite_color"])
# ... and set a cookie on the response
        response.set_cookie("favorite_color",
                            request.GET["favorite_color"])
        return response
    else:
        return HttpResponse("You didn't give a favorite color.")
    
#def post_comment(request, new_comment):
#    if request.session.get('has_commented', False):   
#        return HttpResponse("You've already commented.")
#    c = comments.Comment(comment=new_comment)
#    c.save()
#    request.session['has_commented'] = True
#    return HttpResponse('Thanks for your comment!') 

def login(request):
    try:
        m = Member.objects.get(username__exact=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse("You're logged in.")
    except Member.DoesNotExist:
            return HttpResponse("Your username and password didn't match.")
    