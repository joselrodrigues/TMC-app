import requests
from django.shortcuts import render
from django.http import HttpResponse
from conf.settings import TMC_API_KEY
from tmc.constantes import BASE_TMC_URL_API
from tmc.forms import TmcForm
from tmc.utils import get_tmc


def tmc(request):
    """Funcion que retorna el view de la TMC
    
    Arguments:
        request {Object}
    
    Returns:
        [Object] -- retorna el render con los parametros
    """
    response = ''
    error = ''
    if request.method == 'POST':
        form = TmcForm(request.POST)
        if form.is_valid():
            try:
                fecha_tmc = str(form.cleaned_data['fecha_tmc'])
                tmc_año = fecha_tmc.split('-')[0]
                tmc_mes = fecha_tmc.split('-')[1]
                url = '{}{}/{}?apikey={}&formato=json'.format(BASE_TMC_URL_API,tmc_año,tmc_mes,TMC_API_KEY)
                get_response = requests.get(url)
                response_json = get_response.json()
                if not response_json.get('CodigoHTTP'):      
                    data = {
                        'plazo': form.cleaned_data['plazo'],
                        'monto': form.cleaned_data['monto']
                    }
                    response = get_tmc(response_json['TMCs'], **data)
                else:
                    error =  response_json['Mensaje']   
            except requests.exceptions.RequestException as e:
                error = e 
            except requests.exceptions.Timeout as e:
                error = e
            except Exception as e:
                error = e
    else:
        form = TmcForm()
    
    return render(request,'tmc/tmc.html',{ 'response': response, 'form': form, 'error': error })
