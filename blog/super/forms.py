from django import  forms
from django.contrib.auth.models import User

class Userlogin(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True, error_messages={'required': '姓名必填',
                                                                                       'min_length': '姓名最短2个字符',
                                                                                       'max_length': '姓名最长10个字符'})
    userpwd = forms.CharField(max_length=20, min_length=6, required=True, error_messages={'required': '密码必填',
                                                                                     'min_length': '密码最短6个字符',
                                                                                     'max_length': '密码最长20个字符'})

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username':'没有该用户的信息！'})

        return self.cleaned_data