from django.shortcuts import render, redirect
from customprofile.forms import CustomUserForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url = "/profile/login/")
def profile(request):
	return render(request, 'customprofile/profile.html')

def register(request):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		if request.method == "POST":
			form = CustomUserForm(request.POST or None)
			if form.is_valid():
				form.save()
				email = request.POST['email']
				password = request.POST['password2']
				user = authenticate(request, email=email, password=password)
				login(request, user)
				return redirect("/")
			else:
				messages.error(request, "Somthing went wrong!")
		else:
			form = CustomUserForm()
		context = {
			'form':form,
		}
		return render(request, 'customprofile/register.html', context)

def loginv(request):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		if request.method == "POST":
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(request, email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect("/")
			else:
				messages.error(request, "User doesn't exist.")
		return render(request, 'customprofile/login.html')

def logoutv(request):
	logout(request)
	return redirect("login-c")

def error404(request, exception):
	return render(request, "customprofile/error.html", status = 404)

def internal500(request):
	return render(request, 'customprofile/error.html')