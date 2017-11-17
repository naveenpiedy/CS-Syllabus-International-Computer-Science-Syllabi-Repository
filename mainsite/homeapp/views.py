from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import DocumentForm
from .models import Document


# def index(request):
#     return render(request, 'homeapp/dashboard.html')

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'homeapp/dashboard.html', {
        'form': form
    })