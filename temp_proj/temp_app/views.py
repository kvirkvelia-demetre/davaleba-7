from django.shortcuts import render


def info(request):
    context = {
        'name': 'დემეტრე',
        'surname': 'კვირკველია',
        'age': 14,
        'height': 174,
    }

    return render(request, 'info.html', context)


def hobbies(request):
    context = {
        'hobbies': ["პიანინოზე დაკვრა", "მონეტების აგროვება"],
    }

    return render(request, 'hobbies.html', context)