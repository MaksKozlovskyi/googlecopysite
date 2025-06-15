from django.shortcuts import render, redirect
from .forms import RegisterForm

def index(request):
    return render(request, 'main/index.html')

def reg(request):
    return render(request, 'main/reg.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # або на головну сторінку
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})
