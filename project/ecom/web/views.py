from django.shortcuts import render,redirect
from .models import Product, User, Cart, Anime, Category, current_user
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password, check_password



# Create your views here.


def home(req):
    return render(req, "./web/home.html", {"products": Product.objects.all(),
                                            "categories": Category.objects.all(),
                                            "animes": Anime.objects.all(),
                                            })


def cart(req):
    return render(req, "./web/cart.html")

def product(req):
    return render(req, './web/product.html', {"products":Product.objects.filter(category="Katana")})

def profile(req):
    
    return render(req, './web/profile.html', {"current_user":current_user.objects.filter(id=1)})
    

def signup(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        user = User(lname=lname,fname=fname,email=email, password=hashed_password)
        user.save()
        return redirect('login')
    else:
        return render(request, './web/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                auth_login(request, user)  # Note: Use a different name for your view function
                temp=current_user.objects.filter(id=1)
                temp.delete()
                curr_uer=current_user(id=1, fname=user.fname, lname=user.lname, email=user.email, is_staff=user.is_staff, is_superuser=user.is_superuser, image=user.image)
                curr_uer.save()
                return redirect('home')
            else:
                return render(request, './web/login.html', {'error': 'Invalid password'})
        except User.DoesNotExist:
            return render(request, './web/login.html', {'error': 'Email does not exist'})
    else:
        return render(request, './web/login.html')

        
