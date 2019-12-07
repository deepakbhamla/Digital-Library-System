from django.shortcuts import render
from DLS.forms import NewBookForm , SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from DLS import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('DLS/login_DLS.html')

def userLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('DLS/view-books')
        else:
            data['error']='Incorrect Password or Username'
            res=render(request,'DLS/login_DLS.html',data)
            return res
    else:
        return render(request,'DLS/login_DLS.html')
@login_required(login_url='/DLS/login')
def searchBook(request):
    form=SearchForm()
    res=render(request, 'DLS/search_book.html',{'form':form})
    return res
@login_required(login_url='/DLS/login')
def search(request):
    form=SearchForm(request.POST)
    book=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'DLS/search_book.html',{'form':form,'book':book})
    return res
@login_required(login_url='/DLS/login')
def delete(request):
    book=request.GET['bookid']
    form=models.Book.objects.filter(id=book)
    form.delete()
    return HttpResponseRedirect('DLS/view-books')
@login_required(login_url='/DLS/login')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.bookid=form.data['bookid']
        book.title=form.data['title']
        book.auther=form.data['auther']
        book.publisher=form.data['publisher']
        book.price=form.data['price']
        book.copy=form.data['copy']
        return HttpResponseRedirect('DLS/view-books')
@login_required(login_url='/DLS/login')
def edit_book(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    field={
        'title':book.title,
        'auther':book.auther,
        'publisher':book.publisher,
        'price':book.price,
        'copy':book.copy,

    }
    form=NewBookForm(initial=field)
    doc={'form':form,'book':book}
    res=render(request, 'DLS/edit_book.html',doc)
    return res
@login_required(login_url='/DLS/login')
def ViewBooks(request):
    books=models.Book.objects.all()
    dic={'books':books}
    res=render(request,'DLS/view_book.html',dic)
    return res

@login_required(login_url='/DLS/login')
def addBook(request):
    form=NewBookForm()
    res=render(request,'DLS/new_book.html',{'form':form})
    return res

@login_required(login_url='/DLS/login')
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.auther=form.data['auther']
        book.publisher=form.data['publisher']
        book.price=form.data['price']
        book.copy=form.data['copy']
        book.save()
        return HttpResponseRedirect('DLS/view-books')
