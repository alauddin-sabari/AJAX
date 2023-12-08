from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.
from .models import user_profile
def index(request):
    # return HttpResponse("Hello World")
    
        return render(request, 'formsubprj/home.html')
def create_user(request):
    if request.method == "POST":
            print('---\n inside post create user view')
            user_name = request.POST.get('username')
            name = request.POST.get('name')
            email = request.POST.get('email')
            bio = request.POST.get('bio')
            phone = request.POST.get('phone')
            user_profile.objects.create(user_name=user_name,name=name,email=email,bio=bio,phone=phone)
            print(user_name,name,email,bio,phone)
            
            return JsonResponse({'name':name})
     