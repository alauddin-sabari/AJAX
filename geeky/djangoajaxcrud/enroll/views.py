from django.shortcuts import render
from enroll.models import User
# Create your views here.
from .forms import StudentRegistration
#import JsonResponse
from django.http import JsonResponse
def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form':form, 'stu':stud})

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt # exemtp mean mukti dea ba bad dea : this decorator is used to remove csrf token error or avoid csrf token error and doesn't provide any security
def save_data(request): # for update and save both purpose we use this function
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid(): # validation checking require because if user enter wrong data then it will not save
            name =  request.POST['name']
            email =  request.POST['email']
            password = request.POST['password']
            studentID = request.POST.get('studentID') # this studentID comes from ajax data
            if studentID == '':
                newUser = User(name=name, email=email, password=password)
            else:
                newUser = User(id=studentID,name=name,email=email,password=password) # id is primary key
            
            
            newUser.save()
            stud = User.objects.values()
            print(stud)
            student_data = list(stud) # since need to pass this data to ajax (inside success function response) so need to convert into list
            print(student_data)
            return JsonResponse({'status':'Save', 'student_data': student_data})
        else:
            form = StudentRegistration(request.POST)
            return JsonResponse({'status':0})
     
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid') #sid comes from ajax data
        print(id)
        pi = User.objects.get(pk=id) # pk means primary key and get means get the data from database
        pi.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({'status':0})
    
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        #find the students belong to this id
        student = User.objects.get(pk=id)
        #convert into json format
        student_data = {"id":student.id, "name": student.name, "email": student.email, "password": student.password}
        # this JSON file is needed to pass in ajax response to populate the data into html form left side
         
        return JsonResponse(student_data)
    else:
        return JsonResponse({"status":0})