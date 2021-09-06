from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from datetime import datetime as date


# Create your views here.

def home(request):
    
    if request.method=='POST':
        city=request.POST['input']
        get_data=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric'+   '&appid=faecd118f554b1a20db1f77b81c226de').read()
        list_of_data=json.loads(get_data)
        current_day=date.today().strftime("%A")
        current_date=date.today()
        c_day=current_day
        c_date=current_date.date()
        city_name=city
        my_data={

            "City": str(list_of_data['sys']['country']),
            "Temperature": str(list_of_data['main']['temp']),
            "Wind": str(list_of_data['wind']['speed']),
            "Status": str(list_of_data['weather'][0]['main']),
            
            
        }

    
        return render(request,'index.html',{"my_data":my_data,"c_day":c_day,"c_date":c_date,"c_name":city_name})
    else:
        current_day=date.today().strftime("%A")
        current_date=date.today()
        c_day=current_day
        c_date=current_date.date()
        my_data={

            "City": "null",
            "Temperature": "null",
            "Wind": "null",
            "Status": "null",
            


        }
        return render(request,'index.html',{"my_data":my_data,"c_day":c_day,"c_date":c_date})