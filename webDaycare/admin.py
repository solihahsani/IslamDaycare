from django.contrib import admin
from app_genaral.models import *

class Profilekids(admin.ModelAdmin):
    list_display=['id','kids_name','kids_lname','kids_gender']
class Profileparents(admin.ModelAdmin):
    list_display=['id','parents_name','parents_lname','parents_email','parents_tel','parents_usertype']
class Profileemp(admin.ModelAdmin):
    list_display=['id','emp_name','emp_lname','emp_email','emp_tel','emp_usertype']
class Detaildaycare(admin.ModelAdmin):
    list_display=['id','profile_kids','profile_emp']
class Healthkids(admin.ModelAdmin):
    list_display=['id','profile_kids','health_name']
# Register your models here.
admin.site.register(Profile_kids , Profilekids)
admin.site.register(Profile_parents, Profileparents)
admin.site.register(Profile_emp,Profileemp)
admin.site.register(Detail_daycare,Detaildaycare)
admin.site.register(Health_kids)
admin.site.register(Comment)
admin.site.register(Activity)
