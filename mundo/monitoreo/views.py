from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from datetime import datetime, timedelta
from .forms import BuscarForm

# Create your views here.

def index(request):
    f = datetime.now() - timedelta(1) 
    ay = datetime.now() - timedelta(2) 
    anteayer = ay.strftime('%a')
    before_yesterday = ay.strftime('%d_%b_%Y')
    hour = datetime.now().strftime('%H:%M')
    yesterday = f.strftime('%d_%b_%Y')
    date = datetime.now().strftime('%d_%b_%Y')
    yesterday_route = 'monitoreo/images/graph_'+yesterday+'.png'
    before_yesterday_route = 'monitoreo/images/graph_'+before_yesterday+'.png'
    route = 'monitoreo/images/graph_'+date+'.png'
    context = {
        'route': route,
        'date': date,
        'yesterday': yesterday,
        'yesterday_route': yesterday_route,
        'hour': hour,
        'anteayer': anteayer,
        'before_yesterday_route': before_yesterday_route,
    }
    return render(request, 'monitoreo/index.html', context)

def buscar(request):
    today = datetime.now().strftime('%d_%b_%Y')
    time = datetime.now() - timedelta(1)
    interger_today = int(datetime.now().strftime('%d'))
    yesterday = time.strftime('%d_%b_%Y')
    hour = datetime.now().strftime('%H:%M')
    yesterday_route = 'monitoreo/images/graph_'+yesterday+'.png'
    today_route = 'monitoreo/images/graph_'+today+'.png'

    if request.method == 'POST':
        form = BuscarForm(request.POST) 

        if form.is_valid():

            date_form = form.cleaned_data
            date = date_form['ingresar_fecha'].strftime('%d_%b_%Y')
            if_date = date_form['ingresar_fecha'].strftime('%m')
            if_today = datetime.now().strftime('%m')
            if_year = date_form['ingresar_fecha'].strftime('%Y')
            current_year = datetime.now().strftime('%Y')
            context = {
                'date': date,
                'if_date': if_date,
                'if_year': if_year,
                'current_year': current_year,
                'if_today': if_today, 
                'form': form,
                'today': today,
                'today_route': today_route,
                'interger_today': interger_today,
                'yesterday': yesterday,
                'yesterday_route': yesterday_route,
                'hour': hour,
            }

            return render(request, 'monitoreo/buscar.html', context)


    else:

        form = BuscarForm()

    return render(request, 'monitoreo/buscar.html', {'form': form,
                                                     'today': today,
                                                     'yesterday': yesterday,
                                                     'yesterday_route': yesterday_route,
                                                     'today_route': today_route,
                                                     'interger_today': interger_today,
                                                     'hour': hour,
                                                     })

