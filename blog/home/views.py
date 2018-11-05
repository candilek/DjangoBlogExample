from django.shortcuts import render,HttpResponse


def home_view(request):
    if request.user.is_authenticated():   #kayıtlı kullanıcı siteye giriş yaptıysa
        context={
            'isim':'Dilek'
        }
    else:
        context ={
            'isim':'misafir'
        }

    return render(request,'home.html',context)






#render metodunun ilk parametresi request,
#2. parametresi servis edeceğimiz html dosyası
#3. parametre ise contex key:value şeklinde içerik değeridir.

# Create your views here.
