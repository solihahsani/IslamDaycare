from django.db import models

# Create your models here.

class Profile_parents(models.Model):
    parents_name = models.CharField(max_length=100,default="")
    parents_lname = models.CharField(max_length=100,default="")
    parents_address = models.TextField(default="")
    parents_email = models.EmailField(max_length=100,default="")
    parents_tel = models.CharField(max_length=15, default="")
    parents_usertype = models.CharField(max_length=100,default='ผู้ใช้ทั่วไป')

    def __str__(self):
        return self.parents_name+" "+self.parents_lname

class Profile_kids(models.Model):
    kids_name = models.CharField(max_length=100,default="")
    kids_lname = models.CharField(max_length=100 ,default="")
    kids_birth = models.DateField(null=True,blank=True)
    GENDER_CHOICES= (
         ('male', 'Male'),
         ('female', 'Female'),       
    )
    kids_gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    kids_image = models.ImageField(upload_to='kids', blank=True,null=True)
    parents = models.ForeignKey(Profile_parents, on_delete=models.CASCADE )

    def __str__(self):
        return self.kids_name+" "+self.kids_lname


class Profile_emp(models.Model):
    emp_name = models.CharField(max_length=100,default="")
    emp_lname = models.CharField(max_length=100,default="")
    emp_address = models.TextField(default="")
    emp_email = models.EmailField(max_length=100,default="")
    emp_tel = models.CharField(max_length=15, default="")
    EMP_CHOICES= (
         ('emp_genaral', 'พนักงานทั่วไป'),
         ('apprentice', 'นักศึกษาฝึกงาน'),       
    )
    emp_usertype = models.CharField(max_length=50, choices=EMP_CHOICES)
    emp_image = models.ImageField(upload_to='emp', blank=True,null=True)
    

    

    def __str__(self):
        return self.emp_name+" "+self.emp_lname
    
class Detail_daycare(models.Model):
    date_detail=models.DateField(auto_now_add=True, blank=True, null=True)
    GM_KIDS= (
         ('ทำได้ดี', 'ทำได้ดี'),
         ('ทำได้','ทำได้'), 
         ('ทำไม่ได้','ทำไม่ได้')        
    )
    gm_kids = models.CharField(max_length=50, choices=GM_KIDS,blank=True, null=True)
    FM_KIDS= (
         ('ทำได้ดี', 'ทำได้ดี'),
         ('ทำได้','ทำได้'), 
         ('ทำไม่ได้','ทำไม่ได้')     
    )
    fm_kids = models.CharField(max_length=50, choices=FM_KIDS,blank=True, null=True)
    RL_KIDS= (
         ('ทำได้ดี', 'ทำได้ดี'),
         ('ทำได้','ทำได้'), 
         ('ทำไม่ได้','ทำไม่ได้')       
    )
    rl_kids = models.CharField(max_length=50, choices=RL_KIDS,blank=True, null=True)
    PS_KIDS= (
         ('ทำได้ดี', 'ทำได้ดี'),
         ('ทำได้','ทำได้'), 
         ('ทำไม่ได้','ทำไม่ได้')      
    )
    ps_kids = models.CharField(max_length=50, choices=PS_KIDS,blank=True, null=True)
    profile_emp=models.ForeignKey(Profile_emp,on_delete=models.CASCADE)
    profile_kids=models.ForeignKey(Profile_kids,on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_kids.kids_name+""+self.profile_kids.kids_lname
    
class Health_kids(models.Model):
    health_name=models.TextField(max_length=100,default="")
    health_drug=models.TextField(max_length=100 ,default="")
    health_date=models.DateField(auto_now_add=True,null=True,blank=True)
    parents_id = models.ForeignKey(Profile_parents, on_delete=models.CASCADE )
    profile_kids=models.ForeignKey(Profile_kids,on_delete=models.CASCADE)

    def __str__(self):
         return self.profile_kids.kids_name+""+self.profile_kids.kids_lname
    
class Comment(models.Model):
    comment = models.TextField(max_length=100,default="")
    score = models.IntegerField(null=True, blank=True)
    comment_date = models.DateField(auto_now_add=True,null=True,blank=True)
    parents = models.ForeignKey(Profile_parents, on_delete=models.CASCADE )
    emp=models.ForeignKey(Profile_emp,on_delete=models.CASCADE)

    def __str__(self):
         return self.emp.emp_name+""+self.emp.emp_lname

class Activity(models.Model):
    kids_id=models.ManyToManyField(Profile_kids)
    emp=models.ForeignKey(Profile_emp,on_delete=models.CASCADE)
    activity_name=models.CharField(max_length=50,null=True,blank=True)
    activity_date=models.DateField(null=True,blank=True)
    activity_equipment=models.CharField(max_length=50,null=True,blank=True)
    activity_description=models.TextField(max_length=1000,default="")
    activity_image = models.ImageField(upload_to='activity', blank=True,null=True)

    def __str__(self):
         return self.activity_name
    



   

