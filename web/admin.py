from django.contrib import admin
from web.models import *
# Register your models here.

class ModifiedSlider(admin.ModelAdmin):
    list_display = ('title1','title2','title3','picture')# extra fields in the admin
    list_filter = ('title1',) #filters
    search_fields = ('title1',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically
class ModifiedProduct(admin.ModelAdmin):
    list_display = ('name','price','currency','inDate','status','brandsby','designedby',)# extra fields in the admin
    list_filter = ('price','shoesSize','size',) #filters
    search_fields = ('name','markname',) #bu alanlar üzerinde search yapılacaktır
    date_hierarchy = 'inDate' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'

class ModifiedDesigner(admin.ModelAdmin):
    list_display = ('name','lastname',)# extra fields in the admin
    list_filter = ('name','lastname','email',) #filters
    search_fields = ('name','lastname',) #bu alanlar üzerinde search yapılacaktır
    # date_hierarchy = 'inDate' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'



class ModifiedBrands(admin.ModelAdmin):
    list_display = ('name',)# extra fields in the admin
    list_filter = ('name',) #filters
    search_fields = ('name',) #bu alanlar üzerinde search yapılacaktır
    # date_hierarchy = 'inDate' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'



class ModifiedTeam_member(admin.ModelAdmin):
    list_display = ('team_name',)# extra fields in the admin
    list_filter = ('team_name',) #filters
    search_fields = ('team_name',) #bu alanlar üzerinde search yapılacaktır
    # date_hierarchy = 'inDate' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'





admin.site.register(Sliders,ModifiedSlider)
admin.site.register(Product,ModifiedProduct)
admin.site.register(Brands,ModifiedBrands)
admin.site.register(Designer,ModifiedDesigner)
admin.site.register(Footer)
admin.site.register(Seyirci)
admin.site.register(Team_member,ModifiedTeam_member)

