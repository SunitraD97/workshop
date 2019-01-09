from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from .forms import TestForm
from .models import Cars

def home(request):
    user_list = Cars.objects.all()
    form = TestForm()
    return render(request,'home.html',{'form':form,'user_list':user_list})

def add(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    return render(request,'add.html',{'form':form})

def edit(request,pk): 
        edit = get_object_or_404(Cars, pk=pk)
        if request.method =='POST':
                form = TestForm(request.POST, instance=edit)
                if form.is_valid():
                        form.save()
                        return redirect('/home/', pk=edit.pk)
        else:
                form = TestForm(instance=edit)
        return render(request,'edit.html',{'form':form,'edit':edit})   


def delete(request,pk):
    dele = get_object_or_404(Cars, pk=pk)
    dele_pk = dele.pk
    dele.delete()
    return redirect('/home/', pk=dele.pk)