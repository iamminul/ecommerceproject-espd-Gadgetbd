from django.shortcuts import render
from. models import *
def homepage(request):
    prod = Product.objects.all()

 #for loop for media image show
    for p in prod:
        print('Product Image URL:', p.prod_image)

    context ={
        'prod':prod
    }



    return render(request,'home/homepage.html', context)

def prodDetail(request, id):

    prod = Product.objects.get(pk=id)
    print('Product ID:', prod.pk)
    print('Product Name:', prod.prod_name)
    print('Product Price:', prod.prod_price)
    print('Product Description:', prod.prod_desc)
    context = {
        'prod':prod
    }
    return render(request,'home/productDetail.html', context)
