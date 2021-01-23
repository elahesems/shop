from django.db import models
from multiselectfield import MultiSelectField
from colorfield.fields import ColorField
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


class Brands(models.Model):
    name = models.CharField(max_length=300,verbose_name='brandin Ismi')
    brandslogo = models.ImageField(verbose_name='logo')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "BRaNDs"



class Product(models.Model):
    currencyType=(
        ('tl','₺'),
        ('usd','$'),
        ('euro','€')
    )
    categoryType = (
        ('kadin', 'kadin'),
        ('erkek', 'erkek'),
        ('elektronik', 'elektronik'),
        ('sport', 'sport'),
        ('aksesuar', 'aksesuar'),
        ('makyaj', 'makyaj'),
    )
    productCategory= (
        ('jaket', 'jaket'),
        ('pantolon', 'pantolon'),
        ('gömlek', 'gömlek'),
        ('mont', 'mont'),
        ('kölye', 'kölye'),
        ('halhal', 'halhal'),
        ('bilezik', 'bilezik'),
        ('küpe', 'küpe'),
        ('saat', 'saat'),
        ('etek', 'etek'),
        ('gözlük', 'gözlük'),
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



    name = models.CharField(max_length=100,verbose_name='ad')
    brandsby = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='brand', null=True, blank=True)
    price = models.IntegerField(max_length=100,verbose_name='fiyat')
    oldprice = models.IntegerField(max_length=100,verbose_name='oldPrice',null=True,blank=True)
    currency = models.CharField(max_length=5,choices=currencyType, default='tl',verbose_name='kur')
    picture = models.ImageField('resim seçiniz', null=True, blank=True)
    designedby = models.ForeignKey(Designer,on_delete=models.CASCADE,verbose_name='tasarımcı', null=True, blank=True)
    category = MultiSelectField(choices=categoryType,verbose_name='kategoriler',null=True,blank=True)
    productSpeciality= models.CharField(choices=productCategory,max_length=100,null=True,blank=True,verbose_name='ürün türü')
    shoesSize = MultiSelectField(choices=shoesSizeChoices,verbose_name='ayakkabı numarası',null=True,blank=True)
    size = MultiSelectField(choices=sizeChoices,verbose_name='size',null=True,blank=True)
    colorField1 = ColorField(verbose_name='1.renk',null=True,blank=True)
    colorField2 = ColorField(verbose_name='2.renk',null=True,blank=True)
    colorField3 = ColorField(verbose_name='3.renk',null=True,blank=True)
    colorField4 = ColorField(verbose_name='4.renk',null=True,blank=True)
    productInformation = models.TextField(null=True,blank=True,verbose_name='ürün bilgileri')
    description = models.TextField(null=True,blank=True,verbose_name='description')
    inDate = models.DateField(auto_now_add=True,null=True,blank=True,verbose_name='giriş tarihi')
    status = models.BooleanField(default=True,verbose_name='gösterilsin mi?')



    class Meta:
        verbose_name_plural = "Ürünler"



class Footer(models.Model):
    address = models.CharField(max_length=100,null=True,blank=True)
    telephone = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name='EPOSTA')
    facebook = models.URLField(null=True,blank=True,verbose_name='facebook')
    twitter = models.URLField(null=True,blank=True,verbose_name='twitter')
    vimeo = models.URLField(null=True,blank=True,verbose_name='vimeo')
    googlePlus = models.URLField(null=True,blank=True,verbose_name='googlePlus')
    tumblr = models.URLField(null=True,blank=True,verbose_name='tumblr')
    pinterest = models.URLField(null=True,blank=True,verbose_name='pinterest')


class Seyirci(models.Model):

    location = models.CharField(max_length=500,help_text=(':2131/5 sokak no:6 Adalet mahallesi bayraklı'))
    countrylocation = models.CharField(max_length=500,null=True,blank=True)
    phone = models.IntegerField(max_length=100,verbose_name='phonenumber')
    fax = models.IntegerField(max_length=100,verbose_name='fax')
    email1 = models.EmailField(max_length=100)
    email2 = models.EmailField(max_length=100)

    class Meta:
        verbose_name_plural = "ConTaCt"


class Team_member(models.Model):
    team_name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    detail = models.CharField(max_length=400)
    img = models.ImageField(verbose_name='resim')
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    vimeo = models.URLField(null=True, blank=True)
    tumblr = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True)
    # inDate = models.DateField(auto_now_add=True,null=True,blank=True,verbose_name='giriş tarihi')


    class Meta:
        verbose_name_plural = "TeamMember"