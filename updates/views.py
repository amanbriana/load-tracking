from django.shortcuts import render
from django.http import HttpResponse
from updates.forms import updateForm
from updates.models import loadStatus
from datetime import datetime

# Create your views here.

def loadUpdate(request):
    if request.method == 'POST':
        form = updateForm(request.POST)
        if form.is_valid():
            load_update = form.save(commit=False)
            load_update.date = datetime.now()
            load_update.save()
        loadUpdates = loadStatus.objects.all()
        return render(request, "loadupdates.html", { 'loadupdates' : loadUpdates } ) 
    else:
        form = updateForm
    return render(request, "loadform.html", { 'form' : form } ) 


def loads(request):
    loadUpdates = loadStatus.objects.all()
    return render(request, "loadupdates.html", { 'loadupdates' : loadUpdates } ) 

