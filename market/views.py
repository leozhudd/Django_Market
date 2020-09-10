from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, RegisterForm, GoodsForm
from django.contrib.auth.models import User
from market.models import Category,Goods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    goods_all = Goods.objects.all()
    category_list = Category.objects.all()
    user_id = request.user.id
    return render(request, 'index.html',
        {
            'goods_all':goods_all,
            'category_list':category_list,
        }
    )

def index_category(request,category_id):
    category_list = Category.objects.all()
    goods_all = Goods.objects.filter(category=category_id)
    return render(request, 'index.html',
        {
            'goods_all':goods_all,
            'category_list':category_list
        }
    )


def loginView(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "PLZ CHECK!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            if User.objects.filter(username=username): # 如果存在这个账号
                user = authenticate(username=username, password=password)
                if user and user.is_active:
                        login(request, user)
                        return redirect('../index')
                else:
                    message = "WRONG PASSWORD"
            else:
                message = "NO USER"
        return render(request,'login.html', locals())
    
    login_form = UserForm()
    return render(request,'login.html', locals())

def register(request):        
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                
                if User.objects.filter(username=username):  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户
                d=dict(username=username,password=password1,email=email,is_staff=0,is_superuser=1)
                new_user = User.objects.create_user(**d)
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面

    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logoutView(request):
    logout(request)
    return redirect('/index/')

def goods_page(requset, goods_id):
    
    # if request.user.is_authenticated:
    #     user = request.user
    #     user_profile = UserProfile.objects.get(user = user)
    # else:
    #     user_profile = []
    # comment_form = CommentForm()
    
    goods = Goods.objects.get(id=goods_id)
    context_dic = {'goods':goods}
    return render(requset, 'items.html',context_dic)


def search(request):
    key_word = request.GET.get('keyword')
    print(key_word)
    category_list = Category.objects.all()
    goods_list = Goods.objects.filter(name__contains=key_word)
    return render(request, 'index.html',
        {
        'categories':category_list,'goods_all':goods_list
        }
    )

def add_goods(request):
    if request.method == "POST":
        goods_form = GoodsForm(request.POST, request.FILES)
        if goods_form.is_valid():
            goods = goods_form.save(commit=True)

            username = request.user.username
            goods.seller = User.objects.get(username=username)
            goods.save()
            return index(request)
    else:
        goods_form = GoodsForm()
    
    if request.user.is_authenticated:
        user = request.user
    user_goods = Goods.objects.filter(seller=user)
    category_list = Category.objects.all()
    return render(request, 'add_goods.html', locals())


def profile(request):
    if request.user.is_authenticated:
        user = request.user
    user_goods = Goods.objects.filter(seller=user)

    category_list = Category.objects.all()
    return render(request, 'profile.html',
        {
            'user':user,
            'user_goods':user_goods,
            'category_list':category_list,
        }
    )
