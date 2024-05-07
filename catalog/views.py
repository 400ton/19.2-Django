from django.shortcuts import render
import datetime


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('feedback.txt', 'a') as file:
            file.write(f'{timestamp}, {name},{telephone}: {message}\n')

    return render(request, 'catalog/contacts.html')


