from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','publishing_date']   #admin panelinde bu alanlar gözükecek
    list_display_links = ['publishing_date']   #alanlar tıklanabilir oldu.
    list_filter = ['publishing_date']   #birden çok veri arasında filtreleme işlemi yapılacak
    search_fields = ['title', 'content']  #arama çubuğu ekledik.
    list_editable = ['title'] #alanlar üzeinde güncellme yapması için.

    #list_editable olarak ayarlanan alanlar link özelliği taşımamalır.
    class Meta:
        model=Post #meta sınıfında Post modelini  referans aldık



admin.site.register(Post,PostAdmin)


# Register your models here.
