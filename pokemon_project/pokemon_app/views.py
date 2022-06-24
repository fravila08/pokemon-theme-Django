
import json
import random
from random import randint
from webbrowser import get
from django.shortcuts import render  
import requests 
from django.http import HttpResponseRedirect

# from .forms import NameForm
# Create your views here.
def index(request):
   return render(request, 'pages/index.html')

def pokepics(request):
   pokemon_id=request.POST.get("pokemon_id")
   endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
   response = requests.get(endpoint)
   responseJSON=response.json()
   picture={
      "pic":responseJSON["sprites"]["front_default"]
      }
   type_name=responseJSON["types"][0]["type"]["name"]
   other_end_point=f"https://pokeapi.co/api/v2/type/{type_name}"
   response2=requests.get(other_end_point)
   responseJSON2=response2.json()
   i=0
   while i<5:
      id=random.randint(0,(len(responseJSON2["pokemon"])-1))
      last_end_point=responseJSON2["pokemon"][id]["pokemon"]["url"]
      last_response=requests.get(last_end_point)
      last_responseJSON=last_response.json()
      picture.update({"pic"+str(i):last_responseJSON["sprites"]["front_default"]})
      i+=1
   return render(request, 'pages/pokemon.html', picture)









# def getNum(request):
#    print('start')
#    if request.method == 'POST':
#       form = NameForm(request.POST)
#       if form.is_valid():
#          message = form.cleaned_data['message']
#          print('youre here')
#          return HttpResponseRedirect("{% url 'pokemon_app:pics'%}")
#    else:
#          print('No')
#          form=NameForm()
#    return render(request, 'pages/index.html', {'form': form})

       