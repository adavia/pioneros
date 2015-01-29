from articles.models import Category, Article
from teams.models import Image

def footer(request):
	f_articles = Article.objects.filter(status = True)[:4]
	f_categories = Category.objects.all()[:4]
	f_images = Image.objects.all()[:8]

	context = {'f_articles': f_articles,
			   'f_categories': f_categories,
			   'f_images': f_images}
	return context