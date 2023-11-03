from django.shortcuts import render,redirect
from .models import ProductMst, ProductSubCat

# Create your views here.
def dashboard_view(request):
    products = ProductMst.objects.all()
    return render(request, 'dashboard.html',{'products': products})

from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductMst


def edit_product(request, product_id):
    product = ProductMst.objects.get(pk=product_id)
    if request.method == 'POST':
        product_subcat = product.productsubcat
        product_subcat.product_price = request.POST.get('product_price')
        product_subcat.product_image = request.POST.get('product_image')
        product_subcat.product_model = request.POST.get('product_model')
        product_subcat.product_ram = request.POST.get('product_ram')
        product_subcat.save()
        product.save()
        
        return redirect('dashboard_view')

    return render(request, 'edit_product.html', {'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(ProductMst, product_id=product_id)
    product.delete()
    return redirect('dashboard_view')


def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_image = request.POST.get('product_image')
        product_model = request.POST.get('product_model')
        product_ram = request.POST.get('product_ram')

        if product_name:
            product_mst = ProductMst.objects.create(product_name=product_name)
            product_subcat = ProductSubCat.objects.create(
                product=product_mst,
                product_price=product_price,
                product_image=product_image,
                product_model=product_model,
                product_ram=product_ram
            )

            return redirect('dashboard_view')
    
    return redirect('dashboard_view')