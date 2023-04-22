from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from part1.models import data
from django.contrib import messages

def go(request):
    if request.method == 'POST':
        c1 = request.POST['country1']
        c2 = request.POST['country2']
        if c1 and c2:
            data_obj1 = data.objects.get(c=c1).t
            data_obj2 = data.objects.get(c=c2).t 
            data_obj1=data_obj1.split(',')
            data_obj2=data_obj2.split(',')


            context ={'data_obj1':data_obj1,'data_obj2':data_obj2,'country1':c1,'country':c2}
            return  render(request,'part1/compare.html',context)       
        
        elif c1:
            country =c1
            data_obj = data.objects.get(c=country).t
            data_obj=data_obj.split(',')
            
            context={'data_obj':data_obj,'country':country}
            return render(request, 'part1/datac.html', context)
        







def index(request):
    return render(request,'part1/index.html')
def show(request):
    country = request.GET.get('country')
    
    data_obj = data.objects.get(c=country).t
    links=data.objects.get(c=country).links
    data_obj=data_obj.split(',')
    
    
               
    context={'data_obj':data_obj,'country':country,'links':links}

    

        
    return render(request, 'part1/datac.html', context)



        

        



