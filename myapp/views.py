from django.shortcuts import render
from myapp.models import Account
from django.core.mail import send_mail
# Create your views here.
def default(request):
    resp=render(request,'home.html')
    return resp
def newuser(request):
    resp=render(request,'register.html')
    return resp
def forgot(request):
    if(request.method=='GET'):
        resp=render(request,'forgotpass.html')
        return resp
    else:
        u = request.POST.get('user')
        e = request.POST.get('email')
        qs = Account.objects.filter(userid=u,email=e)
        count = qs.count()
        if (count > 0):
            ps=qs[0].password
            send_mail('password recovery','password is:'+ps,'mayank1119gupta@gmail.com',[e])
            return render(request, 'forgotpass.html',{'msg':'your password is send on your mail'})
        else:
            return render(request, 'forgotpass.html', {'msg':'Invalid Userid or Email'})

def login(request):
    u=request.POST.get('user')
    p=request.POST.get('pass')
    e=request.POST.get('email')
    m=request.POST.get('mob')
    t=request.POST.get('type')
    picture=request.FILES.get('image')
    picture=u+'.jpg'
    acc=Account(userid=u,password=p,email=e,mobile=m,type=t,balance=1000,picture=picture)
    try:
        acc.save()
        resp=render(request,'register.html',{'msg':'Account Open Successfully...'})
        return resp
    except Exception as e:
        resp = render(request, 'register.html', {'msg':'Something went wrong,please try with different userid'})
        return resp
def auth(request):
    if(request.method=='GET'):
        return render(request, 'login.html')
    else:
        u=request.POST.get('user')
        p=request.POST.get('pass')
        qs=Account.objects.filter(userid=u,password=p)
        count=qs.count()
        if(count>0):
            request.session['user']=u
            row=qs.first()
            request.session['image']=row.picture.url
            return render(request,'login.html')
        else:
            return render(request,'home.html',{'msg':'Invalid Userid or Password'})

def checkbalance(request):
    u=request.session.get('user')
    row=Account.objects.get(userid=u)
    return render(request,'checkbalance.html',{'row':row})

def depositamt(request):
    if(request.method=='GET'):
        return render(request,'depositamt.html')
    else:
        amt=request.POST.get('amt')
        amt=int(amt)
        u = request.session.get('user')
        row = Account.objects.get(userid=u)
        row.balance=row.balance+amt
        row.save()
        return render(request,'depositamt.html',{'msg':'Amount Deposited'})

def withdrawamt(request):
    if (request.method == 'GET'):
        return render(request, 'withdrawamt.html')
    else:
        amt = request.POST.get('amt')
        amt = int(amt)
        u = request.session.get('user')
        row = Account.objects.get(userid=u)
        row.balance = row.balance - amt
        row.save()
        return render(request, 'withdrawamt.html', {'msg': 'Amount Withdrawn'})

def updatepass(request):
    if (request.method == 'GET'):
        return render(request, 'updatepass.html')
    else:
        ps = request.POST.get('pass')
        u = request.session.get('user')
        row = Account.objects.get(userid=u)
        row.password = ps
        row.save()
        return render(request, 'updatepass.html', {'msg': 'Password Updated'})
def logout(request):
    resp=render(request,'logout.html')
    return resp
