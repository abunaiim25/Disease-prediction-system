from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from store.models import Profile

from store.froms import CustomerUserForm


def register(request):
    form = CustomerUserForm()
    
    #post
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('/login')
        
    context = {'form': form}
    return render(request, "store/auth/register.html", context)



def loginpage(request):
    if request.user.is_authenticated:
         messages.warning(request, "You are already logged in")
         return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            user = authenticate(request, username=name, password=passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
        return render(request, "store/auth/login.html")
    

    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect('/')


#-----------Profile------------
def my_profile(request):
     #Profile get
    userprofile = Profile.objects.filter(user=request.user).first()
    
    context = {'userprofile':userprofile}
    return render(request, "store/auth/my_profile.html", context)


def profile_update(request):
    if request.method == 'POST':
         #User table
        currentuser = User.objects.filter(id=request.user.id).first()
        currentuser.username =  request.POST.get('username')
        currentuser.email =  request.POST.get('email')
        currentuser.save()
        
        #if not Profile.object.filter(user=request.user):
        # Profile.objects.filter(user=request.user).first()
        if not Profile.objects.filter(user=request.user):
            profile = Profile()
            profile.user = request.user
            profile.full_name = request.POST.get('full_name')
            profile.phone = request.POST.get('phone')
            profile.bio = request.POST.get('bio')
            #image
            if len(request.FILES) != 0:
                profile.image = request.FILES['image']
                
            profile.save()
            messages.success(request, "Profile Updated Successfully")
        else:
            profile = Profile.objects.filter(user=request.user).first()
            profile.user = request.user
            profile.full_name = request.POST.get('full_name')
            profile.phone = request.POST.get('phone')
            profile.bio = request.POST.get('bio')
            #image
            if len(request.FILES) != 0:
                profile.image = request.FILES['image']
            profile.save()


    return redirect('/')

            
        