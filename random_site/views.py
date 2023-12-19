from django.shortcuts import render
import random

def generate_random_numbers(request):
    # Birinchi bosqich: 1 dan 4000 gacha random son
    first_random_number = random.randint(1, 4000)

    # Ikkinchi bosqich: 1 dan 3000 gacha random son
    second_random_number = random.randint(1, 3000)

    # Uchinchi bosqich: Foydalanuvchi kiritgan son
    third_number = int(request.GET.get('third_number', 0))

    # Jinja templating uchun context
    context = {
        'first_random_number': first_random_number,
        'second_random_number': second_random_number,
        'third_number': third_number,
    }

    return render(request, 'index.html', context)
