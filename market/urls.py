from django.urls import path, re_path
import market.views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('index/', market.views.index, name="index"),
    path('login/', market.views.loginView),
    path('register/', market.views.register),
    path('logout/', market.views.logoutView),
    
    path('goods/<int:goods_id>', market.views.goods_page, name="goods"),
    #从url中读取id这个参数，并传递给views函数

    path('goods/<int:goods_id>/<int:modi_flag>', market.views.goods_page_modi),

    path('search/', market.views.search),
    path('add_goods/',market.views.add_goods, name="add_goods"),

    path('index/<int:category_id>', market.views.index_category),
    path('profile/', market.views.profile),

    path('delete/<int:goods_id>', market.views.delete),

    re_path('media/(?P<path>.*)',serve,
    {'document_root': settings.MEDIA_ROOT})
]
