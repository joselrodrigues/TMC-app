import requests
from django.shortcuts import render
from django.http import HttpResponse
from conf.settings import TMC_API_KEY
from tmc.constantes import BASE_TMC_URL_API


# Create your views here.


def tmc(request):
    url = '{}{}?apikey={}&formato=json'.format(BASE_TMC_URL_API,'2018',TMC_API_KEY)
    try:
       response = requests.get(url)
    except Exception as error:
        pass
    
    return render(request,'tmc/tmc.html',{'response': response.json()})
