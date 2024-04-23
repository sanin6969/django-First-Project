from django.shortcuts import render,redirect
from .models import Movieinfo
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# homepage
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

# create movies details
@login_required(login_url='login')
def create(request):
    if request.POST:
        form=MovieForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form=MovieForm()
    return render(request,'create.html',{'form':form})

# edit details and update them
def edit(request,id):
    to_Edit=Movieinfo.objects.get(id=id)
    form=MovieForm(request.POST,instance=to_Edit,)
    if form.is_valid():
        to_Edit.save()
        return redirect('list')
    form=MovieForm(instance=to_Edit)
    return render(request,'edit.html',{'form':form})

# delete movie from the movie list
def delete(request,id):
    D=Movieinfo.objects.get(id=id)
    D.delete()
    return redirect('list')

# show the list of movies user enetered
@login_required(login_url='login')
def list(request):
    movie_data=Movieinfo.objects.all()
    count=request.session.get('count',0)
    count=int(count)
    count+=1
    request.session['count']=count
    # movie_data=Movieinfo.objects.all().order_by('year') #sort by year
    # movie_data=Movieinfo.objects.filter(rating=9) #filetr method to get the data having rating of 9
    response=render(request,'list.html',{'movies':movie_data,'visits':count},) 
    return response

# clear the sesson in the list.html
def clear_session(request):
    request.session.flush()
    return redirect('list')

# USER : SIGNUP AND LOGIN AND LOGOUT
from django.contrib.auth.models import User

# signup
def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message=str(e)
        return redirect('login')    
    return render(request,'signup.html',{'user':user,'error_message':error_message})



from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import login as LogIn
# login
def login(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            LogIn(request,user)
            return redirect('index/')
        else:
            error_message='invalid username or password , please signup if you are not alreadyuser'    
    return render(request,'login.html',{'error_message':error_message})

# logout 
from django.contrib.auth import logout as django_logout

def logout(request):
    django_logout(request)
    return redirect('login')

