from django.shortcuts import render , HttpResponseRedirect
from .forms import ClubForm
from . import models

def index(request):

    liste=list(models.Club.objects.all())
    return render (request, 'football/index.html',{'liste': liste})



def ajout(request):
    if request.method == "POST":
        form = ClubForm(request)
        if form.is_valid():
            club = form.save()
            return render(request, "football/affiche.html", {"club": club})
        else:
            return render(request, "football/ajout.html", {"form": form})

    else:
        form = ClubForm()
        id = ""
        return render(request, "football/ajout.html", {"form": form, 'id' : id})




def traitement(request):
    cform = ClubForm(request.POST)
    if cform.is_valid():
        club= cform.save()
        return HttpResponseRedirrect("/football/")
    else:
        return render(request,"football/ajout.html",{"form": cform})

def affiche (request , id ):
        club=models.Club.objects.get(pk = id)
        return render(request,"football/affiche.html",{"club":club})

def update(request,id):
    club=models.Club.objects.get(pk=id)
    form = ClubForm(club.dico() )
    return render(request,'football/ajout.html',{'form':form,"id":id})

def updatetraitement (request,id):
    cform = ClubForm(request.POST)
    if cform.is_valid():
        club = cform.save(commit= False)
        club.id=id
        club.save()
        return HttpResponseRedirect("/football/")
    else:
        return render(request, "football/ajout.html", {"form": cform, "id":id} )

def delete(request,id):
    club = models.Club.objects.get(pk=id)
    club.delete()
    return HttpResponseRedirect("/football/")