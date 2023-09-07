from django import forms 
from .models import *

class Kids_form(forms.ModelForm):
    class Meta: 
        model = Profile_kids
        fields = '__all__'
        labels ={
            "kids_name":"ชื่อ",
            "kids_lname":"นามสกุล",
            "kids_birth":"วัน/เดือน/ปี",
            "kids_gender":"เพศ",
            "kids_image": "อับโหลดรูปเด็ก",
            "parents":"ชื่อผู้ปกครอง"
        }
        # widgets = {
        #     'kids_name': forms.TextInput(attrs={
        #         'class': 'form-control col-xl-8'
        #     }),
        #     'kids_lname': forms.TextInput(attrs={
        #         'class': 'form-control col-xl-8'
        #     }),
        #     'kids_age': forms.TextInput(attrs={
        #         'class': 'form-control col-xl-8'
        #     }),
        #     'kids_month': forms.TextInput(attrs={
        #         'class': 'form-control col-xl-8'
        #     }),
           
            
        # }

class Parents_form(forms.ModelForm):
    class Meta: 
        model = Profile_parents
        fields = '__all__'
        labels ={
            "parents_name":"ชื่อ",
            "parents_lname":"นามสกุล",
            "parents_email":"อีเมล์",
            "parents_address":"ที่อยู่",
            "parents_tel": "เบอร์โทร",
            "parents_usertype":"ประเภท"
        }
        widgets = {
            'parents_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_lname': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_address': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_tel': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
           
            
        }

class Emp_form(forms.ModelForm):
    class Meta: 
        model = Profile_emp
        fields = '__all__'
        labels ={
            "emp_name":"ชื่อ",
            "emp_lname":"นามสกุล",
            "emp_email":"อีเมล์",
            "emp_address":"ที่อยู่",
            "emp_tel": "เบอร์โทร",
            "emp_usertype":"ประเภท",
            "emp_image":"รูปพนักงาน"
        }
        widgets = {
            'emp_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_lname': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'emp_email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_address': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_tel': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
           
            
        }
class Detail_daycareform(forms.ModelForm):
    class Meta: 
        model = Detail_daycare
        fields = '__all__'
        labels ={
            "gm_kids":"ลุกขึ้นนั่งได้จากที่นอนอยู่โดยไม่ใช่มือเกาะ ",
            "fm_kids":"ใช้นิ้วหัวแม่มือ และนิ้วอื่นๆ หยิบของขึ้นจากพื้น",
            "rl_kids":"ทำตามคำสั้งง่ายๆ เมื่อใช้ ท่าทาง ประกอบ เช่น ตบมือ โบกมือ",
            "ps_kids":"ใช้นิ้วหยิบอาหารกินได้",
            "profile_kids": "เด็ก",
            "profile_emp":"พนักงานที่ทำการประเมิน"
            
            
        }
       

class Health_form(forms.ModelForm):
    class Meta: 
        model = Health_kids
        fields = '__all__'
        labels ={
            "health_name":"ชื่ออาการ",
            "health_drug": "ยา",
            "profile_kids":"ชื่อเด็ก",
            "parents_id":"ชื่อผู้ปกครอง",
        }
        widgets = {
            'health_name': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'health_drug': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
           
          
        }

class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        labels ={
            "comment":"ความคิดเห็น",
            "score": "คะแนน/100",
            "comment_date":"วันที่",
            "parents":"ชื่อผู้ปกครอง",
            'emp':"ชื่อพนักงาน"
        }
        widgets = {
            
            'comment': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'score': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'comment_date': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
            
        }

