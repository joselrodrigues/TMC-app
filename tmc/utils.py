def get_tmc(args, **kwargs):
    
    plazo = kwargs.get('plazo')
    uf = kwargs.get('monto')
    tmc = ''

    if plazo < 90:
        if uf <= 5000:
            tmc = over_tmc('26', args)
        else:
            tmc = over_tmc('25', args)

    elif plazo >= 90:  
        if uf <= 50:
            tmc = over_tmc('45', args)
        elif 200 >= uf > 50:
            tmc = over_tmc('44', args)
        elif 5000 >= uf > 200:
            tmc = over_tmc('35', args)
        else:
            tmc = over_tmc('34', args)
    return tmc

def over_tmc(tipo, args):
    tmc_values = ''
    for tmc in args:
        if tmc['Tipo'] == tipo:
            tmc_values = tmc
    return tmc_values