
import json
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
   print(pokemon_id)
   endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
   response = requests.get(endpoint)
   responseJSON=response.json()
   picture={
      "pic":responseJSON["sprites"]["front_default"]
      }
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

       