class Activity_form(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        labels ={
            "kids_id":"ชื่อเด็ก",
            "emp":"ชื่อพนักงาน",
            "activity_name":"ชื่อกิจกรรม",
            "activity_description":"อธิบายกิจกรรม",
            "activity_equipment":"อุปกรณ์ในการจัดกิจกรรม",
            "activity_date":"วันที่จัดกิจกรรม",
            "activity_image":"รูปกิจกรรม"
        }
        widgets = {
            'activity_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
             'activity_description': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
             'activity_equipment': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'activity_equipment': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'activity_date': forms.DateInput(attrs={'type': 'date'})
             
               
        }

#edit
class Activity_edit(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        labels ={
            
            "activity_name":"ชื่อกิจกรรม",
            "activity_description":"อธิบายกิจกรรม",
            "activity_equipment":"อุปกรณ์ในการจัดกิจกรรม",
            "activity_date":"วันที่จัดกิจกรรม",
            "activity_image":"รูปกิจกรรม"
        }
        widgets = {
            'activity_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
             'activity_description': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
             'activity_equipment': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'activity_equipment': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'activity_date': forms.DateInput(attrs={'type': 'date'})
             
               
        }
        

class Comment_update(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment','score']
        labels ={
            "comment":"ความคิดเห็น",
            "score": "คะแนน/100",
            
        }
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'score': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
           
            
        }
class Health_update(forms.ModelForm):
    class Meta: 
       model = Health_kids
       fields = ['health_name', 'health_drug']
       labels ={
            "health_name":"ชื่ออาการ",
            "health_drug": "ยา",
        }
       widgets = {
            'health_name': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'health_drug': forms.Textarea(attrs={
                'class': 'form-control col-xl-8 '
            }),
        }

class Parents_update(forms.ModelForm):
    class Meta: 
        model = Profile_parents
        fields = '__all__'
        labels ={
            "parents_name":"ชื่อ",
            "parents_lname":"นามสกุล",
            "parents_email":"อีเมล์",
            "parents_address":"ที่อยู่",
            "parents_tel": "เบอร์โทร",
            "parents_usertype":"ประเภท"
        }
        widgets = {
            'parents_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_lname': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_address': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'parents_tel': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),  
            
        }

class Emp_update(forms.ModelForm):
     class Meta: 
        model = Profile_emp
        fields = '__all__'
        labels ={
            "emp_name":"ชื่อ",
            "emp_lname":"นามสกุล",
            "emp_email":"อีเมล์",
            "emp_address":"ที่อยู่",
            "emp_tel": "เบอร์โทร",
            "emp_usertype":"ประเภท",
            "emp_image":"รูปพนักงาน"
        }
        widgets = {
            'emp_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_lname': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'emp_email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_address': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_tel': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
           
            
        }

class Kids_update(forms.ModelForm):
     class Meta: 
        model = Profile_kids
        fields = ['kids_name','kids_lname','kids_gender','kids_image']
        labels ={
            "kids_name":"ชื่อ",
            "kids_lname":"นามสกุล",
            "kids_birth":"วัน/เดือน/ปี",
            "kids_gender":"เพศ",
            "kids_image": "อับโหลดรูปเด็ก",
            
        }
        widgets = {
            'kids_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'kids_lname': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
           
            
        }

class Emp_update(forms.ModelForm):
     class Meta: 
        model = Profile_emp
        fields = '__all__'
        labels ={
            "emp_name":"ชื่อ",
            "emp_lname":"นามสกุล",
            "emp_email":"อีเมล์",
            "emp_address":"ที่อยู่",
            "emp_tel": "เบอร์โทร",
            "emp_usertype":"ประเภท",
            "emp_image":"รูปพนักงาน"
        }
        widgets = {
            'emp_name': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_lname': forms.TextInput(attrs={
                'class': 'form-control col-xl-8 '
            }),
            'emp_email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_address': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            }),
            'emp_tel': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
           
            
        }

class Detaildaycare_edit(forms.ModelForm):
     class Meta: 
        model = Detail_daycare
        fields = ['gm_kids','fm_kids','rl_kids','ps_kids']
        labels ={
            "gm_kids":"ลุกขึ้นนั่งได้จากที่นอนอยู่โดยไม่ใช่มือเกาะ ",
            "fm_kids":"ใช้นิ้วหัวแม่มือ และนิ้วอื่นๆ หยิบของขึ้นจากพื้น",
            "rl_kids":"ทำตามคำสั้งง่ายๆ เมื่อใช้ ท่าทาง ประกอบ เช่น ตบมือ โบกมือ",
            "ps_kids":"ใช้นิ้วหยิบอาหารกินได้",
            
            
        }



        