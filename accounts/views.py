from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'accounts/profile.html')

def user_login(request):
    if request.method == "POST":
        # if not request.user.is_authenticated:
        #     return redirect('accounts:login')
        # else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('accounts:profile')
        else:
            return render(request, "accounts/login.html", context={"message": "invalid username or passowrd"})
        print("user is trying to login")
        return render(request, 'accounts/profile') 
    return render(request,'accounts/login.html')

def user_logout(request):
    return render(request,'accounts/logout.html')