from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from home.models import contact
from django.contrib import messages
from service.models import services
from practice.models import practiceadmin


# Create your views here.


def home(request):
    servicesdata=services.objects.all()# making dynamic (getting data from database to template file)
    data={'servicesdata':servicesdata} 
    
    return render (request,'portfolio.html',data)
def practice(request,slug):
    practicesss=practiceadmin.objects.all()
    datas={'practicesss':practicesss}
    return render(request,'practice.html',datas,slug)
def we(request):
    return render (request,'we.html' ) 
def us(request ,id):
    return render (request,'us.html') 
def second(request):
    return render(request,'second.html')     


  
''' def signup(request):
    if request.method=="post":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.PosT['pass1']
        pass2=request.POST['pass2']
        ln=contact(username=username,fname=fname,lname=lname,email=email,pass1=pass1,pass2=pass2)
        ln.save()
        messages.success(request,'your form has been submitted successfully')
        return redirect('/signin')


        
    return render(request,'signup.html') 
def signin(request):
    if request.method=='post':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        ln1=contact(username=username,pass1=pass1)
        ln1.save()
    return render(request,'signin.html')    

def signout(request):
    return render(request,'signout.html')  
def add(request):
    finalans=0
    data={}
    try:
        n1=int(request.post['text1'])
        n2=int(request.post['text2'])
        finalans=n1+n2
        data={
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
    except:
        pass    
            
    return render(request,'add.html',data) 

def aboutme(request):
    return render(request,'aboutme.html')
def services(request):
    messages.success(request,'yes you ')
    return render(request,'services.html')   
def contact1(request):
    if request.method=="post":
        email=request.POST['email']
        password=request.POST['password']
        if len(email)<20 or len(password<4):
            messages.error(request,'please fill up form correctly')
        else:
            ln=contact(email=email,password=password)
            ln.save()
            messages.success(request,'your form is submitted successfully')    
    return render(request,'contact1.html')
    shift+alt+a for commenting multiple lines 

 '''''' 
def userform(request):
    n3=0
    data={}
    
    try:
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        n3=(n1+n2)
        data={
            'n1':n1,
            'n2':n2,
            'n3':n3
        }

        return HttpResponseRedirect
        



    except:
        pass
    return render(request,'userform.html',data)


def calculator(request):

    try:
        c=0
        data={}
        if request.method=='post':
            n1=eval(request.POST['n1'])
            n2=eval(request.POST['n2'])
            opr=request.POST['ans']
            if opr== "+":
                c=(n1+n2)
            elif opr=='-':
                c=(n1-n2)
            elif opr=='*':
                c=(n1*n2)
            elif opr=='/':
                c=(n1/n2) 
            data={'n1':n1,'n2':n2,'n3':c}    
    except:
        pass                      
            
    return render(request,'calculator.html',data)  '''  
 

               


               

    
    

