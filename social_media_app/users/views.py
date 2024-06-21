from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User 
from .models import Profile


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()


                #the new user after signup will redirect to the signup page
                #user_login=authenticate(username,password)
                #login(request,user_login)
                

                #create a profile object for the new user
                user_model=User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                
                messages.info(request,"account created")
                return redirect('login')
                


                
        else:
            messages.info(request,"Password did not match")
            return redirect('signup')
    else:
        return render(request,'registration.html')




def loginPage(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')



@login_required
def feeds(request):
    return render(request, 'index.html')




@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    user_profile=Profile.objects.get(user=request.user)
    return render(request,"account_settings.html",{'user_profile':user_profile})

@login_required
def followers(request):
    return render(request, 'friendslist.html')




