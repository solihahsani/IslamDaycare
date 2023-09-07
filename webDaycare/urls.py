from django.urls import path , include
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('',view=Home,name='Home'),
    path('Kids-show',view=Kids_show,name='Kids_show'),
    path('Parents_show',view=Parents_show,name='Parents_show'),
    path('emp_show',view=emp_show,name='emp_show'),
    path('detaildaycare_show',view=detaildaycare_show,name='detaildaycare_show'),
    path('health_show/<int:kids_id>/',view=health_show,name='health_show'),
    path('comment_show/<int:emp_id>/',view=comment_show,name='comment_show'),
    path('activity_show',view=activity_show,name='activity_show'),
    

    path('kids_form',view=kids_form,name='Kids_form'),
    path('parent_form',view=parent_form,name='parent_form'),
    path('emp_form',view=emp_form,name='emp_form'),
    path('detail_daycareform',view=detail_daycareform,name='detail_daycareform'),
    path('health_form/<int:kids_id>/',view=health_form,name='health_form'),
    path('comment_form /<int:emp_id>/',view=comment_form,name='comment_form'),
    path('activity_form ',view=activity_form,name='activity_form'),
    
    path('kids_edit/<int:kids_id>/',view=kids_edit,name='kids_edit'),
    path('emp_edit/<emp_id>',view=emp_edit,name='emp_edit'),
    path('parents_edit/<int:parents_id>/',view=parents_edit,name='parents_edit'),
    path('health_edit/<int:health_id>/',view=health_edit,name='health_edit'),
    path('details_edit/<int:detail_id>/',view=details_edit,name='details_edit'),
    path('comment_update/<int:Comments_id>',view=comment_update,name='comment_update'),
    path('activity_edit/<int:activity_id>/',view=activity_edit,name='activity_edit'),
    

    path('kids_delete/<int:kids_id>/',view=kids_delete,name='kids_delete'),
    path('emp_delete/<emp_id>',view=emp_delete,name='emp_delete'),
    path('parents_delete/<int:parents_id>/',view=parents_delete,name='parents_delete'),
    path('detail_delete/<int:detail_id>/',view=detail_delete,name='detail_delete'),
    path('health_delete/<int:health_id>/',view=health_delete,name='health_delete'),
    path('comment_delete/<int:Comments_id>',view=comment_delete,name='comment_delete'),
    path('activity_delete/<int:activity_id>',view=activity_delete,name='activity_delete'),
   


    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)