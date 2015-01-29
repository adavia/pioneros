#-*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from articles.models import Article, Video, Category, Image, Sponsor
from teams.models import Game
from articles.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def index(request):
	sponsors = Sponsor.objects.filter(status = True)[:4]
	return render(request, 'articles/index.html', {
		'sponsors': sponsors
	})

def home(request):
    banners = Article.objects.filter(status = True)[:4]
    articles = Article.objects.filter(status = True)[:3]
    games = Game.objects.filter(status = True).order_by('-id')[:3]
    images = Image.objects.all()[:6]
    videos = Video.objects.all()[:3]
    categories = Category.objects.all()
    sponsors = Sponsor.objects.all()
    return render(request, 'articles/home.html', {
                    'banners': banners,
                    'articles': articles,
                    'games': games,
                    'images': images,
                    'videos': videos,
                    'categories': categories,
                    'sponsors': sponsors
    })

def detail(request, year, month, day, slug):
	articles = Article.objects.filter(status = True)[:4]
	article = get_object_or_404(Article, status = True,
										 created_at__year = year,
										 created_at__month = month,
										 created_at__day = day,
										 url = slug)
	url = request.build_absolute_uri('/%s/%s/%s/%s'%(article.created_at.year,
													 article.created_at.month,
													 article.created_at.day,
													 article.url))
	return render(request, 'articles/detail.html', {
					'article': article,
					'articles':articles,
					'url':url
	})

def list(request):
	a = Article.objects.filter(status = True)
	articles = paginator(request, a)
	images = Image.objects.all()[:6]
	videos = Video.objects.all()[:3]
	return render(request, 'articles/list.html', {
				 	'articles': articles,
				 	'images': images,
				 	'videos': videos
	})

def category(request, slug):
	a = Article.objects.filter(category__url = slug, status = True)
	articles = paginator(request, a)
	images = Image.objects.all()[:6]
	videos = Video.objects.all()[:3]
	return render(request, 
				 'articles/category.html', {
				 'articles': articles,
				 'images': images,
				 'videos': videos
	})

def paginator(request, parameter):
    paginator = Paginator(parameter, 4)

    try:
        page = int(request.GET.get('pag', '1'))
    except:
        page = 1
    try:
        p = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p = paginator.page(paginator.num_pages)

    return p

def sponsors(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'articles/sponsors.html', {
    				'sponsors': sponsors
    })

def gallery(request):
	images = Image.objects.all()[:15]
	videos = Video.objects.all()
	return render(request, 'articles/gallery.html', {
				 	'images': images,
				 	'videos': videos
	})

def search(request):
	errors = []
	if 'term' in request.GET:
		search = request.GET['term']
		if not search:
			errors.append('Ingrese algún término de búsqueda.')
		elif len(search) > 20:
			errors.append('Ingrese algún término que no supere los 20 caracteres')
		else:
			articles = Article.objects.filter(title__icontains = search, status = True)[:4]
			last = Article.objects.filter(status = True)[:4]
			images = Image.objects.all()[:8]
			return render(request, 
				 'articles/search.html', {
				 'articles': articles,
				 'last': last,
				 'errors': errors,
				 'images': images
			})
	return render(request, 
				 'articles/search.html', {
				 'errors': errors
	})

def contact(request):
	return render(request, 'articles/contact.html')

def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)      
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message_text']
            contact_email(request, name, email, message_text)
            message = 'Los datos han sido ingresados correctamente. En la brevedad nos estaremos contactando al mail que nos proporcionó. Muchas gracias.'

    else:
        form = ContactForm()
    return render(request, 'articles/contact.html', {
    	'form':form, 'message':message
    })

def contact_email(request, name, email, message_text):
    to = email
    html_content = """<h3>Mensaje enviado del Sr/a: %s </h3><p>%s<p><b>Direccion de correo electronico: %s</b></p><br>
    <small>Este es un mensaje enviado automaticamente. Por favor no responda a esta direccion de mail.</small>"""%(name, message_text, email)

    msg = EmailMultiAlternatives('Contacto Pioneros Cancun FC', html_content, 'from@server.com', ['jocelynefdz@gmail.com'])
    msg.attach_alternative(html_content, 'text/html') #Definimos el contenido como html
    msg.send() #Enviamos el correo
