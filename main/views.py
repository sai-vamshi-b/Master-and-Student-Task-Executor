from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,"main/index.html")

def signup(request):

	if request.method == "POST":

		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		myuser = User.objects.create_user(username, email, pass1)
		myuser.first_name = firstname
		myuser.last_name = lastname

		myuser.save()
		
		messages.success(request, "Your account has been created!")

		return redirect('signin')

	return render(request,"main/signup.html")

def signin(request):

	if request.method == "POST":

		username = request.POST['username']
		pass1 = request.POST['pass1']

		user = authenticate(username=username, password=pass1)

		if user is not None:
			login(request, user)
			firstname = user.first_name
			return render(request, "main/index.html", {'firstname':firstname})

		else:
			messages.error(request, "Bad credentials!")
			return redirect('home')

	return render(request,"main/signin.html")

def signout(request):
	logout(request)
	messages.success(request, "Logged Out Successfully!")
	return redirect('home')