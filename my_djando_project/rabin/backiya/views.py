from django.shortcuts import render,redirect
from backiya.models import Dates

# Create your views here.
def index(request):
   mydata=Dates.objects.all()
   if(mydata!=""):
      return render(request,"index.html",{"dates":mydata})
   else:
       return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
    
    

def adddate(request):
    if request.method=="POST":
        name=request.POST["name"]
        city=request.POST["city"]
        email=request.POST["email"]
        contect=request.POST["contect"]

        object=Dates()
        object.Name=name
        object.City=city
        object.Email=email
        object.Contect=contect
        object.save()
        mydata=Dates.objects.all()
        return redirect("index")
    return render(request,"index.html")




def update (request,id):
  mydata=Dates.objects.get(id=id)
  if request.method=="POST":
      name=request.POST["name"]
      city=request.POST["city"]
      email=request.POST["email"]
      contect=request.POST["contect"]
       
      mydata.Name=name
      mydata.City=city
      mydata.Email=email
      mydata.Contect=contect
      mydata.save()
      return redirect("index")
  return render(request,"update.html",{"data":mydata})

def deletedata(request,id):
    mydata=Dates.objects.get(id=id)
    mydata.delete()
    return redirect("index")
 