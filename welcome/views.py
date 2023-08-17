import requests
from django.shortcuts import render
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        response = requests.get('https://api.weatherbit.io/v2.0/current?city=%s&key=28b86472321742638685a47582687d5c' %city)
        posts = response.json()
        data=posts['data']
        return render(request,"index.html",{"data":data})
    return render(request,"index.html")


