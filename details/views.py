from django.http import HttpResponse
from details.models import User,BooksDetails,LibraryMember,image
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            if user.is_admin:
                return redirect('details/')  
            else:
                return redirect('books/')  
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def Library_Member(request):
    Member=LibraryMember.objects.all().values() 
    return render(request,'LibrayMember.html',context={"Member":Member})
def Books_Details(request):
    allimage=BooksDetails.objects.all().values()
    return render(request,'BooksDetails.html',context={"allimage":allimage})
def allimages(request):
    this=image.objects.all().values()
    return render(request, 'img.html',context={'this':this})

