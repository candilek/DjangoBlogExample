
from django.db import models

# Create your models here.
from django.utils import timezone


class Post (models.Model): #Model sınıfından miras aldık
    title=models.CharField(max_length=120,verbose_name='Başlık')   #baslık alanı---charfilelf a mutlaka max değer vermek gerekir.

    content=models.TextField(default='', verbose_name='içerik')  #metin alanı olusturdum

    publishing_date=models.DateTimeField(default=timezone.now, verbose_name='yayımlanma tarihi') #yayınlanma tarihi için tarih ve saat alanı

#---------verbose_name parametresi ile alanlarda değişiklik yayıp kullanıcıya görünen kısmı Türkçe yaptık.----

    def __str__(self): #her post kendi adıyla kayıt olsun.
        return self.title


#Dökümana bak: https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
