import requests
from django.shortcuts import render
from django.http import HttpResponse
from conf.settings import TMC_API_KEY
from tmc.constantes import BASE_TMC_URL_API
from tmc.forms import TmcForm
from tmc.utils import get_tmc


def tmc(request):
    response = ''
    if request.method == 'POST':
        form = TmcForm(request.POST)
        if form.is_valid():
            try:
                url = '{}{}/{}?apikey={}&formato=json'.format(BASE_TMC_URL_API,'2018','09',TMC_API_KEY)
                get_response = requests.get(url)
                response_json = get_response.json()
                data = {
                    'plazo': form.cleaned_data['plazo'],
                    'monto': form.cleaned_data['monto']
                }
                response = get_tmc(response_json['TMCs'], **data)  
            except Exception as error:
                raise Exception(error) 
    else:
        form = TmcForm()
    
    return render(request,'tmc/tmc.html',{ 'response': response, 'form': form })
