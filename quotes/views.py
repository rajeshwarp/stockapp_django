from django.shortcuts import render
from django.views.generic import CreateView

from .models import Stock
import requests
import json
from django.forms import forms
from django.views import View


# Create your views here. pk_040e8167739b43628cad0d45905e5db7
# https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_040e8167739b43628cad0d45905e5db7

def api_request():
    return requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_040e8167739b43628cad0d45905e5db7')


def home(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_040e8167739b43628cad0d45905e5db7")
        try:
            api = json.loads(api_request.content)
            return render(request, 'home.html', {'api': api})
        except Exception as e:
            api = 'error'
            return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "enter ticker"})


def about(request):
    return render(request, 'about.html')


def add_stock(request):
    #pass
    if request.method == 'POST':
        stocktoadd = request.POST['addstock']
        stk= Stock()
        stk.ticker=stocktoadd
        stk.save()

    ticker = Stock.objects.all()
    return render(request, 'add_stock.html', {'ticker': ticker})


# class AddStock(CreateView):
#     model = Stock
#     fields = [
#         "ticker",
#     ]
