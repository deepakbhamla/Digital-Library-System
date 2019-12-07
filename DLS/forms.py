from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=30)
    auther=forms.CharField(label='Auther',max_length=30)
    publisher=forms.CharField(label='Publisher',max_length=30)
    price=forms.FloatField(label='Price')
    copy=forms.IntegerField(label='Copy')

class SearchForm(forms.Form):
    title=forms.CharField(label='',max_length=30)

class profileForm(forms.Form):
    fname=forms.CharField(label='first Name',max_length=30)
    lname=forms.CharField(label='last Name',max_length=30)
    email=forms.CharField(label='Email',max_length=30)
    phone=forms.IntegerField(label='Phone')
