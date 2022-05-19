from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        print('SUBMITTED REGISTRATION')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        print('SUBMITTED LOGIN USER')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
