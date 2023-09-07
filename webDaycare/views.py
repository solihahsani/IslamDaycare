from pyexpat.errors import messages
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from app_genaral.models import *
from .models import *
from .forms import *


# Create your views here.


#SHOW
def Home(request):
    activities = Activity.objects.all()
    context = {'activities':activities}
    return render(request, 'app_genaral/index/home.html', context)

def Kids_show(request):
    all_kids = Profile_kids.objects.all()
    return render(request, 'app_genaral/kids/kids_show.html',{'all_kids':all_kids})

def Parents_show(request):
    all_parents = Profile_parents.objects.all()
    return render(request, 'app_genaral/parents/parent_show.html',{'all_parents':all_parents})

def emp_show(request):
    all_emp = Profile_emp.objects.all()
    return render(request, 'app_genaral/emp/emp_show.html',{'all_emp':all_emp})

def detaildaycare_show(request):
    all_detail = Detail_daycare.objects.all()
    return render(request, 'app_genaral/daycare/detaildaycare_show.html',{'all_detail':all_detail})

def health_show(request,kids_id):
    kids = Profile_kids.objects.get(id=kids_id)
    healths=Health_kids.objects.filter(profile_kids_id=kids.id)
    print(healths) 
    # all_health = Health_kids.objects.all()
    return render(request, 'app_genaral/health/health_show.html',{'healths':healths,'kids':kids})

def comment_show(request, emp_id):
    emp = Profile_emp.objects.get(id=emp_id)
    comment=Comment.objects.filter(emp_id=emp.id)
    print(comment) 
    # all_Comment = Comment.objects.all()
    return render(request, 'app_genaral/comment/comment_show.html',{'emp':emp,'comment':comment})

def activity_show(request):
    all_activity = Activity.objects.all()
    return render(request, 'app_genaral/activity/activity_show.html',{'all_activity':all_activity})



#form
def kids_form(request):
    # Check the incoming request
   if request.method == 'POST':
        form = Kids_form(request.POST ,request.FILES)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('Kids_show')  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
   else:
       form = Kids_form()
       context = {'form': form}
       return render(request, 'app_genaral/kids/kids_form.html', context)
   
def parent_form(request):
    # Check the incoming request
   if request.method == 'POST':
        form = Parents_form(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('Parents_show')  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
   else:
       form = Parents_form()
       context = {'form': form}
       return render(request, 'app_genaral/parents/parent_form.html', context)

def emp_form(request):
    # Check the incoming request
   if request.method == 'POST':
        form = Emp_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('emp_show')  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
   else:
       form = Emp_form()
       context = {'form': form}
       return render(request, 'app_genaral/emp/emp_form.html', context)
   
def detail_daycareform(request):
    # Check the incoming request
   if request.method == 'POST':
        form = Detail_daycareform(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('detaildaycare_show')  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
   else:
       form = Detail_daycareform()
   context = {'form': form}
   return render(request, 'app_genaral/daycare/detail_daycare.html', context)


def health_form(request,kids_id):
    # Check the incoming request
    # healths = Profile_kids.objects.get(pk=kids_id)
    # new_healths = Health_kids.objects.filter(profile_kids_id=kids_id)
    # context = {'healths': healths, 'new_healths': new_healths}
#    healths=Health_kids.objects.filter(profile_kids_id=kids_id)
#    instance = Profile_kids.objects.get(pk=kids_id)
    if request.method == 'POST':
        form = Health_form(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('Kids_show')  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
    else:
       form = Health_form()
    context = {'form': form}
    return render(request, 'app_genaral/health/health_form.html', context)

def comment_form(request,emp_id):
    # Check the incoming request
   instance = Profile_emp.objects.get(pk=emp_id)
   if request.method == 'POST':
        form = Comment_form(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('comment_show',instance)  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
   else:
       form = Comment_form(instance=instance)
   context = {'form': form}
   return render(request, 'app_genaral/comment/comment_form.html', context)

def activity_form(request):
    # Check the incoming request
   if request.method == 'POST':
        form = Activity_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่ผู้ใช้กรอกเข้าไปในฐานข้อมูล
            return redirect('activity_show')  # ส่งไปยังหน้าที่แสดงว่าสร้างข้อความสำเร็จ
   else:
       form = Activity_form()
   context = {'form': form}
   return render(request, 'app_genaral/activity/activity_form.html', context)



#edit
def  activity_edit(request , activity_id):
    instance =  Activity.objects.get(pk=activity_id)
    
    
    if request.method == 'POST':
        form = Activity_edit(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('activity_show')
    else:
        form = Activity_edit(instance=instance)
    
    return render(request, 'app_genaral/health/health_edit.html', {'form': form})

def  health_edit(request , health_id):
    instance =  Health_kids.objects.get(pk=health_id)
    
    
    if request.method == 'POST':
        form = Health_update(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('Kids_show')
    else:
        form = Health_update(instance=instance)
    
    return render(request, 'app_genaral/health/health_edit.html', {'form': form})



def  kids_edit(request , kids_id):
    instance = Profile_kids.objects.get(pk=kids_id)
    
    if request.method == 'POST':
        form = Kids_update(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('Kids_show')
    else:
        form = Kids_update(instance=instance)
    
    return render(request, 'app_genaral/kids/kids_edit.html', {'form': form})
    
def emp_edit(request , emp_id):
    instance = Profile_emp.objects.get(pk=emp_id)
    
    if request.method == 'POST':
        form = Emp_update(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('emp_show')
    else:
        form = Emp_update(instance=instance)
    
    return render(request, 'app_genaral/emp/emp_edit.html', {'form': form})

def comment_update(request , Comments_id):
    instance = Comment.objects.get(pk=Comments_id)
    
    if request.method == 'POST':
        form = Comment_update(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('emp_show')
    else:
        form = Comment_update(instance=instance)
    
    return render(request, 'app_genaral/comment/comment_edit.html', {'form': form})


def parents_edit(request , parents_id): 
    instance = Profile_parents.objects.get(pk=parents_id)
    
    if request.method == 'POST':
        form = Parents_update(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('Parents_show')
    else:
        form = Parents_update(instance=instance)
    
    return render(request, 'app_genaral/parents/parents_edit.html', {'form': form})
    
def details_edit(request,detail_id):
    instance = Detail_daycare.objects.get(pk=detail_id)
    
    if request.method == 'POST':
        form = Detaildaycare_edit(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('detaildaycare_show')
    else:
        form =Detaildaycare_edit(instance=instance)
    
    return render(request, 'app_genaral/daycare/detaildaycare_edit.html', {'form': form})

#delete
def kids_delete(request, kids_id):
    instance = Profile_kids.objects.get(pk=kids_id)
    instance.delete()
    return redirect("Kids_show")

def parents_delete(request,  parents_id):
    instance = Profile_parents.objects.get(pk= parents_id)
    instance.delete()
    return redirect("Parents_show")

def emp_delete(request, emp_id):
    instance = Profile_emp.objects.get(pk= emp_id)
    instance.delete()
    return redirect("emp_show")

def detail_delete(request, detail_id):
    instance = Detail_daycare.objects.get(pk= detail_id)
    instance.delete()
    return redirect("detaildaycare_show")
def health_delete(request, health_id):
    instance = Profile_kids.objects.get(pk=health_id)
    instance.delete()
    return redirect("health_show")

def comment_delete(request, Comments_id):
    instance = Comment.objects.get(pk=Comments_id)
    instance.delete()
    return redirect("emp_show")

def activity_delete(request, activity_id):
    instance = Activity.objects.get(pk=activity_id)
    instance.delete()
    return redirect("activity_show")