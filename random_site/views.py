from django.shortcuts import render
import random

from random_site.models import Son


def generate_random_numbers(request):
    # Birinchi bosqich: Foydalanuvchi kiritgan son
    first_number = int(request.GET.get('first_number', 0))
    # Ikkinchi bosqich: Foydalanuvchi kiritgan son
    second_number = int(request.GET.get('second_number', 0))
    # Uchinchi bosqich: Foydalanuvchi kiritgan son
    third_number = int(request.GET.get('third_number', 0))
    my_data = Son.objects.get(id=1)
    i = random.randint(1, 1000)
    code = Son.objects.get(id=1)
    if my_data.count == True:
        code = Son.objects.get(id=1)
        print("Give buzildi")
    else:
        print("Give buzilishi tugad")
        i = random.randint(1, 2000)
    # Jinja templating uchun context
    context = {
        'first_number': first_number,
        'my_data':my_data,
        'second_number': second_number,
        'third_number': third_number,
        'code':code,
        'i':i
    }

    return render(request, 'index.html', context)
