from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from account.EmailBackEnd import EmailBackEnd
# Create your views here.
def principal(request):
    return render(request, 'principal/home.html')

def loging(request):
    return render(request, 'accounts/login.html')

# def principal(request):
#     return render(request, 'accounts/login.html')




def doLogin(request):
    if request.method!='POST':
        return HttpResponse("<h2>Invalid Method.</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('psw'))
        if user != None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            user_type = user.user_type
            if user_type == '1':
                return redirect('principal')
            elif user_type == '2':
                return redirect('teacher')

            elif user_type == '3':
                return redirect('student')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('loging')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('loging')

    #return render(request, 'accounts/login.html')


        # user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        # if user != None:
        #     login(request, user)
        #     user_type = user.user_type
        #     #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
        #     if user_type == '1':
        #         return redirect('admin_home')
        #
        #     elif user_type == '2':
        #         # return HttpResponse("Staff Login")
        #         return redirect('staff_home')
        #
        #     elif user_type == '3':
        #         # return HttpResponse("Student Login")
        #         return redirect('student_home')
        #     else:
        #         messages.error(request, "Invalid Login!")
        #         return redirect('login')
        # else:
        #     messages.error(request, "Invalid Login Credentials!")
        #     #return HttpResponseRedirect("/")
        #     return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
