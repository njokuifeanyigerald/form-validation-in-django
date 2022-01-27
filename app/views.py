from django.shortcuts import render, redirect
from .models import CommentModel
from .forms import CommentForm


def home(request):
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        'form': form
    }
        
    return render(request, 'home.html', context)