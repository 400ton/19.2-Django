from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('feedback.txt', 'w') as file:
            file.write(f'{name},{telephone}, {message}')

    return render(request, 'catalog/contacts.html')


