from django.contrib import messages,auth
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileDetailForms, AddBlogForm
from .models import Account, ProfileDetails
from customerportal.views import _cart_id
from customerportal.models import CartItem, MyCart
from blog.models import Blog

def Register(request):
    if request.method == "POST":
        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name,
                last_name = last_name,
                phone_number = phone_number,
                email = email,
                password = password,
                username = username,
            )
            user.phone_number = phone_number
            user.save()
            messages.success(request ,"Registration Successful")
            return redirect('register')
        

    else:
        form = RegistrationForm

    context = {
        'form':form,
    }
    return render(request, 'accounts/customer_register.html', context)

def Login_User(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            try:
                cart = MyCart.objects.get(cart_id = _cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()

                if is_cart_item_exists:
                    cart_items = CartItem.objects.filter(cart=cart)

                    for item in cart_items:
                        item.user = user
                        item.save()
                
            except:
                pass
            login(request, user)
            print(user)
            #messages.success(request, "Tou are now logged in")
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid Password")
            return redirect("login")

    else:

        return render(request, 'accounts/customer_login.html',)
@login_required(login_url = 'login')
def Logout(request):
    logout(request)
    messages.success(request,'You are logged out')
    return redirect('login')

def MyOrder(request):

    user = request.user
    total = 0
    tax = 0
    quantity = 0

    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)

    else:
        pass

    my_items = []
    for item in cart_items:
        product_name = item.product.name
        my_items.append(product_name)

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2*total)/100
    grand_total = total + tax
    product_count = len(my_items)

    context = {
        'cart_items':cart_items,
        "grand_total":grand_total,
        'tax' : tax,
        'quantity':quantity,
        'my_items':my_items,
        'product_count':product_count
    }
    return render(request, "accounts/orders.html", context)

@login_required(login_url = 'login')
def Dashboard(request):
    user = request.user
    total = 0
    tax = 0
    quantity = 0
    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)

    else:
        pass
    my_items = []

    for item in cart_items:
        product_name = item.product.name
        my_items.append(product_name)

    string_items = ''.join([str(item) for item in my_items])

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2*total)/100
    grand_total = total + tax

    context = {
        "cart_items":cart_items,
        'grand_total': grand_total,
        'my_items':my_items,
        "string_items":string_items,
        "quantity":quantity,
    }
        
    return render(request,'accounts/index.html', context)

@login_required(login_url = 'login')
def Profile(request):

    user = request.user
    if request.method == 'POST':
        form = ProfileDetailForms(request.POST)

        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            city = form.cleaned_data['city']
            county = form.cleaned_data['county']
            sub_county = form.cleaned_data['sub_county']
            address = form.cleaned_data['address']
            zip_code = form.cleaned_data['zip_code']
            gender = form.cleaned_data['gender']
            secondary_phone = form.cleaned_data['secondary_phone']

            profile_details = ProfileDetails.objects.create(
                user = request.user,
                user_type = user_type,
                city = city,
                county = county,
                sub_county = sub_county,
                address = address,
                zip_code = zip_code,
                gender = gender,
                secondary_phone = secondary_phone,
            )
            profile_details.save()
            messages.success(request, 'Updated Profile Details Successfully')
            return redirect('profile')

    else:
        form = ProfileDetailForms

    context = {
            "form":form,
    }

    

    return render(request, 'accounts/accounts_setting.html',context)

@login_required(login_url = 'login')
def Notifications(request):
    return render(request, 'accounts/accounts_notification.html')

@login_required(login_url = 'login')
def Connections(request):
    return render(request, 'accounts/accounts_connection.html')
@login_required(login_url = 'login')
def AddBlog(request):
    author = request.user
    blog_posts = Blog.objects.filter(author = author)
    blog_post_0 = Blog.objects.filter(author = author)[0]
    blog_post_1 = Blog.objects.filter(author = author)[1]
    blog_post_2 = Blog.objects.filter(author = author)[2]
    if request.method == "POST":
        form = AddBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            blog = form.cleaned_data['blog']

            blog_post = Blog.objects.create(
                author = request.user,
                category = category,
                title =title,
                blog = blog,
                image = image,
               
            )

            blog_post.save()
            messages.success(request, 'Blog Posted To Public DOmain Successfully')
            return redirect('add-blog')

    else:
        form = AddBlogForm

    context = {
        'form':form,
        "blog_posts":blog_posts,
        "blog_post_1":blog_post_1,
        "blog_post_0":blog_post_0,
        "blog_post_2":blog_post_2,
    

    }
    return render(request, "accounts/blog_add.html",context )

def BlogDetail(request):
    return render(request,'accounts/blog_detail.html')