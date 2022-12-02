from django.shortcuts import render,redirect
from . models import Content, contectTable
from . forms import contactForm
def home (req):
    database = Content.objects.all()
    
    return render (req, 'blog/home.html', {"db":database})

def content(req, pk):
    database = Content.objects.get(id = pk)
    return render(req, 'blog/content.html',{"db":database})

def contactUs(req):
    form = contactForm()
    if req.method == "POST":
        form = contactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'blog/contactus.html', {"form":form})

