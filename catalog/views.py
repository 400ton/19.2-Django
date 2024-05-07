from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({telephone}): {message}')
    return render(request, 'catalog/contacts.html')


