from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Sliders(models.Model):
    title1 = models.CharField(max_length=100, null=True,blank=True, verbose_name='en ust sırada yazılacak')
    title2 = models.CharField(max_length=100, null=True,blank=True,verbose_name='ortada yazılacak')
    title3 = models.CharField(max_length=100, null=True,blank=True,verbose_name='en alt')
    link = models.URLField(verbose_name='website',null=True,blank=True)
    picture = models.ImageField('resim seçiniz',null=True,blank=True)
    def __str__(self):
        return self.title1
    class Meta:
        verbose_name_plural = "sliderler"


class Designer(models.Model):
    name = models.CharField(max_length=100,verbose_name='ad')
    lastname = models.CharField(max_length=100,verbose_name='soyad')
    telephone = models.CharField(max_length=100,verbose_name='telefon')
    email = models.EmailField(max_length=100,verbose_name='eposta')
    def __str__(self):
        return str(self.name) + ' ' + str(self.lastname)
    class Meta:
        verbose_name_plural = "TaSaRıMCı"
class Product(models.Model):
    currencyType=(
        ('tl','TL'),
        ('usd','USD'),
        ('euro','EURO')
    )
    categoryType = (
        ('kadin', 'kadin'),
        ('erkek', 'erkek'),
        ('elektronik', 'elektronik'),
        ('sport', 'sport'),
        ('aksesuar', 'aksesuar'),
        ('makyaj', 'makyaj'),
    )
    shoesSizeChoices = (
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44')
    )
    sizeChoices = (
        ('xs', 'xs'),
        ('s', 's'),
        ('m', 'm'),
        ('l', 'l'),
        ('xl', 'xl'),
        ('xxl', 'xxl'),
        ('xxxl', 'xxxl')

    )
    colorChoices = (
        ('red', 'red'),
        ('pink', 'pink'),
        ('orange', 'orange'),
        ('yellow', 'yellow'),
        ('purple', 'purple'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('brown', 'brown'),
        ('black', 'black'),

    )


    name = models.CharField(max_length=100,verbose_name='ad')
    price = models.IntegerField(max_length=100,verbose_name='fiyat')
    currency = models.CharField(max_length=5,choices=currencyType, default='tl',verbose_name='kur')
    picture = models.ImageField('resim seçiniz', null=True, blank=True)
    designedby = models.ForeignKey(Designer,on_delete=models.CASCADE,verbose_name='tasarımcı', null=True, blank=True)
    category = MultiSelectField(choices=categoryType,verbose_name='kategoriler',null=True,blank=True)
    shoesSize = MultiSelectField(choices=shoesSizeChoices,verbose_name='ayakkabı numarası',null=True,blank=True)
    size = MultiSelectField(choices=sizeChoices,verbose_name='size',null=True,blank=True)
    color = MultiSelectField(choices=colorChoices,verbose_name='renk',null=True,blank=True)
    inDate = models.DateField(auto_now_add=True,null=True,blank=True,verbose_name='giriş tarihi')
    status = models.BooleanField(default=True,verbose_name='gösterilsin mi?')


    class Meta:
        verbose_name_plural = "Ürünler"


