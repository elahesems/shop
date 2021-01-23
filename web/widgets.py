from web.models import *
from django import template

register=template.Library()

@register.simple_tag(takes_context=True)
def navbarVariables(context):
    categoriesList = Product._meta.get_field('category').choices
    categories = []
    for i in categoriesList:
        categories.append(i[0])
    context['categories'] = categories

    _products=Product.objects.all()
    womanListing = []
    manListing = []
    aksesuarListing = []
    for product in _products:
        kk = product.category
        if 'kadin' in kk:
            womanListing.append(product)
        if 'erkek' in kk:
            manListing.append(product)
        if 'aksesuar' in kk:
            aksesuarListing.append(product)

    womanListingPS = []
    for product in womanListing:
        if product.productSpeciality:
            womanListingPS.append(product)
    context['womanListingPS'] = womanListingPS
    manListingPS = []
    for product in manListing:
        if product.productSpeciality:
            manListingPS.append(product)
    context['manListingPS'] = manListingPS
    aksesuarListingPS = []
    for product in aksesuarListing:
        if product.productSpeciality:
            aksesuarListingPS.append(product)
    context['aksesuarListingPS'] = aksesuarListingPS
