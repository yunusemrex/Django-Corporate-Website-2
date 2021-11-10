from django.shortcuts import render
from main_pages.models.main_pages import Pages


def pricing(request):
    prices = Pages.objects.get(title='Prices')
    return render(request, 'sections/pricing.html', context={
        'prices' : prices
    })