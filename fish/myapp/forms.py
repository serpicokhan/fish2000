from django import forms
from myapp.models import *
from django.conf import settings
import logging
from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.models import Group
class SysUserForm(forms.ModelForm):
    #CustomerId = forms.ModelChoiceField(queryset=Customer.objects.all())



    class Meta:
        model = SysUser
        fields = '__all__'
class MessageForm(forms.ModelForm):
    toUser = forms.ModelChoiceField(label="مخاطب",queryset=SysUser.objects.all(),empty_label='به کی')
    def clean_messageStatus(self):
        if(self.isupdated):
            messageStatus=3
        else:
            messageStatus=2

        return messageStatus



    class Meta:
        model = Message
        fields = '__all__'

class HozurForm(forms.ModelForm):
    name=forms.CharField(widget=forms.Textarea())
   

    class Meta:
        model = HozurGhiab
        fields = '__all__'
class PersonelForm(forms.ModelForm):

    class Meta:
        model = Personnel
        # fields = '__all__'
        fields = ['manager', 'saloon','PNumber','FName','LName','NCode','Father','title']

class MessageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea())
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)