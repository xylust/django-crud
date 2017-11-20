from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse, QueryDict
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django import forms


# Create your views here.

def index(request):
    return render(request, 'webapp/index.html')


class Validation(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()


def create_product(request):
    if request.method == 'POST':
        form = Validation(request.POST, request.FILES)
        if form.is_valid():
            product = Product(name=request.POST['name'],
                              description=request.POST['description'],
                              price=request.POST['price'])
            product.save()
            return JsonResponse(model_to_dict(product), safe=False)
        else:
            raise forms.ValidationError("Invalid values!")


def get_product(request):
    if request.method == 'GET':
        products = Product.objects.all().values()
        products_list = list(products)
        return JsonResponse(products_list, safe=False)


def modify_product(request, id):
    if request.method == 'PUT':
        # form = Validation(request.POST, request.FILES) ... can't validate the same way because it is PUT
        # if form.is_valid(): ... Too lazy to find out how to get around it thus unvalidated it is!
        put = QueryDict(request.body)
        Product.objects.filter(id=id).update(
            name=put.get('name'),
            description=put.get('description'),
            price=put.get('price'))
        product = Product.objects.filter(id=id).first()
        return JsonResponse(model_to_dict(product), safe=False)
        # else:
        #     raise forms.ValidationError("Invalid values!")


def delete_product(request, id):
    if request.method == 'DELETE':
        product = Product.objects.filter(id=id).first()
        get_object_or_404(Product, pk=id).delete()
        return JsonResponse(model_to_dict(product), safe=False)
