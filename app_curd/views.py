from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    if request.method == 'GET':
        return render(request,"index.html",{"objs":[],"seconds":"NaN","counts":"NaN"})
    else:
        query = request.POST.get("query")
        print(query)
        return render(request,"index.html",{"objs":[],"seconds":"NaN","counts":"NaN"})
