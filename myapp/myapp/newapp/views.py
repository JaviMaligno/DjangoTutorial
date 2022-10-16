from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members
from django.contrib.auth.models import User, auth #this User is the User database in the admin panel
from django.contrib import messages
#import logging

# Create your views here.
def index(request):
    template = loader.get_template('index.html') #if it's in newapp\templates it works even if we specify a template directory
    #template = loader.get_template('index.html') #more on directories https://stackoverflow.com/questions/3817926/django-can-we-do-loader-get-templatemy-template-txt
    return HttpResponse(template.render())
    #return  render(request, 'myfirst.html') // one-line alternative

def member_names(request):
    mymembers = Members.objects.all().values()
  #output = ""
  #for x in mymembers:
   # output += x["firstname"]
  #return HttpResponse(output)
    #logging.basicConfig(level=logging.INFO)
    #logging.info(mymembers)
    template = loader.get_template('members_table.html')
    context = {
    'mymembers': mymembers,
  }
  # this should be refactored, but it was just to play with key/value pairs
    key = request.GET
    if key:
      try:
        name = key['firstname']
        if name == "all":
          mydata = Members.objects.values_list('firstname')
          return HttpResponse(mydata) 
        else:
          mydata = Members.objects.filter(firstname=name).values()
          return HttpResponse(mydata)
      except:
        return HttpResponse("<h1> Wrong key</h1>", status = 400)

    return HttpResponse(template.render(context)) #optional exra argument request for .render()
    #the one line alternative is 
    #return  render(request, 'index.html', context)

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request)) # Django needs the request for POST methods

def addrecord(request):
  #It adds with the next id to the latest value, so after deletion there are gaps
  #Think about changing it
  x = request.POST['first'] # with GET method on the form (or no specified method) we should use request.GET
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  #return HttpResponseRedirect(reverse('index')) #redirects the user back to the indext view -> index here is a url name (the one given in the kwarg name in urls.py), it's not  the url, that is why reverse() is used, to get the url gith a given name
  #return HttpResponseRedirect('/members/') # redirects to /members/
  return HttpResponseRedirect(reverse('members')) #  does the same

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('members'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('members'))

def register(request):
  #Registers a user in the User database from the admin panel
  if request.method == "POST":
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    if password == password2:
      #we check if the email already exist in the User database
      if email and User.objects.filter(email = email ).exists():
        messages.info(request, "Email already used.")
        return redirect('register') #same as HttpResponseRedirect
      elif User.objects.filter(username = username ).exists():
        messages.info(request, "Username already used.")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return  redirect('login')
    else:
      messages.info(request, "Passwords don't match.")
  else: 
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))