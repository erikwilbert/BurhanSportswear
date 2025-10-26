from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForms
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import datetime
import json


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "my")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'nama_aplikasi': 'Burhan Sportswear',
        'name': request.user.username,
        'class': 'PBP C',
        'product_list': product_list,
        'filter_type': filter_type,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)


@login_required(login_url='/login')
def create_product(request):
    form = ProductForms(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, 'Product created successfully!')
        return redirect('main:show_main')

    return render(request, "create_product.html", {'form': form})


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
    return render(request, "product_detail.html", {'product': product})


@login_required(login_url='/login')
def show_xml(request):
    product_list = Product.objects.all().order_by('-created_at')
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


@login_required(login_url='/login')
def show_json(request):
    products = Product.objects.all().order_by('-created_at')
    data = [
        {
            'id': product.id,
            "user_id": product.user.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'views': product.views,
            'is_featured': product.is_featured,
            'user': product.user.username,
            'created_at': product.created_at.isoformat(),
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)


@login_required(login_url='/login')
def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


@login_required(login_url='/login')
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'views': product.views,
            'is_featured': product.is_featured,
            'user': product.user.username,
            'created_at': product.created_at.isoformat(),
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, 'Your account has been successfully created!')
        return redirect('main:login')
    return render(request, 'register.html', {'form': form})


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        return response

    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForms(request.POST or None, instance=product)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('main:show_main')

    return render(request, "edit_product.html", {'form': form})


@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('main:show_main')


@csrf_exempt
@login_required(login_url='/login')
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category", "none")
    thumbnail = request.POST.get("thumbnail", "")
    is_featured = str(request.POST.get("is_featured", "")).lower() in ["true", "on"]
    price = int(request.POST.get("price", 0))

    product = Product.objects.create(
        user=request.user,
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price,
    )

    return JsonResponse({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'thumbnail': product.thumbnail,
        'is_featured': product.is_featured,
        'views': product.views,
        'created_at': product.created_at.isoformat(),
    }, status=201)
