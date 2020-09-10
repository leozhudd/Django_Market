from django import forms
from .models import Goods

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class RegisterForm(forms.Form):
    # email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        exclude = ()
        
        labels = {
            "name":"物品名称",       #用于html页面中显示的名字
            "price":"价格",
            "description":"物品描述",
            "trade_location":"交易地点（校区）",
            "category":"类别",
            "goods_phone":"联系方式",
            "picture":"实物图片"
        }