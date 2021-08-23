from django.shortcuts import render ,redirect
from . models import Product
from login.models import User,Order
from django.http import HttpResponse
import datetime
# Create your views here.


def display(request,username = None):
    return render(request,'product/views.html',{
            'username':username
        })


def search(request,username = None):
    if request.method == "POST":
        categary = ["seeds", "seed","fertilizers","fertilisers","pestisides","manures","fertilzer","fertiliser","pestiside","manure"]
        search_value = request.POST['search']
        if search_value.lower() in categary:
            if username != None:
                url = f"/{username}/product/{search_value}"
            else:
                url = f"/product/{search_value}"
            return redirect(url)
        
        if username:
            products = Product.objects.all().filter(id = search_value.lower())
            return render(request,'product/search.html',{
                'products':products,
                'username':username
            })

        else:
            products = Product.objects.all().filter(id = search_value.lower())
            return render(request,'product/search.html',{
                'products':products
            })



def seeds(request,username = None ):
    if username :
        seeds = Product.objects.all().filter(category = 'seeds')
        return render(request, 'product/seeds.html',{
            'seeds': seeds,
            'username':username
            })
    else:
        seeds = Product.objects.all().filter(category = 'seeds')
        return render(request, 'product/seeds.html',{
            'seeds': seeds,
            })


def fertilizers(request,username = None ):
    if username :
        fertilizers = Product.objects.all().filter(category = 'fertilizers')
        return render(request, 'product/fertilizers.html',{
            'fertilizers': fertilizers,
            'username':username
            })
    else:
        fertilizers = Product.objects.all().filter(category = 'fertilizers')
        return render(request, 'product/fertilizers.html',{
            'fertilizers': fertilizers ,
            })


def pesticides(request,username = None):
    if username :
        pestisides = Product.objects.all().filter(category = 'pestisides')
        return render(request, 'product/pestisides.html',{
            'pestisides': pestisides,
            'username':username
            })
    else:
        pestisides = Product.objects.all().filter(category = 'pestisides')
        return render(request, 'product/pestisides.html',{
            'pestisides': pestisides,
            })

def manures(request,username = None):
    if username :
        manures = Product.objects.all().filter(category = 'manures')
        return render(request, 'product/manures.html',{
            'manures': manures,
            'username':username
            })
    else:
        manures = Product.objects.all().filter(category = 'manures')
        return render(request, 'product/manures.html',{
            'manures': manures,
            })

def view(request,productname,username=None):
    if username:
        product = Product.objects.get(pk = productname)
        return render(request,'product/view_product.html',{
        'product':product,
        'username':username
        })
    else:
        product = Product.objects.get(pk = productname)
        return render(request,'product/view_product.html',{
        'product':product
    })

def vieworder(request,username=None):
    if username:
        current_user = request.user
        user = User.object.get(pk=current_user.phone_number)
        if user.is_admin:
            return render(request,'product/orders.html', {
                'username':username
            })


def confirm_order(request,productname,username= None):
    current_user = request.user
    id = current_user.phone_number
    user = User.object.get(pk = id)
    product = Product.objects.get(pk = productname)

    name = username
    productname = productname
    price = product.price
    date_required = request.POST['date_required']
    quantity = request.POST['quantity']
    address = user.address   
    total = int(price) * int(quantity)
    address = address.split(',')
    if username:    
        return render(request,'product/confirm_order.html',{
            'username':username,
            'name' : name,
            'productname' : productname,
            'price' : price,
            'date_required' : date_required,
            'quantity' : quantity,
            'address' : address,
            'total' : total,
            })
    else:
        return redirect("/login")

def confirmed(request,productname,username=None):
    if request.method == "POST":
        current_user = request.user
        id = current_user.phone_number
        user = User.object.get(pk = id)
        product = Product.objects.get(pk = productname)

        name = username
        productname = productname
        price = product.price
        date_required = request.POST['date_required']
        quantity = request.POST['quantity']
        address = user.address

        order = Order.objects.create(user = name,product_name=productname,quantity=quantity,price=price,
        date_required=date_required,address=address)

        return render(request,'product/orders.html',{
            'username':username
        })


def vieworders(request,username=None):
    today = datetime.date.today()
    orders = Order.objects.all()
    for order in orders:
        if order.date_required < today:
            order.delete()
    return render(request,'product/view_orders.html',{
        'username' : username,
        'orders' : orders
    })
