from django.contrib import admin
from articles.models import Article, Category, Image, Video, Sponsor

class ImageInline(admin.TabularInline):
    model = Image
    extra = 5
    include = ['image', 'description', 'updated_at']
    exclude = ['width', 'height', 'thumbnail1', 'thumbnail2', 'thumbnail3']
   
class VideoInline(admin.TabularInline):
    model = Video
    extra = 5
    exclude = ['url']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class SponsorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'images', 'videos')
    list_filter = ('category',)
    search_fields = ['title']
    prepopulated_fields = {"url": ("title",)}
    #asi se va cambiando el orden de los campos en el admin
    fieldsets = [
        (None, {'fields': ['title', 'url', 'body', 'sub_title', 'aside', 'status']}),
        ('Informacion adicional', {'fields': [('category',), 'updated_at']}),
    ]
    inlines = [ImageInline, VideoInline]
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ['article', '__unicode__', 'thumbnail', 'updated_at']
    list_filter = ['article']
    search_fields = ['title']
    exclude = ['thumbnail1','width', 'height']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['article', '__unicode__', 'updated_at']
    list_filter = ['article']
    search_fields = ['title']
    prepopulated_fields = {"url": ("title",)}

    def get_queryset(self, request):
        qs = self.model.objects.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Sponsor, SponsorAdmin)


