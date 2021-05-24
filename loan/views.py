from django.http import HttpResponse, request, response
from django.shortcuts import render
from .models import Register
from .models import Loan
import datetime 
# Create your views here.

#for accessing registration.html page
def firstpage(request):
    return render(request,'registration.html')

#for saving data in database created in models class Register
def regform(request):
    nm=request.POST.get('fname')
    mobn=request.POST.get('mobileno')
    adr=request.POST.get('address')
    cit=request.POST.get('city')
    st=request.POST.get('state')
    c=Register(name=nm, mobileno=mobn,address=adr,city=cit,state=st)
    c.save()
    return render(request,'done.html',)

#for accessing loanform.html page
def secondpage(request):
    return render(request,'loanform.html')


#for saving data in database created in models class Loan and to calculate the compound insterest
def loancal(request):
        
    ln=request.POST.get('loanamt')
    dura=request.POST.get('loanduration')
    roi=request.POST.get('rateofinterest')
    d=Loan(loanamt=ln, duration_of_loan=dura,ROI=roi)
    d.save()
    x=int(d.loanamt)
    y=int(d.duration_of_loan)
    z=int(d.ROI)
    print(x)
    print(y)
    print(z)
    Ci=(x*(z/100))+x
    print(Ci)
    current_time = datetime.datetime.now() 
    f=current_time.day 
    q=f+y
    return render(request,'payableamt.html',{'result':Ci,'duedate':q,'curdate':f})

#for showing data stored in the backend

def backnd(request):
    reg=Register.objects.all()
    lon=Loan.objects.all()
  
    return render(request,'backend.html',{'re' : reg ,'lo' : lon })