
from django.urls import path,include

from EmpApp import views
urlpatterns=[

# path('',views.index,name='index'),
path('',views.profile,name='profile')

]
